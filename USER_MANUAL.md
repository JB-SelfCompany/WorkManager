# Руководство пользователя - Система управления служащими по контракту. 

## Содержание
1. [Общее описание](#общее-описание)
2. [Термины и определения](#термины-и-определения)
3. [Начало работы](#начало-работы)
4. [Интерфейс приложения](#интерфейс-приложения)
5. [Пошаговые инструкции](#пошаговые-инструкции)
6. [Управление данными](#управление-данными)
7. [Часто задаваемые вопросы](#часто-задаваемые-вопросы)
8. [Устранение неполадок](#устранение-неполадок)

## Термины и определения

### Основные понятия
- **Служащий**: Физическое лицо с контрактом в системе.
- **Личный номер**: Уникальный идентификатор каждого служащего.
- **Дата начала контракта**: Дата начала действия контракта служащего.
- **Дата окончания контракта**: Дата окончания действия контракта служащего.
- **Дневная ставка**: Сумма, выплачиваемая служащему за день.
- **Зарплата**: Общая сумма, рассчитанная на основе количества отработанных дней и дневной ставки.

## Начало работы

### Системные требования
1. **Операционная система**:
   - Windows 10/11 (64-bit)
   - Ubuntu 20.04/22.04/24.04 (64-bit)
   - MacOS 11+ (Big Sur и новее) (64-bit)

2. **Минимальные требования к оборудованию**:
   - Свободное место на диске: 200 МБ
   - Разрешение экрана: Минимум 1024x768

### Установка приложения
1. Перейдите на страницу релизов приложения.
2. Скачайте версию для вашей операционной системы:
   - Для Windows: `WorkerManagementApp.exe`
   - Для Linux: `WorkerManagementApp`
   - Для MacOS: `WorkerManagementApp.app`
3. Запустите скачанный файл:
   - Windows: Двойной клик по `WorkerManagementApp.exe`
   - Linux: 
     ```bash
     chmod +x worker-management
     ./worker-management
     ```
   - MacOS: Двойной клик по `WorkerManagementApp.app`

## Интерфейс приложения

### Главное окно

#### Общие элементы
- **Заголовок окна**: "Contract Worker Management"
- **Размер окна**: Минимум 800x600 пикселей
- **Тема**: Светлая тема по умолчанию

#### Табличное представление
- Отображает всех служащих с их данными и рассчитанными зарплатами.

### Поля ввода
1. **Personal Number**
   - Обязательное поле
   - Пример: "1001"

2. **Full Name**
   - Обязательное поле
   - Пример: "Иванов Иван Иванович"

3. **Start Date**
   - Формат: ГГГГ-ММ-ДД
   - Пример: "2025-01-01"

4. **End Date**
   - Формат: ГГГГ-ММ-ДД
   - Пример: "2025-12-31"

5. **Daily Wage**
   - Сумма, выплачиваемая за день
   - Пример: "500.00"

### Кнопки действий
1. **Add Worker**
   - Добавляет новую запись служащего.
   - Активна только когда все обязательные поля заполнены.

2. **Update Selected**
   - Обновляет данные выбранного служащего.
   - Активна только когда служащий выбран.

3. **Delete Selected**
   - Удаляет выбранного служащего.
   - Требует подтверждения.

## Пошаговые инструкции

### Добавление нового служащего
1. Откройте главное окно.
2. Заполните все поля ввода.
3. Нажмите "Add Worker".
4. Проверьте, что служащий появился в таблице.

### Редактирование служащего
1. Выберите служашего из таблицы.
2. Измените необходимые поля ввода.
3. Нажмите "Update Selected".
4. Проверьте, что изменения сохранены.

### Удаление служащего
1. Выберите служащего из таблицы.
2. Нажмите "Delete Selected".
3. Подтвердите удаление.
4. Проверьте, что служащий удален из таблицы.

## Часто задаваемые вопросы

### Общие вопросы
1. **Как добавить нового служащего?**
   - Откройте главное окно.
   - Заполните форму и нажмите "Add Worker".

2. **Почему не сохраняются изменения?**
   Проверьте:
   - Все обязательные поля заполнены.
   - Правильные форматы данных.
   - Нажата соответствующая кнопка.

3. **Как рассчитывается зарплата?**
   - Зарплаты рассчитываются автоматически на основе длительности контракта и дневной ставки.

### Управление данными
1. **Можно ли восстановить удаленного служащего?**
   - Нет, удаление необратимо.
   - Всегда подтверждайте перед удалением.

2. **Почему не рассчитывается зарплата?**
   Убедитесь:
   - Корректные даты начала и окончания.
   - Положительная дневная ставка.

## Устранение неполадок

### Проблемы с вводом
1. **Личный номер не принимается**
   - Убедитесь в уникальности.
   - Используйте допустимые символы.

2. **Ошибка формата даты**
   - Используйте формат ГГГГ-ММ-ДД.

3. **Изменения не сохраняются**
   - Заполните все обязательные поля.
   - Используйте правильные форматы данных.
   - Нажмите правильную кнопку.

### Общие проблемы
1. **Приложение работает медленно**
   - Закройте ненужные программы.
   - Проверьте свободное место на диске.
   - Очистите временные файлы.

2. **Окно не изменяет размер**
   - Проверьте разрешение экрана.
   - Минимальный размер 800x600.

3. **Проблемы с отображением**
   - Обновите графические драйверы.
   - Проверьте разрешение экрана.
   - Перезапустите приложение.

## Советы по эффективному использованию

### Организация данных
1. **Система именования**
   - Используйте понятные имена.
   - Поддерживайте единообразие.

2. **Управление датами**
   - Проверяйте правильность.
   - Соблюдайте хронологический порядок.

3. **Ведение записей**
   - Поддерживайте справочник служащих.
   - Используйте стандартные единицы.
   - Отслеживайте изменения.

### Безопасность
1. **Регулярное резервное копирование**
   - Создавайте резервные копии `workers.db`.
   - Проверяйте целостность данных.
   - Храните резервные копии отдельно.

2. **Контроль доступа**
   - Ограничьте доступ к приложению.
   - Используйте отдельные учетные записи.
   - Отслеживайте изменения.

3. **Проверка данных**
   - Проверяйте вводимые данные.
   - Исправляйте ошибки немедленно.
   - Ведите журнал изменений.