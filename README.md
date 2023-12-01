# User Logbook

![GitHub stars](https://img.shields.io/github/stars/Sudipta-Trisha/User-Logbook)  ![GitHub forks](https://img.shields.io/github/forks/Sudipta-Trisha/User-Logbook)

This Django-based web application facilitates the management of familial data, specifically focusing on parents and their children. It enables users to effortlessly perform comprehensive CRUD (Create, Read, Update, Delete) operations. Featuring an intuitive user interface and a database model, the application ensures efficient and organized data handling. Additionally, it integrates Django REST Framework for API interactions, enhancing its capabilities for data manipulation and retrieval, making it an ideal solution for users seeking a reliable and versatile system for managing relational data.

## Table of Contents
   * [Features](#features)
   * [System Requirements](#system-requirements)
   * [Installation](#installation)
   * [Entity-Relationship (ER) Model Diagram](#entity-relationship-er-model-diagram)
   * [Usage](#usage)
   * [Contributing](#contributing)
   * [License](#license)

## Features
* <strong>User List</strong>: View a list of users (individuals) with their details, organized in a tabular format. Easily navigate through the list for quick reference.

* <strong>Create User</strong>: Add new user data using a user-friendly form. Capture details such as first name, last name, address, city, state, and zip code.

* <strong>Update User</strong>: Modify existing user data through an editable form. Update details like first name, last name, address, city, state, and zip code.

* <strong>Delete User</strong>: Remove a user record from the system.

* <strong>Responsive Design</strong>: Ensure the application is responsive, adapting to different screen sizes.

## System Requirements
  * Operating System: Windows, macOS, or Linux-based system.
  * Python: 3.11.4
  * Virtual Environment: Use <strong>venv</strong> or <strong>virtualenv</strong> for creating isolated Python environments.
  * Database: SQLite for development (included with Python).
  * Dependencies: Check <strong>requirements.txt</strong> for a list of specific Python packages and versions required for this project.
  * Code Editor: Visual Studio Code, PyCharm, Sublime Text, or any preferred Python code editor.
  * Version Control: Git installed on system.

## Installation

1. Clone the project repository or Download zip file
```bash
  git clone https://github.com/Sudipta-Trisha/UserLogbook.git
```
2. Navigate to directory
```bash
  cd UserLogbook
``` 
3. Install python virtual environment
```bash
  python -m venv myenv
```
4. Activate virtual environment
- On windows
```bash
  myenv\Scripts\activate
```
- On Linux and macOS
```bash
  source myenv/bin/activate
```
5. Install Dependencies
```bash
  pip install -r requirements.txt
```
6. Run Migrations
```bash
  python manage.py migrate
```
7. Start the Development Server
```bash
  python manage.py runserver
```
8. Open the web browser and navigate to **http://127.0.0.1:8000/**
   

## Entity-Relationship (ER) Model Diagram

```plaintext
+------------------+       +------------------+
|     Parent       |       |      Child       |
+------------------+       +------------------+
| id               | 1   * | id               |
| first_name       |<------| parent_id        |
| last_name        |       | first_name       |
| address          |       | last_name        |
| city             |       +------------------+
| state            |
| zip_code         |
+------------------+

```

## Usage
* Access a list of individuals with their details in a tabular format.
* Add new users by filling out a user-friendly form.
* Modify existing user data through an editable form.
* Remove user records from the system.
* Utilize a simple database model for efficient data handling.
* Optionally establish relationships between users.
* Navigate through an intuitive interface for easy interaction.
* Ensure compatibility with different screen sizes (Optional).
* Manage project dependencies using requirements.txt.


## Contributing

I appreciate your interest in contributing to this project. Please check the guidelines in [**Contributing.md**](UserLogbook/CONTRIBUTING.md). Your contributions help make the project better and benefit the entire community.

Feel free to reach out to **sudiptatrisha.19@gmail.com** , if you have any questions or need further assistance regarding the contribution process.

## License

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-orange.svg)](https://www.gnu.org/licenses/gpl-3.0)

This software is licensed under the GNU General Public License (GPL) version 3.

The full text of the GPL can be found in the [**LICENSE**](LICENSE) file.