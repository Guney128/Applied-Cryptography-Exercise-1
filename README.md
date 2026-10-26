Applied Cryptography – Exercise 1

Prime factorization of integers using trial division, written in Python as part of the Applied Cryptography course (FH Campus Wien, Master's program).

Files

factor.py – Contains the factor() function, which returns the prime factors of an integer as a list.
main.py – Asks the user for an integer, validates the input and prints its prime factors.

Usage

Requires Python 3. Run the program with:

python main.py

Example:

Enter an integer:
12
[2, 2, 3]

Invalid input (e.g. text or numbers that are too small) is rejected and the user is asked again.

How it works

The algorithm divides the number by the smallest possible divisor i, starting at 2. If i divides the number, it is added to the list of factors and the number is divided by it. Otherwise i is increased by one. This repeats until the number is reduced to 1.

Trial division works well for small numbers but becomes impractical for very large ones. This is exactly what the security of RSA relies on: factoring the product of two large primes is computationally infeasible.
