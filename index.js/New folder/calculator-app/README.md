# Calculator Application

This is a simple calculator application that performs basic arithmetic operations.

## Features

- Addition
- Subtraction
- Multiplication
- Division

## Installation

To install the required dependencies, run the following command:

```
pip install -r requirements.txt
```

## Usage

To use the calculator, you can import the `calculator` module in your Python scripts:

```python
from src.calculator import add, subtract, multiply, divide

result = add(5, 3)
print(result)  # Output: 8
```

## Running Tests

To run the tests for the calculator application, you can use the following command:

```
pytest tests/test_calculator.py
```

Make sure you have `pytest` installed. You can add it to your `requirements.txt` if it's not already included.

## License

This project is licensed under the MIT License.