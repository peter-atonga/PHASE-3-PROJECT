# Task and Project Management System

## Overview
The Task and Project Management System is a lightweight, command-line interface (CLI) application designed to help users efficiently manage tasks and projects. The application addresses common challenges such as missed deadlines, poor task prioritization, and lack of visibility into project progress.

## Features
- **Project Management**:
  - Create, view, update, and delete projects.
  - Manage project deadlines and descriptions.

- **Task Management**:
  - Create tasks with priorities and due dates.
  - View tasks by project and track their statuses (Pending, In Progress, Completed).
  - Update or delete tasks as needed.

- **Reporting**:
  - View upcoming and overdue tasks.
  - Generate lists of completed tasks.

- **Command-Line Interface (CLI)**:
  - Simple commands for user interaction:
    - `add_project`
    - `add_task`
    - `list_projects`
    - `list_tasks`
    - `complete_task`
    - `delete_task`

## Project Structure
- `db.py`: Handles database connection and initialization.
- `models.py`: Defines the data models for Project and Task tables.
- `main.py`: Acts as the entry point to the application, providing CLI commands for user interaction.

## Installation

### Prerequisites
- Python 3.6 or higher
- Pipenv for managing the virtual environment

### Setup
1. Clone the repository:
   ```bash
   git clone 
   cd task-project-management
