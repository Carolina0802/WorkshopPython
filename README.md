# WorkshopPython

This project demonstrates the use of Clean Architecture in reading and processing csv files.

## Project Structure

```plaintext
app/
│
├── main/
│   ├── application/
│   │   ├── interfaces/
│   │   │   └── csv_reader_service_interface.py
│   │   └── services/
│   │       └── csv_reader_service.py
│   │
│   ├── domain/
│   │   ├── entities/
│   │   │   └── csv_data.py
│   │   └── helpers/
│   │       └── json_file_path.py
│   │
│   ├── infrastructure/
│   │   ├── di/
│   │   │   └── dependency_injection.py
│   │   └── repositories/
│   │       └── csv_repository.py
│   │
│   └── resource/
│       └── data.csv
│
└── main.py
```

## Prerequisites

- Python 3.x
- Virtualenv

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