/*
 * 05 - N-Queens (Backtracking)
 *
 * Aim: Design n-Queens matrix having first Queen placed. Use backtracking to
 *      place remaining Queens to generate the final n-queen's matrix.
 *
 * Complexity:
 *   Time  : O(n!)  -> n choices in first row, fewer in next, ... (n x (n-1) x ...)
 *   Space : O(n^2) -> the n x n board (+ O(n) recursion stack)
 *
 * Key terms:
 *   N-Queens     : place n queens on an n x n board so no two attack each other.
 *   Attack       : a queen attacks along its row, column and both diagonals.
 *   Backtracking : try a choice; if it leads to a dead end, undo it and try the next.
 *   Safe check   : only column + 2 upper diagonals are checked, because we place
 *                  exactly one queen per row (rows can never clash).
 *   Facts        : no solution for n = 2, 3; 4-Queens has 2 solutions; 8-Queens has 92.
 */

#include <iostream>
using namespace std;

int n;
int board[10][10];

// Check column and both upper diagonals of (row, col)
bool isSafe(int row, int col) {
    for (int i = 0; i < row; i++)
        if (board[i][col]) return false;                       // same column
    for (int i = row, j = col; i >= 0 && j >= 0; i--, j--)
        if (board[i][j]) return false;                         // upper-left diagonal
    for (int i = row, j = col; i >= 0 && j < n; i--, j++)
        if (board[i][j]) return false;                         // upper-right diagonal
    return true;
}

bool solve(int row) {
    if (row == n) return true;              // all queens placed
    for (int col = 0; col < n; col++) {
        if (isSafe(row, col)) {
            board[row][col] = 1;            // place queen
            if (solve(row + 1)) return true;
            board[row][col] = 0;            // backtrack (remove queen)
        }
    }
    return false;
}

int main() {
    int firstCol;
    cout << "Enter n: ";
    cin >> n;
    cout << "Enter column for first queen (0 to " << n - 1 << "): ";
    cin >> firstCol;

    board[0][firstCol] = 1;                 // first queen in row 0

    if (solve(1)) {                         // place the rest from row 1
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++)
                cout << (board[i][j] ? "Q " : ". ");
            cout << endl;
        }
    } else {
        cout << "No solution with this first position" << endl;
    }
    return 0;
}
