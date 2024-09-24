
Inventory Management System Documentation

Introduction

The Inventory Management System is based on CUI, designed to help businesses efficiently manage their inventory, customer information, and supplier details. This documentation provides an overview of the system's functionality, architecture, and requirements.

System Overview

The Inventory Management System consists of several components, including:

Main Program Script:
 
Responsible for presenting a command-line interface to the user and handling user input.

Modules:

main.py: Contains functions for adding, updating, and deleting records from the database.

delete.py: Includes a function for deleting all data from a selected table in the database.

Database: Stores inventory, customer, and supplier information. The system interacts with the database using pyodbc.

Requirements
---------------------------------------
Software Requirements
---------------------------------------
Python 3.x
pyodbc library (for database connectivity)
pandas library (for displaying data)

Hardware Requirements

A computer with sufficient memory and processing power to run Python scripts and connect to a database.
Installation
Install Python: If Python is not already installed on your system, download and install it from the official Python website: python.org.

Install Dependencies:
***************************************************************************************************
Install the pyodbc library by running pip install pyodbc in your command line.
Install the pandas library by running pip install pandas in your command line.
***************************************************************************************************
Setup
Database Setup:

Create a SQL Server database where the inventory, customer, and supplier information will be stored.
Modify the connection string in the main script (main.py) to specify the server and database name.

Project Setup:

Download or clone the project files from the repository.
Ensure that all project files are stored in the same directory.


<Usage>

Running the System:

Open a terminal or command prompt.
Navigate to the directory where the project files are stored.
Run the main program script by executing python main.py.
Menu Navigation:

Use the numeric keys to navigate the menu options and perform various tasks such as adding, updating, or deleting records.

Follow Instructions:

Follow the on-screen instructions to enter server and database information, select menu options, and provide input for adding, updating, or deleting records.

Documentation Structure

Introduction: Overview of the Inventory Management System.

System Overview: Description of system components and architecture.

Requirements:
Software and hardware requirements for running the system.
Installation instructions for required dependencies.

Setup:
Instructions for setting up the database and configuring the project.

Usage:
Steps for running the system and navigating the command-line interface.

Conclusion: Summary of the documentation and system functionality.

Conclusion

This documentation provides a comprehensive guide for understanding, installing, and using the Inventory Management System. For further assistance or inquiries, please refer to the contact information provided in the project documentation or seek support from the project maintainers.




