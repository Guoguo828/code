#include <stdio.h>  // Standard input and output library
#include <time.h>   // Time library for timing functions

clock_t begin, stop; // Variables to record time
double duration;     // Variable to calculate duration

// Iterative binary search function
int iterativeBinary(int *array, int start, int end, int target) {
    while (start <= end) { // Loop until start exceeds end
        int mid = (start + end) / 2; // Find the middle index
        if (target == array[mid]) {
            return mid; // Target found, return index
        } else if (target > array[mid]) {
            start = mid + 1; // Search in the right half
        } else {
            end = mid - 1;   // Search in the left half
        }
    }
    return -1; // Target not found
}

// Recursive binary search function
int recursiveBinary(int *array, int start, int end, int target) {
    if (start <= end) { // Base case
        int mid = (start + end) / 2; // Find the middle index
        if (target == array[mid]) {
            return mid; // Target found, return index
        } else if (target > array[mid]) {
            return recursiveBinary(array, mid + 1, end, target); // Search in the right half
        } else {
            return recursiveBinary(array, start, mid - 1, target); // Search in the left half
        }
    }
    return -1; // Target not found
}

// Iterative sequential search function
int iterativeSequential(int *array, int size, int target) {
    for (int i = 0; i < size; i++) { // Loop through the array
        if (array[i] == target) {
            return i; // Target found, return index
        }
    }
    return -1; // Target not found
}

// Recursive sequential search function
int recursiveSequential(int *array, int start, int end, int target) {
    if (start <= end) { // Base case
        if (array[start] == target) {
            return start; // Target found, return index
        } else {
            return recursiveSequential(array, start + 1, end, target); // Search the rest of the array
        }
    }
    return -1; // Target not found
}

int main() {
    int s;
    printf("Enter the size of the array: ");
    scanf("%d", &s); // Input array size

    int array[s], result; // Array and result variable
    for (int i = 0; i < s; i++) {
        array[i] = i; // Fill array with values 0 to s-1
    }

    // Here I would like to explain why I choose the array as 0 to s-1:
    // the project is to compare the time of different search algorithms for an ordered list,
    // so the time complexity has nothing to do with what the ordered list is.
    // So I choose the simplest ordered list to make the time complexity more obvious, and the code more concise.
   
    // To avoid the influence of different target numbers, here I choose the target number as s,
    // so all the search algorithms will return -1, and the time will be the worst.

    // Measure time for iterative binary search
    begin = clock(); // Start timing
    for (int i = 0; i < 1000000; i++) { // Repeat for better accuracy
        result = iterativeBinary(array, 0, s - 1, s); // Perform search
    }
    stop = clock(); // Stop timing
    duration = ((double)(stop - begin)) / CLOCKS_PER_SEC; // Calculate duration
    printf("Ticks and Time for iterative binary search: %lf ticks and 1%lf seconds\n", (double)(stop - begin), duration);

    // Measure time for recursive binary search
    begin = clock(); 
    for (int i = 0; i < 1000000; i++) { // Repeat for better accuracy
        result = recursiveBinary(array, 0, s - 1, s); // Perform search
    }
    stop = clock(); 
    duration = ((double)(stop - begin)) / CLOCKS_PER_SEC; // Calculate duration
    printf("Ticks and Time for recursive binary search: %lf ticks and %lf seconds\n", (double)(stop - begin), duration);

    // Measure time for iterative sequential search
    begin = clock(); 
    for (int i = 0; i < 10000; i++) { // Repeat for better accuracy
        result = iterativeSequential(array, s, s); // Perform search
    }
    stop = clock(); 
    duration = ((double)(stop - begin)) / CLOCKS_PER_SEC; // Calculate duration
    printf("Ticks and Time for iterative sequential search: %lf ticks and %lf seconds\n", (double)(stop - begin), duration);

    // Measure time for recursive sequential search
    begin = clock();
    for (int i = 0; i < 1000; i++) { // Repeat for better accuracy
        result = recursiveSequential(array, 0, s - 1, s); // Perform search
    }
    stop = clock();
    duration = ((double)(stop - begin)) / CLOCKS_PER_SEC; // Calculate duration
    printf("Ticks and Time for recursive sequential search: %lf ticks and %lf seconds\n", (double)(stop - begin), duration);

    return 0;
}