# Django File Handling Project

A simple Django application for uploading and displaying files.

## Features

- Upload files (images)
- Display uploaded files
- Deleting files 

## Setup

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Razaklekan113/Django-File-Handling.git
    ```

2. Create and activate a virtual environment (optional):

    ```bash
    python -m venv venv
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python manage.py makemigrations
    ```

     ```bash
    python manage.py migrate
    ```

5. Run the server:

    ```bash
    python manage.py runserver
    ```

6. Open `http://127.0.0.1:8000` in your browser.

## Usage

- Upload files at `http://127.0.0.1:8000/`
- View files at `http://127.0.0.1:8000/list/`
- delete files at `http://127.0.0.1:8000/delete/Id/`

## License

This project is licensed under the MIT License.
