/*
 * 02 - Huffman Encoding (Greedy Strategy)
 *
 * Aim: Write a program to implement Huffman Encoding using a greedy strategy.
 *
 * Complexity:
 *   Time  : O(n log n)  -> about n push/pop operations on a heap, each costs log n
 *   Space : O(n)        -> the tree and heap hold about 2n nodes
 *
 * Key terms:
 *   Greedy strategy : pick the best choice at each step (here: the 2 lowest
 *                     frequencies) hoping it leads to the best overall answer.
 *   Min-heap        : structure that always gives the smallest element first
 *                     (priority_queue with a custom compare).
 *   Huffman tree    : binary tree; left edge = 0, right edge = 1.
 *   Prefix code     : no code is the start of another code, so decoding is
 *                     never confusing.
 *   Result          : frequent characters get short codes -> data compression
 *                     (used in ZIP, JPEG).
 */

#include <iostream>
#include <queue>
using namespace std;

struct Node {
    char ch;
    int freq;
    Node *left, *right;
    Node(char c, int f) { ch = c; freq = f; left = right = NULL; }
};

// Keeps the node with the smallest freq on top
struct compare {
    bool operator()(Node* a, Node* b) { return a->freq > b->freq; }
};

void printCodes(Node* root, string code) {
    if (!root) return;
    if (!root->left && !root->right)          // leaf node
        cout << root->ch << " : " << code << endl;
    printCodes(root->left, code + "0");
    printCodes(root->right, code + "1");
}

int main() {
    char ch[] = {'a', 'b', 'c', 'd', 'e', 'f'};
    int freq[] = {5, 9, 12, 13, 16, 45};
    int n = 6;

    priority_queue<Node*, vector<Node*>, compare> pq;
    for (int i = 0; i < n; i++)
        pq.push(new Node(ch[i], freq[i]));

    // Greedy: always join the two smallest
    while (pq.size() > 1) {
        Node* l = pq.top(); pq.pop();
        Node* r = pq.top(); pq.pop();
        Node* parent = new Node('$', l->freq + r->freq);
        parent->left = l;
        parent->right = r;
        pq.push(parent);
    }

    cout << "Huffman Codes:" << endl;
    printCodes(pq.top(), "");
    return 0;
}
