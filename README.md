# TodoList Project

## Overview

TodoList is a Django-based project for managing a list of tasks. The project includes features for creating, reading, updating, and deleting tasks. The front-end is styled using custom CSS and enhanced with Select2 for dropdowns and Flatpickr for date pickers. Additionally, the project includes a RESTful API using Django REST Framework.

## Features

- Create, Read, Update, Delete (CRUD) functionality for tasks
- Tasks displayed in a table format
- User-friendly forms with enhanced UI components
- API endpoints for task management

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Django REST Framework
- Select2
- Flatpickr

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/todolist.git
   cd todolist
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Apply the migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

### Running the Server

Start the Django development server:

```bash
python manage.py runserver
```

Open your web browser and go to `http://127.0.0.1:8000/`.

## Project Structure

- `todo_app/`
  - `models.py`: Contains the `TaskModel` class.
  - `admin.py`: Registers `TaskModel` in the admin interface and customizes the display.
  - `views.py`: Contains views for creating, reading, updating, and deleting tasks.
  - `forms.py`: Contains form definitions for `TaskModel`.
  - `urls.py`: URL routing for `todo_app`.
  - `serializers.py`: Serializers for API endpoints.

- `templates/`
  - `todo_app/`
    - `base_task.html`: Base template for task-related forms.
    - `create_task.html`: Template for creating a new task.
    - `update_task.html`: Template for updating an existing task.
    - `home.html`: Template for displaying the list of tasks.
    - `TaskModel_confirm_delete`: Template for confirmation of a delete task. 

- `static/`
  - `todo_app/`
    - `css/`
      - `base_task_styles.css`: Styles for task forms.
      - `home_styles.css`: Styles for the home page.

## Change Log

### Initial Setup

- Created `todo_app` model.
- Made and applied migrations.

### Admin Configuration

- Added `__str__` method to `TaskModel`.
- Registered `todo_app` model in admin.
- Overridden `list_display` in admin.

### Model Updates

- Renamed `TodoItem` to `TaskModel`.
- Changed `task` to `task_name` in `models.py`.

### Views and Templates

- Added `show_todolist` function and `home.html`.
- Mapped `show_todolist` view function and URL.
- Renamed `show_todolist` to `read_task`.

### Task Creation

- Created `TaskModelForm`.
- Added `create_task` view function and `create_task.html`.
- Added path for `create_task` view.
- Renamed to `TaskForm`

### Task Update

- Added widget for `deadline`.
- Added hyperlinks for updating tasks.
- Added `update_task.html`.
- Added path for `update_task` view.
- Added `update_task` view function.

### Task Deletion

- Added delete view function.
- Added path for `delete_task` view.
- Added hyperlinks for deleting tasks.

### Refactoring

- Displayed tasks in a table format in `home.html`.
- Created `base_task.html` and refactored `create_task.html` and `update_task.html` to extend from the base template.
- Added CSS styling and configured static files for task templates.
- Enhanced form styling and UI components.
- Refactored `PriorityChoice` and `StatusChoices` keys.

### Django REST Framework

- Added Django REST Framework to `INSTALLED_APPS`.
- Refactored views to class-based views.
- Updated URL patterns for class-based views.
- Added comments to `views.py` and utilized `get_object_or_404` in update and delete views.
- Added `serializers.py`.
- Introduced Django REST Framework viewset and router setup.

## API Endpoints

The API endpoints for managing tasks are as follows:

- `GET /api/tasks/`: List all tasks.
- `POST /api/tasks/`: Create a new task.
- `GET /api/tasks/<id>/`: Retrieve a specific task.
- `PUT /api/tasks/<id>/`: Update a specific task.
- `DELETE /api/tasks/<id>/`: Delete a specific task.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- Django
- Django REST Framework
- Select2
- Flatpickr

For any questions or contributions, please contact tanzilehsan@gmail.com.