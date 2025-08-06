# prime-numbers
A Python script that checks if a user-provided number is a prime number by counting its divisors.

# 🧐 Prime Number Checker

This is a command-line Python program that determines if an integer provided by the user is a prime number.

The script prompts for a number and then uses a `for` loop to count how many divisors that number has. Based on the mathematical definition (a prime number has exactly two divisors: 1 and itself), the program informs the user whether the number is prime or not.

## How to Use

1.  Make sure you have Python installed on your system.
2.  Save the code as a `.py` file (e.g., `prime_numbers.py`).
3.  Open your terminal or command prompt.
4.  Run the script with the following command:
    ```sh
    python prime_numbers.py
    ```
5.  Enter the number you wish to check and press Enter to see the result.

## Program Logic

* **Definition of a Prime Number:** The program relies on the definition that a prime number is a natural number greater than 1 that has exactly two distinct positive divisors: 1 and itself.
* **Counting Divisors:**
    * A variable `total_divisors` is initialized to 0.
    * A `for` loop iterates through all numbers from 1 up to the user's number (inclusive).
    * Inside the loop, the condition `if number % check == 0` verifies if the current loop number (`check`) is a divisor of the user's number.
    * If it is a divisor, `total_divisors` is incremented by 1.
* **Final Validation:** After the loop completes, an `if/else` structure checks if `total_divisors` is exactly equal to 2. If it is, the number is prime. Otherwise, it is not.
