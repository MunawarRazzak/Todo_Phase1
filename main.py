#!/usr/bin/env python3
"""
Todo Application
===============

A console-based todo application that stores tasks in memory.
"""

from src.services.todo_service import TodoService
from src.cli.cli_interface import CliInterface


def main():
    """Main entry point for the application."""
    # Initialize the todo service and CLI interface
    todo_service = TodoService()
    cli = CliInterface(todo_service)

    # Run the CLI application
    cli.run()


if __name__ == "__main__":
    main()