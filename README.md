**Simple Command-Line Calculator**
=====================================

**Description**
---------------

This is a simple command-line calculator that performs basic arithmetic operations such as addition, subtraction, multiplication, division, and squaring. The user is prompted to select an operation and input the necessary numbers to perform the calculation.

**Prerequisites**
----------------

* Python 3.x installed on the system

**How to Run**
---------------

To run this calculator, follow these steps:

1. Save the code in a file named `calculator.py`.
2. Open a terminal or command prompt and navigate to the directory where you saved the file.
3. Run the script using the command `python calculator.py`.
4. Follow the on-screen instructions to select an operation and input the necessary numbers.
5. The calculator will display the result of the calculation.

### Example Use Case

```bash
$ python calculator.py
1:+, 2:-, 3:*, 4:/, 5:^2
Enter choice (1-5): 3
Num 1: 10
Num 2: 5
Result: 50
```

### Running the Calculator in an Environment

To run the calculator in a more interactive environment, you can add a `if __name__ == "__main__":` guard to the script to ensure it is only executed when run directly. Update the script as follows:

```python
def calculator():
    # ...

if __name__ == "__main__":
    calculator()
```

You can then run the script using the command `python calculator.py` and interact with the calculator in a more conventional way.