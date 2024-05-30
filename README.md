# WorkshopPython

This project demonstrates the use of Clean Architecture in reading and processing csv files.

## Project Structure

```plaintext
app/
│
├── __init__.py
│
├── main/
│   ├── __init__.py
│   │
│   ├── application/
│   │   ├── __init__.py
│   │   │
│   │   ├── interfaces/
│   │   │   ├── __init__.py
│   │   │   └── csv_reader_service_interface.py
│   │   │
│   │   └── services/
│   │       ├── __init__.py
│   │       └── csv_reader_service.py
│   │
│   ├── domain/
│   │   ├── __init__.py
│   │   │
│   │   ├── entities/
│   │   │   ├── __init__.py
│   │   │   └── csv_data.py
│   │   │
│   │   └── helpers/
│   │       ├── __init__.py
│   │       └── json_file_path_helpers.py            
│   │       └── csv_repository_helpers.py
│   │
│   ├── infrastructure/
│   │   ├── __init__.py
│   │   │
│   │   ├── di/
│   │   │   ├── __init__.py
│   │   │   └── dependency_injection.py
│   │   │
│   │   └── repositories/
│   │       ├── __init__.py
│   │       └── csv_repository.py
│   │
│   └── resource/
│       ├── __init__.py
│       └── data.csv
│
└── main.py
```

## Prerequisites

- Python 3.x
- Ambiente virtual env

## Installation and Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/Carolina0802/WorkshopPython.git
    cd WorkshopPython
    ```

2. Create and activate a virtual environment:

    On Windows:
    ```bash
    python -m venv env
    .\env\Scripts\activate
    ```

    On macOS and Linux:
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. Install the dependencies ( in este caso no necesitamos instalarlas ):

    ```bash
    pip install -r requirements.txt
    ```
4. Run the main script:

    ```bash
    python main.py
    ```
    You should see an output similar to:
    ```bash
    ID: 1, Name: John Gomez, Age: 30
    ID: 2, Name: Maria Perez, Age: 25
    ID: 3, Name: Pedro Suarez, Age: 20
    ID: 4, Name: Kathe Martinez, Age: 35
    ```