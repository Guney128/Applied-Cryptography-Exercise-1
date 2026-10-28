Applied Cryptography – Exercise 1

Prime factorization and greatest common divisor (GCD) of integers, written in Python as part of the Applied Cryptography course (FH Campus Wien, Master's program).

Files

factor.py – Contains the factor() function, which returns the prime factors of an integer as a list.
gcd.py – Contains the greatestCommonDivider() function, which computes the greatest common divisor of two numbers from their lists of prime factors.
main.py – Asks the user for two integers, validates the input, prints the prime factors of both numbers and their greatest common divisor.

Usage

Requires Python 3. Run the program with:

python main.py

Example:

Enter two integers:
12
18
[2, 2, 3]
[2, 3, 3]
6

Invalid input (e.g. text or numbers that are too small) is rejected and the user is asked again.

How it works

Prime factorization: The algorithm divides the number by the smallest possible divisor i, starting at 2. If i divides the number, it is added to the list of factors and the number is divided by it. Otherwise i is increased by one. This repeats until the number is reduced to 1.

Greatest common divisor: Both numbers are first broken down into their prime factors. Each prime factor of the first number is matched with an identical, not yet used prime factor of the second number. The GCD is the product of all matched factors. If the numbers have no prime factor in common, the GCD is 1.

Test cases

12 and 18 – GCD 6
72 and 120 – GCD 24
8 and 9 – GCD 1
7 and 28 – GCD 7
2 and 4 – GCD 2

Trial division works well for small numbers but becomes impractical for very large ones. This is exactly what the security of RSA relies on: factoring the product of two large primes is computationally infeasible. In practice, the GCD is therefore computed with the Euclidean algorithm, which does not require factorization.