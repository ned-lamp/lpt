/*
 * 03 - Fractional Knapsack (Greedy Method)
 *
 * Aim: Write a program to solve a fractional Knapsack problem using a greedy method.
 *
 * Complexity:
 *   Time  : O(n log n) -> sorting takes n log n, the loop after it is only O(n)
 *   Space : O(1)       -> only a few extra variables (sorting is in place)
 *
 * Key terms:
 *   Knapsack            : a bag with a fixed weight capacity W; fill it to get
 *                         maximum total value.
 *   Fractional          : items CAN be broken, so we may take part of an item.
 *   Value/Weight ratio  : value per 1 unit of weight (profit density).
 *   Greedy choice       : always take the item with the highest ratio first.
 *   Why greedy works    : since items can be split, the remaining space is always
 *                         filled with the best ratio -> always optimal.
 *   (In 0/1 knapsack greedy fails -> use Dynamic Programming, see program 04.)
 */

#include <iostream>
#include <algorithm>
using namespace std;

struct Item {
    int value, weight;
};

// Sort by value/weight ratio, highest first
bool cmp(Item a, Item b) {
    return (double)a.value / a.weight > (double)b.value / b.weight;
}

int main() {
    Item items[] = {{60, 10}, {100, 20}, {120, 30}};
    int n = 3, W = 50;

    sort(items, items + n, cmp);

    double total = 0;
    for (int i = 0; i < n; i++) {
        if (items[i].weight <= W) {          // take the whole item
            W -= items[i].weight;
            total += items[i].value;
        } else {                             // take only a part of it
            total += items[i].value * ((double)W / items[i].weight);
            break;
        }
    }

    cout << "Maximum value = " << total << endl;   // 240
    return 0;
}
