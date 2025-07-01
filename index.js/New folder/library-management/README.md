# Library Management System

This project is a simple library management system that allows users to manage books in a library. It provides functionalities to add, remove, and list books, as well as check their availability.

## Project Structure

```
library-management
├── src
│   ├── main.py               # Entry point of the application
│   ├── models
│   │   └── book.py           # Book model with properties and methods
│   ├── controllers
│   │   └── library_controller.py # Manages library operations
│   └── utils
│       └── helpers.py        # Utility functions for input validation and output formatting
├── requirements.txt          # Project dependencies
└── README.md                 # Documentation for the project
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd library-management
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/main.py
   ```

## Features

- Add new books to the library
- Remove books from the library
- List all available books
- Check the availability of a specific book

## Usage

Once the application is running, follow the on-screen prompts to interact with the library management system. You can add, remove, and view books as needed.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.