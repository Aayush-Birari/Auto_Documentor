**Simple Command-Line Calculator**
=====================================

**Description**
---------------

This script implements a basic command-line calculator that performs addition, subtraction, multiplication, and division operations. The user is presented with a menu of operations and is prompted to enter their choice, followed by the two numbers to be operated on.

**Prerequisites**
-----------------

*   Python 3.x (tested with Python 3.8 and 3.9)

**How to Run**
--------------

### Steps to Run the Calculator

1.  Save the code in a file named `calculator.py` (or any other name you prefer).
2.  Install Python 3.x (if not already installed) from the official Python website.
3.  Open a terminal or command prompt and navigate to the directory where you saved the `calculator.py` file.
4.  Run the calculator by executing the command `python calculator.py`.

### Example Use Cases

*   Perform simple arithmetic operations, such as adding two numbers:
    ```
python calculator.py
1:+, 2:-, 3:*, 4:/
Enter choice (1-4): 1
Num 1: 2.5
Num 2: 3.5
Result: 6.0
```

*   Attempt to divide by zero:
```bash
python calculator.py
1:+, 2:-, 3:*, 4:/
Enter choice (1-4): 4
Num 1: 10
Num 2: 0
Result: Error
```

Note that if an invalid number is entered, the calculator will display an error message. Similarly, if an invalid operation is chosen, the calculator will display an error message.