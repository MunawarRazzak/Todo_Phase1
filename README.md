# Console Todo Application

A simple, in-memory console-based todo application built with Python.

## Features

- Add new todo tasks
- View all todo tasks
- Update existing tasks
- Delete tasks
- Mark tasks as completed

## Prerequisites

- Python 3.13 or higher

## Usage

1. Clone the repository
2. Navigate to the project directory
3. Run `python main.py`
4. Follow the menu prompts to interact with your todo list

## Architecture

The application follows a layered architecture:

- **CLI Layer**: Handles user input and output
- **Service Layer**: Contains business logic for todo operations
- **Domain Layer**: Manages data models and in-memory storage