# Система управления служащими по контракту

Приложение для управления служащими по контракту, включая их данные и расчет заработной платы.

## Возможности

- Добавление новых служащих с личными данными и информацией о контракте.
- Редактирование существующих записей служащих.
- Удаление записей служащих.
- Просмотр таблицы всех служащих с расчетом заработной платы на основе длительности контракта и дневной ставки.
- Проверка вводимых данных в реальном времени для обеспечения целостности данных.

## Системные требования

- Windows 10/11 (64-bit)
- Ubuntu 20.04/22.04/24.04 (64-bit)
- MacOS 11+ (Big Sur и новее) (64-bit)
- Python 3.8+

## Установка

### Простая установка (для пользователей)

1. Скачайте последнюю версию со страницы [Releases](https://github.com/JB-SelfCompany/WorkManager/releases).
2. Запустите исполняемый файл:
   - Windows: `WorkerManagementApp.exe`
   - Linux: `WorkerManagementApp`
   - MacOS: `WorkerManagementApp.app`

### Сборка из исходного кода (для разработчиков)

#### Windows
1. Установите Python 3.8+ с официального сайта: https://www.python.org/
2. Установите Git: https://git-scm.com/
3. Откройте командную строку и выполните:

```cmd
git clone https://github.com/JB-SelfCompany/WorkManager
cd WorkManager
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pyinstaller WorkerManagementApp.spec
```

#### Linux
1. Установите необходимые пакеты:
```bash
sudo apt-get update
sudo apt-get install python3.12 python3.12-venv git
```
2. Клонируйте репозиторий и настройте окружение:
```bash
git clone https://github.com/JB-SelfCompany/WorkManager
cd WorkManager
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
3. Соберите приложение:
```bash
pyinstaller WorkerManagementApp.spec
```

#### MacOS
1. Установите Homebrew (если еще не установлен):
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
2. Установите Python и Git:
```bash
brew install python git
```
3. Клонируйте репозиторий и настройте окружение:
```bash
git clone https://github.com/JB-SelfCompany/WorkManager
cd WorkManager
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
4. Соберите приложение:
```bash
pyinstaller WorkerManagementApp.spec
```

Скомпилированное приложение будет находиться в папке `dist`.

## Использование

### Главное окно

- **Табличное представление**: Отображает всех служащих с их данными и рассчитанной зарплатой.
- **Поля ввода**: Ввод данных служащего (`Personal Number`, `Full Name`, `Start Date`, `End Date`, `Daily Wage`).
- **Кнопки действий**:
  - "Add Worker" - Создает новую запись служащего.
  - "Update Selected" - Обновляет данные выбранного служащего.
  - "Delete Selected" - Удаляет выбранного служащего.

### Управление служащими

1. **Добавление служащего**
   - Заполните все поля ввода.
   - Нажмите "Add Worker".

2. **Редактирование служащего**
   - Выберите служащего из таблицы.
   - Измените поля ввода.
   - Нажмите "Update Selected".

3. **Удаление служащего**
   - Выберите служащего из таблицы.
   - Нажмите "Delete Selected".
   - Подтвердите удаление.

## Структура проекта

- `app.py` - Основной файл приложения с GUI и бизнес-логикой.
- `WorkerManagementApp.spec` - Файл спецификации PyInstaller для сборки приложения.
- `workers.db` - Файл базы данных SQLite для хранения информации о работниках.