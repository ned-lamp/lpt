/*
 * 01 - Fibonacci Numbers (Recursive and Non-Recursive)
 *
 * Aim: Write a recursive and non-recursive program to calculate Fibonacci
 *      numbers and analyze their time and space complexity.
 *
 * Fibonacci series: 0 1 1 2 3 5 8 13 ...  ->  F(n) = F(n-1) + F(n-2)
 *
 * Complexity:
 *   Recursive     -> Time O(2^n), Space O(n)
 *   Non-recursive -> Time O(n),   Space O(1)
 *
 * Key terms:
 *   Recursion        : a function calling itself with a smaller input.
 *   Base case        : the condition where recursion stops (n <= 1).
 *   Time complexity  : how the running time grows as input n grows.
 *   Space complexity : how much extra memory the program needs as n grows.
 *   O(2^n)           : each call makes 2 more calls, so work doubles every level
 *                      (same values like fib(3) are calculated again and again).
 *   O(n) space (rec) : calls wait on the stack; deepest chain is n calls.
 *   O(1) space       : only a fixed number of variables (a, b, c).
 *   Memoization      : storing computed values so recursion becomes O(n).
 */

#include <iostream>
using namespace std;

// Recursive
int fibRec(int n) {
    if (n <= 1) return n;                  // base case
    return fibRec(n - 1) + fibRec(n - 2);
}

// Non-recursive (iterative)
int fibIter(int n) {
    if (n == 0) return 0;
    int a = 0, b = 1, c;
    for (int i = 2; i <= n; i++) {
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}

int main() {
    int n;
    cout << "Enter n: ";
    cin >> n;

    cout << "Recursive     : F(" << n << ") = " << fibRec(n) << endl;
    cout << "Non-recursive : F(" << n << ") = " << fibIter(n) << endl;

    return 0;
}
