/**
 * Title: Project 2
 * overall idea:In fact,the problem can be divided into three small problems.
 * 1 Construct two binary search trees
 * 2 perform the inorder traversal and match the two arrays 
 * 3 perform the preorder traversal
 */

#include <stdio.h>  // Standard input and output library
#include <stdlib.h>

#define SIZE 200005 //  maximum size of the nodes of a tree
typedef struct node* binarytree;

typedef struct node{
    int data;       // Value stored in the node
    int left;       // Index of the left child node
    int right;      // Index of the right child node
}Node;

int flag1=1;        // Global flag to control " " in preorder traversal output
int ft[SIZE],ffa[SIZE],st[SIZE],sfa[SIZE]; // Arrays for storing tree data and parent index
//ft means first tree,ffa means first father(the father of the node in first tree) ,st means second tree,sfa means second father  

/**
 * Problem 1 :Creates a binary search tree.
 * @param n Number of nodes in the tree.
 * @param data Array of node values.
 * @param fa Array of parent node index.
 * @return Pointer to the created binary tree(an array).
 */
/*
    Here I would like to explain why I use an array to represent the tree instead of the common linked list version.abort
    The reason is that the input is given the index of the parent node.If I still use the linked list,I need to search the parent node
    when I want to connect the child node to its parent.abort
    So I utilize the array,which enable me to use the index to find the parent directly.
    In short,using the array can simplify the code and improve the efficiency.
*/
binarytree create(int n,int *data,int *fa){
    binarytree tree=(binarytree)malloc(sizeof(struct node)*n); // Allocate memory for the tree
    for(int i=0; i<n; i++){
        tree[i].data = data[i];   // Assign node value
        tree[i].left = -1;        // Initialize left child index as -1 (no child)
        tree[i].right = -1;       // Initialize right child index as -1 (no child)
    }
    for(int i=0;i<n;i++){
        if(fa[i]==-1) continue;   // Skip if the node has no parent (root node)
        else {
            if(tree[i].data<tree[fa[i]].data) 
                tree[fa[i]].left=i; // Set current node as left child if its data is smaller than parent
            else 
                tree[fa[i]].right=i; // Otherwise, set as right child
        }
    }
    return tree; // Return the constructed tree
} 

/**
 * Problem 2.1 :Performs inorder traversal on the first binary tree and stores the result in an array.
 * @param tree Pointer to the binary tree.
 * @param root Root node index.
 * @param array Array to store the inorder traversal result.
 */
/*
    the result of inorder traversal is a sorted array.It is helpful for the next step--match.
    if not sorted,we need to use hash map,but it is more complex.
 */
void inorder_tree1(binarytree tree,int root,int *array){
    static int sizet1=0; // Static variable to track the current position in the array,otherwise the size will be reset
    if(root==-1) return; // Base case: If the node is null, return
    inorder_tree1(tree,tree[root].left,array); // Traverse the left subtree
    array[sizet1++]=tree[root].data; // Store the current node's data in the array
    inorder_tree1(tree,tree[root].right,array); // Traverse the right subtree
}

/**
 * Performs inorder traversal on the second binary tree and stores the result in an array.
 * @param tree Pointer to the binary tree.
 * @param root Root node index.
 * @param array Array to store the inorder traversal result.
 */
void inorder_tree2(binarytree tree,int root,int *array){
    static int sizet2=0; // Static variable to track the current position in the array
    if(root==-1) return; // Base case: If the node is null, return
    inorder_tree2(tree,tree[root].left,array); // Traverse the left subtree
    array[sizet2++]=tree[root].data; // Store the current node's data in the array
    inorder_tree2(tree,tree[root].right,array); // Traverse the right subtree
}

/**
 * Problem 3:Performs preorder traversal on the binary tree and prints the result.
 * @param tree Pointer to the binary tree.
 * @param root Root node index.
 */
void preorder_tree(binarytree tree, int root){
    if(root == -1) return; // Base case: If the node is null, return
    if(flag1==0) printf(" "); // Print a space before each node except the first one
    if(flag1==1){
        flag1=0; // Reset the flag after printing the first node
    }
    printf("%d", tree[root].data); // Print the data of the current node
    preorder_tree(tree, tree[root].left); // Recursively traverse the left subtree
    preorder_tree(tree, tree[root].right); // Recursively traverse the right subtree
}

/**
 * Problem 2.2:Checks if there are pairs in the two arrays whose sum equals the given value.
 * @param size1 Size of the first array.
 * @param size2 Size of the second array.
 * @param array1 First array.
 * @param array2 Second array.
 * @param sum Target sum value.
 */
/*
  the method to find the pairs is similar to the two sum problem.(project1 hard)
  Here I use the two pointer approach , which time complexity is O(n).
*/
void match(int size1,int size2,int *array1,int *array2,int sum){
    int left=0,right=size2-1; // Initialize two pointers for the two arrays,start from the first array's left and second array's right
    int flag=0; // Flag to record if a valid pair is found
    while(left<=size1-1&&right>=0){ // Loop until pointers reach the boundary of the arrays
        int sum1=array1[left]+array2[right]; // Calculate the sum of the current pair
        if(sum1==sum){ // If the sum matches the target
            if(flag==0){
                flag=1; // Set the flag to indicate a match is found
                printf("true\n"); // Print "true" only once
            }
            printf("%d = %d + %d\n", sum, array1[left], array2[right]); // Print the matching pair
            while(array1[left]==array1[left+1])left++; // Skip the same values in array1
            while(array2[right-1]==array2[right])right--; // Skip same values in array2
            left++; // Move the left pointer forward
            right--; // Move the right pointer backward
        }
        else if(sum1<sum) left++; // If the sum is less than the target, move the left pointer forward
        else right--; // If the sum is greater than the target, move the right pointer backward
    }
    if(flag==0) printf("false\n"); // If no match is found, print "false"
}

int main(){
    int size1,size2,sum,root1,root2; // Variables for sizes, sum, and root index
    scanf("%d",&size1); //  the size of the first tree
    for(int i=0;i<size1;i++){
        scanf("%d %d",&ft[i],&ffa[i]); //  node data and parent index for the first tree
        if(ffa[i]==-1) root1=i; // find out the root node of the first tree
    }
    scanf("%d",&size2); //  the size of the second tree
    for(int i=0;i<size2;i++){
        scanf("%d %d",&st[i],&sfa[i]); //  node data and parent index for the second tree
        if(sfa[i]==-1) root2=i; // find out the root node of the second tree
    }

    binarytree Tree1 =create(size1,ft,ffa); // Create the first binary tree
    binarytree Tree2 =create(size2,st,sfa); // Create the second binary tree
    scanf("%d",&sum); //  the target sum value
    int *array1=(int*)malloc(sizeof(int)*size1); // create first array
    int *array2=(int*)malloc(sizeof(int)*size2); // create second array
    inorder_tree1(Tree1,root1,array1); // Perform inorder traversal on the first tree
    inorder_tree2(Tree2,root2,array2); // Perform inorder traversal on the second tree
    //printf("%d\n",array1[0]); // test(ignore it)
    match(size1,size2,array1,array2,sum); // find pairs matching the target sum
    preorder_tree(Tree1,root1); // Perform preorder traversal on the first tree
    printf("\n"); 
    flag1=1; // Reset the flag for preorder traversal
    preorder_tree(Tree2,root2); // Perform preorder traversal on the second tree
    return 0; // End of program
}