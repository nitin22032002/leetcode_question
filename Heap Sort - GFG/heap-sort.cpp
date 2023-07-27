//{ Driver Code Starts
// C++ program for implementation of Heap Sort
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// The functions should be written in a way that array become sorted 
// in increasing order when heapSort() is called.

class Solution {
private:
    // Helper function to maintain heap property.
    void heapify(int arr[], int n, int i) {
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        if (left < n && right < n) {
            int m = min(arr[left], min(arr[right], arr[i]));
            if (m == arr[left]) {
                swap(arr[left], arr[i]);
                heapify(arr, n, left);
            } else if (m == arr[right]) {
                swap(arr[right], arr[i]);
                heapify(arr, n, right);
            } else {
                return;
            }
        } else if (left < n) {
            if (arr[i] > arr[left]) {
                swap(arr[left], arr[i]);
                heapify(arr, n, left);
            }
        } else if (right < n) {
            if (arr[i] > arr[right]) {
                swap(arr[right], arr[i]);
                heapify(arr, n, right);
            }
        }
    }

    // Helper function to maintain heap property while building the heap.
    void get(int arr[], int n, int i) {
        if (i == 0) {
            return;
        }
        int par = (i - 1) / 2;
        if (arr[i] >= arr[par]) {
            return;
        } else {
            swap(arr[i], arr[par]);
            get(arr, n, par);
        }
    }

public:
    // Function to build a Heap from an array.
    void buildHeap(int arr[], int n) {
        for (int i = 1; i < n; i++) {
            get(arr, n, i);
        }
    }

    // Function to sort an array using Heap Sort.
    void heapSort(int arr[], int n) {
        buildHeap(arr, n);
        for (int i = n - 1; i > 0; i--) {
            swap(arr[i], arr[0]);
            heapify(arr, i, 0);
        }
        reverse(arr, arr+n);
    }
};





//{ Driver Code Starts.

/* Function to print an array */
void printArray(int arr[], int size)
{
    int i;
    for (i=0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

// Driver program to test above functions
int main()
{
    int arr[1000000],n,T,i;
    scanf("%d",&T);
    while(T--){
    scanf("%d",&n);
    for(i=0;i<n;i++)
      scanf("%d",&arr[i]);
    Solution ob;
    ob.heapSort(arr, n);
    printArray(arr, n);
    }
    return 0;
}

// } Driver Code Ends