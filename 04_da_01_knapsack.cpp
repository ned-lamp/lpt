/*
 * 04 - 0/1 Knapsack (Dynamic Programming)
 *
 * Aim: Write a program to solve a 0-1 Knapsack problem using dynamic programming
 *      or branch and bound strategy.
 *
 * Formula:
 *   dp[i][w] = max( val[i] + dp[i-1][w - wt[i]],  dp[i-1][w] )   if wt[i] <= w
 *   dp[i][w] = dp[i-1][w]                                         otherwise
 *
 * Complexity:
 *   Time  : O(n x W) -> fills a table of n rows and W columns
 *   Space : O(n x W) -> size of the table
 *   (n = number of items, W = capacity)
 *
 * Key terms:
 *   0/1                     : take an item fully (1) or not at all (0), no fractions.
 *   Dynamic Programming     : break the problem into smaller subproblems, solve
 *                             each once and store the answer in a table.
 *   Overlapping subproblems : the same smaller problems come up again and again.
 *   Optimal substructure    : best answer is built from best answers of smaller parts.
 *   Why not greedy          : greedy picks items 1+2 = 160, real best is 2+3 = 220.
 */

#include <iostream>
using namespace std;

int main() {
    int val[] = {60, 100, 120};
    int wt[]  = {10, 20, 30};
    int n = 3, W = 50;

    int dp[4][51];   // dp[i][w] = best value using first i items with capacity w

    for (int i = 0; i <= n; i++) {
        for (int w = 0; w <= W; w++) {
            if (i == 0 || w == 0)
                dp[i][w] = 0;
            else if (wt[i-1] <= w)
                dp[i][w] = max(val[i-1] + dp[i-1][w - wt[i-1]],   // take it
                               dp[i-1][w]);                       // leave it
            else
                dp[i][w] = dp[i-1][w];                            // too heavy
        }
    }

    cout << "Maximum value = " << dp[n][W] << endl;   // 220
    return 0;
}
