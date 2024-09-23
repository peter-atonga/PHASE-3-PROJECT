import datetime
import click
from models import Project, Task  # Absolute import for models
from db import SessionLocal, init_db  # Absolute import for db

# Initialize the database
init_db()

# Create a new database session
session = SessionLocal()

@click.group()
def cli():
    """Task and Project Management CLI"""
    pass

# Add a new project
@cli.command()
@click.option('--name', prompt='Project name', help='The name of the project.')
@click.option('--description', prompt='Project description', help='The description of the project.')
@click.option('--deadline', prompt='Project deadline (YYYY-MM-DD)', help='The deadline for the project.')
def add_project(name, description, deadline):
    """Add a new project."""
    try:
        deadline_date = datetime.strptime(deadline, '%Y-%m-%d').date()
        new_project = Project(name=name, description=description, deadline=deadline_date)
        session.add(new_project)
        session.commit()
        click.echo(f"Project '{name}' added successfully!")
    except ValueError:
        click.echo("Invalid date format. Please use YYYY-MM-DD.")

# Add a task to a project
@cli.command()
@click.option('--project-id', prompt='Project ID', help='The ID of the project to add the task to.')
@click.option('--name', prompt='Task name', help='The name of the task.')
@click.option('--description', prompt='Task description', help='The description of the task.')
@click.option('--priority', prompt='Task priority (High, Medium, Low)', help='The priority of the task.')
@click.option('--due-date', prompt='Task due date (YYYY-MM-DD)', help='The due date for the task.')
def add_task(project_id, name, description, priority, due_date):
    """Add a task to a project."""
    try:
        project = session.query(Project).filter_by(id=project_id).first()
        if project:
            due_date_parsed = datetime.strptime(due_date, '%Y-%m-%d').date()
            new_task = Task(name=name, description=description, priority=priority, due_date=due_date_parsed, project_id=project_id)
            session.add(new_task)
            session.commit()
            click.echo(f"Task '{name}' added to project '{project.name}' successfully!")
        else:
            click.echo(f"Project with ID {project_id} not found.")
    except ValueError:
        click.echo("Invalid date format. Please use YYYY-MM-DD.")

# List all projects
@cli.command()
def list_projects():
    """List all projects."""
    projects = session.query(Project).all()
    if projects:
        for project in projects:
            click.echo(f"ID: {project.id}, Name: {project.name}, Description: {project.description}, Deadline: {project.deadline}")
    else:
        click.echo("No projects found.")

# List tasks for a specific project
@cli.command()
@click.option('--project-id', prompt='Project ID', help='The ID of the project to list tasks for.')
def list_tasks(project_id):
    """List tasks for a specific project."""
    project = session.query(Project).filter_by(id=project_id).first()
    if project:
        tasks = session.query(Task).filter_by(project_id=project_id).all()
        if tasks:
            for task in tasks:
                click.echo(f"ID: {task.id}, Name: {task.name}, Priority: {task.priority}, Due Date: {task.due_date}, Status: {task.status}")
        else:
            click.echo(f"No tasks found for project '{project.name}'.")
    else:
        click.echo(f"Project with ID {project_id} not found.")

if __name__ == '__main__':
    cli()
