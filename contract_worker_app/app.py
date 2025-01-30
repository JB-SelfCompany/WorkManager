import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget,
    QTableView, QPushButton, QLineEdit, QLabel, QMessageBox,
    QHeaderView, QAbstractItemView
)
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QStandardItemModel, QStandardItem
import sqlite3
import re
import os

# Get current working directory
BASE_DIR = os.getcwd()

# Database connection and initialization
DB_PATH = os.path.join(BASE_DIR, 'workers.db')
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS workers (
             personal_number INTEGER PRIMARY KEY,
             full_name TEXT NOT NULL,
             contract_start_date TEXT NOT NULL,
             contract_end_date TEXT NOT NULL,
             daily_wage REAL NOT NULL)''')
conn.commit()

class WorkerManagementApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Contract Worker Management")
        self.setGeometry(100, 100, 800, 600)
        
        # Main layout
        central_widget = QWidget()
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        
        # Table view
        self.table_model = QStandardItemModel()
        self.table_model.setHorizontalHeaderLabels(
            [
                "Personal Number", "Full Name", "Start Date",
                "End Date", "Daily Wage", "Salary"
            ]
        )
        
        self.table_view = QTableView()
        self.table_view.setModel(self.table_model)
        self.table_view.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_view.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        main_layout.addWidget(self.table_view)
        
        # Input fields
        input_layout = QHBoxLayout()
        
        self.input_widgets = []
        labels = ["Personal Number", "Full Name", "Start Date", "End Date", "Daily Wage"]
        for label_text in labels:
            layout = QVBoxLayout()
            label = QLabel(label_text)
            line_edit = QLineEdit()
            layout.addWidget(label)
            layout.addWidget(line_edit)
            input_layout.addLayout(layout)
            self.input_widgets.append(line_edit)
        
        # Set default start date
        self.input_widgets[2].setText(QDate.currentDate().toString(Qt.DateFormat.ISODate))
        
        main_layout.addLayout(input_layout)
        
        # Button layout
        button_layout = QHBoxLayout()
        
        add_button = QPushButton("Add Worker")
        update_button = QPushButton("Update Selected")
        delete_button = QPushButton("Delete Selected")
        
        add_button.clicked.connect(self.add_worker)
        self.table_view.clicked.connect(self.populate_inputs)
        update_button.clicked.connect(self.update_worker)
        delete_button.clicked.connect(self.delete_worker)
        
        button_layout.addWidget(add_button)
        button_layout.addWidget(update_button)
        button_layout.addWidget(delete_button)
        
        main_layout.addLayout(button_layout)
        
        # Load data
        self.load_data()
    
    def load_data(self):
        self.table_model.removeRows(0, self.table_model.rowCount())
        c.execute("SELECT * FROM workers")
        for row_data in c.fetchall():
            # Extract fields from database row
            personal_number, full_name, start_date, end_date, daily_wage = row_data
            
            # Calculate salary
            start_qdate = QDate.fromString(start_date, Qt.DateFormat.ISODate)
            end_qdate = QDate.fromString(end_date, Qt.DateFormat.ISODate)
            days_worked = start_qdate.daysTo(end_qdate)
            salary = days_worked * daily_wage
            
            # Create table items including calculated salary
            items = [
                QStandardItem(str(personal_number)),
                QStandardItem(full_name),
                QStandardItem(start_date),
                QStandardItem(end_date),
                QStandardItem(str(daily_wage)),
                QStandardItem(str(salary))
            ]
            self.table_model.appendRow(items)

    def populate_inputs(self, index):
        row = index.row()
        for i in range(5):  # Populate first 5 fields
            self.input_widgets[i].setText(self.table_model.item(row, i).text())
    def validate_inputs(self):
        required = [
            ("Personal Number", int),
            ("Full Name", str),
            ("Start Date", str),
            ("End Date", str),
            ("Daily Wage", float),
        ]

        values = []
        # Date validation regex
        date_regex = re.compile(r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$')
        
        for i, (name, type_) in enumerate(required):
            value = self.input_widgets[i].text().strip()
            if not value:
                QMessageBox.warning(self, "Input Error", f"{name} is required")
                return False
            
            # Special handling for date fields
            if name in ["Start Date", "End Date"]:
                if not date_regex.match(value):
                    QMessageBox.critical(
                        self,
                        "Date Format Error",
                        f"{name} must be in YYYY-MM-DD format.\nExample: 2025-01-30"
                    )
                    return False
            
            try:
                if type_ == int:
                    values.append(int(value))
                elif type_ == float:
                    values.append(float(value))
                else:
                    values.append(value)
            except ValueError:
                QMessageBox.warning(self, "Input Error", f"Invalid {name}")

        # Calculate salary separately
        start_date = QDate.fromString(values[2], Qt.DateFormat.ISODate)
        end_date = QDate.fromString(values[3], Qt.DateFormat.ISODate)
        daily_wage = values[4]

        days_worked = start_date.daysTo(end_date)
        if days_worked < 0:
            QMessageBox.warning(self, "Date Error", "End date must be after start date")
            return False
        # Calculate salary for display but don't include in DB insert
        salary = days_worked * daily_wage
        
        # Return DB values and salary separately
        return values[:5], salary

    def add_worker(self):
        result = self.validate_inputs()
        if not result:
            return
        
        db_values, salary = result
        
        try:
            # Insert worker data
            c.execute("""
                INSERT INTO workers VALUES (?, ?, ?, ?, ?)
            """, db_values)
            
            # Update table with all 6 values (including salary)
            items = [QStandardItem(str(value)) for value in db_values]
            items.append(QStandardItem(str(salary)))
            self.table_model.appendRow(items)
            
            # Clear inputs after successful addition
            self.clear_inputs()
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, "Error", "Personal number already exists")
    
    def update_worker(self):
        selected = self.table_view.selectedIndexes()
        if not selected:
            QMessageBox.warning(self, "Selection Error", "Please select a worker to update")
            return
        
        row = selected[0].row()
        personal_number = int(self.table_model.item(row, 0).text())
        
        result = self.validate_inputs()
        if not result:
            return
        
        db_values, _ = result  # Unpack only db_values
        
        try:
            c.execute("""
                UPDATE workers SET
                    full_name = ?,
                    contract_start_date = ?,
                    contract_end_date = ?,
                    daily_wage = ?
                WHERE personal_number = ?
            """, (*db_values[1:], personal_number))
            conn.commit()
            self.load_data()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Update failed: {e}")
    
    def delete_worker(self):
        selected = self.table_view.selectedIndexes()
        if not selected:
            QMessageBox.warning(self, "Selection Error", "Please select a worker to delete")
            return
        
        row = selected[0].row()
        personal_number = int(self.table_model.item(row, 0).text())
        
        confirm = QMessageBox.question(
            self, "Confirm Delete",
            "Are you sure you want to delete this worker?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if confirm == QMessageBox.StandardButton.Yes:
            c.execute("DELETE FROM workers WHERE personal_number = ?", (personal_number,))
            conn.commit()
            self.load_data()
    
    def clear_inputs(self):
        for widget in self.input_widgets:
            widget.clear()
        self.input_widgets[2].setText(QDate.currentDate().toString(Qt.DateFormat.ISODate))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WorkerManagementApp()
    window.show()
    sys.exit(app.exec())