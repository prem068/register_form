# Employee Database Management System

This project is a Django-based web application and REST API for managing an employee database. It allows users to perform CRUD (Create, Read, Update, Delete) operations on employee records through a user-friendly interface and API endpoints.

## Features

### Web Application
- **Display Employees**: View a list of all employees with their details.
- **Add Employee**: Insert a new employee record.
- **Update Employee**: Edit an existing employee's details.
- **Delete Employee**: Remove an employee record with a confirmation prompt.
- **Responsive Design**: Styled using Tailwind CSS for a clean and responsive UI.

### REST API
- **GET `/api/employees/`**: Fetch all employees.
- **POST `/api/employees/insert/`**: Add a new employee.
- **PUT `/api/employees/update/<id>/`**: Update an employee by ID.
- **DELETE `/api/employees/delete/<id>/`**: Delete an employee by ID.

## Technologies Used
- **Backend**: Django 5.1.7, Django REST Framework
- **Frontend**: HTML, Tailwind CSS
- **Database**: SQLite3 (default Django database)
- **Python Version**: 3.9 or higher

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/prem068/register_form
   cd register_form

2. **Create and activate a virtual environment**:
   ```
   python -m venv env

   env\Scripts\activate  

3. **Installation dependencies**:
   ```
    pip install -r requirements.txt

4. **Run the development server**:
   ```
   python manage.py runserver