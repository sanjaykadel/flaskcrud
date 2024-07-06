# Flask CRUD Application

This is a simple Flask CRUD generator (Create, Read, Update, Delete) application. 

## Setup

### Create Virtual Environment

1. **Create the virtual environment:**

    ```sh
    python3 -m venv venv
    ```

2. **Activate the virtual environment:**

    - On **Windows**:
        ```sh
        venv\Scripts\activate
        ```
    - On **Unix or MacOS**:
        ```sh
        source venv/bin/activate
        ```

### Install Requirements

1. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

### Run the Application

1. **Run the `main.py` file:**

    ```sh
    python main.py
    ```

## Project Structure


Here’s how to set up a virtual environment, install dependencies from requirements.txt, and run your main.py for a Flask CRUD gen application. I'll also provide a README.md file for you.

    Create a virtual environment:

sh

python3 -m venv venv

    Activate the virtual environment:
        On Windows:

        sh

venv\Scripts\activate

On Unix or MacOS:

sh

        source venv/bin/activate

    Install the requirements:

sh

pip install -r requirements.txt

    Run main.py:

sh

python main.py

README.md

markdown

# Flask CRUD Application

This is a simple Flask CRUD (Create, Read, Update, Delete) application. 

## Setup

### Create Virtual Environment

1. **Create the virtual environment:**

    ```sh
    python3 -m venv venv
    ```

2. **Activate the virtual environment:**

    - On **Windows**:
        ```sh
        venv\Scripts\activate
        ```
    - On **Unix or MacOS**:
        ```sh
        source venv/bin/activate
        ```

### Install Requirements

1. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

### Run the Application

1. **Run the `main.py` file:**

    ```sh
    python main.py
    ```

## Usage

### Use the UI

1. **Fill the form:**
    - Navigate to the form section on the web page.
    - Fill in the required details as needed.

2. **Add columns for fields:**
    - Click the button to add new columns for the fields.
    - Specify the name and type for each field.

3. **Click Preview for Source Code:**
    - Once the form is filled out, click the `Preview` button.
    - This will display the generated source code based on your input.

4. **Click Generate to Download Project as ZIP File:**
    - After previewing the source code, click the `Generate` button.
    - This will generate the project files and provide a link to download the project as a ZIP file.

## Dependencies

Make sure the following dependencies are listed in your `requirements.txt`:

```plaintext
Flask==2.1.1
Flask-WTF==0.14.3
Flask-SQLAlchemy==2.5.1
