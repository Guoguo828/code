A+B with binary search tree Program Usage Instructions

overview: the program is design to complete the project -- construct two BST , finds pairs of nodes whose values sum up to a specific value, and output the preorder traversal

1. Compilation:
    - Please ensure you have a C compiler  on your system like mingw64.
    - Compile the program with tools like vscode or Dev
2. Execution:
    - open the programmer on your code editor
    - Run the compiled program and keep your computer charged
3.Input
    you're required to input in this format:
	the first line: The count of nodes, n1, in the first binary tree.
	In the following m lines: For each node among the n1 nodes, a pair of integers is provided, which denotes the node’s value and the index of its father node.
	Then : The total number of nodes, n2, in the second binary tree.
	In the following n lines: For each node among the n2 nodes, a pair of integers is given, following the same format as the input for the first tree.
	the last line: The target sum value

  Reminder： please guarantee the n1,n2 are less than 200000 and the node's value is less than 2E9 and the sum is  less than 4E9

4. output

The program outputs "true" if it discovers at least one set of nodes, one from each tree, whose values add up to the specified target sum, and then displays these pairs. If no such pairs are identified, it outputs "false".
Following the evaluation of pairs, the program then prints the preorder traversal results for both trees, with each tree's traversal on a separate line.

Example:
input:
8
12 2
16 5
13 4
18 5
15 -1
17 4
14 2
18 3
7
20 -1
16 0
25 0
13 1
18 1
21 2
28 2
36
output:
true
36 = 15 + 21
36 = 16 + 20
36 = 18 + 18
15 13 12 14 17 16 18 18
20 16 13 18 25 21 28

5.Wish you have a good experience
