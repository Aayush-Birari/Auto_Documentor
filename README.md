# Simple Command-Line Calculator
=====================================

## Description
------------

A simple command-line calculator that takes two numbers and a mathematical operation as input from the user and displays the result. The calculator supports four basic arithmetic operations: addition, subtraction, multiplication, and division.

## Prerequisites
-------------

* Python 3.6 or later version
* A code editor or IDE for execution

## How to Run
------------

### Clone the Repository

To run the code, you will need to clone the repository. You can do this by running the following command in your terminal:

```bash
git clone https://github.com/your-username/simple-calculator.git
```

Replace `https://github.com/your-username/simple-calculator.git` with the actual repository URL.

### Install Required Packages

Since the code uses Python, you don't need to install any additional packages. You can run the code directly.

### Run the Code

Navigate to the directory where you cloned the repository and run the following command:

```bash
python calculator.py
```

Replace `calculator.py` with the actual name of the Python file.

## Usage
-----

When you run the code, it will prompt you to choose a mathematical operation by entering a number between 1 and 4. Based on your choice, it will ask for two numbers. Then, it will display the result of the operation.

Here's an example usage:

```
1:+, 2:-, 3:*, 4:/
Enter choice (1-4): 1
Num 1: 10
Num 2: 20
Result: 30.0
```

Note that if you choose division and enter 0 as the second number, it will display "Error" instead of attempting division by zero.

## Commit History
----------------

The code has been tested and works as expected. However, you can view the commit history and changes made to the code by running the following command in your local repository:

```bash
git log
```