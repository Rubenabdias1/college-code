#include <iostream>
#include <bits/stdc++.h>

// Ruben Nunez
// CS 365 - Program Language Systems
// Assignment 1

using namespace std;

void print(int arr[], int n) {
    for (int i = 0; i < n; ++i) {
        if (arr[i] < 10) {
            cout << " " << arr[i] << " ";
        }
        else {
            cout << arr[i] << " ";
        }

        if ((i + 1) % 10 == 0) {
            cout << "\n";
        }
    }
}

double average ( int arr[], int sum, int n){
    return (double)sum / (double)n;
}

// Function for calculating median
double median(int arr[], int n)
{
    // https://www.geeksforgeeks.org/median/
    // First we sort the array
    sort(arr, arr + n);
 
    // check for even case
    if (n % 2 != 0)
        return (double)arr[n / 2];
 
    return (double)(arr[(n - 1) / 2] + arr[n / 2]) / 2.0;
}

int mode(int a[], int n)
{
    // https://www.geeksforgeeks.org/mode/
    // The output array b[] will
    // have sorted array
    int b[n];
 
    // variable to store max of
    // input array which will
    // to have size of count array
    int max = *max_element(a, a + n);
 
    // auxiliary(count) array to
    // store count. Initialize
    // count array as 0. Size
    // of count array will be
    // equal to (max + 1).
    int t = max + 1;
    int count[t];
    for (int i = 0; i < t; i++)
        count[i] = 0;
 
    // Store count of each element
    // of input array
    for (int i = 0; i < n; i++)
        count[a[i]]++;
 
    // mode is the index with maximum count
    int mode = 0;
    int k = count[0];
    for (int i = 1; i < t; i++) {
        if (count[i] > k) {
            k = count[i];
            mode = i;
        }
    }
 
    return mode;
}
 
 // Function for calculating variance
int variance(int a[], int n)
{
    // https://www.geeksforgeeks.org/program-for-variance-and-standard-deviation-of-an-array/
    // Compute mean (average of elements)
    int sum = 0;
    for (int i = 0; i < n; i++)
        sum += a[i];
    double mean = (double)sum /
                  (double)n;
 
    // Compute sum squared
    // differences with mean.
    double sqDiff = 0;
    for (int i = 0; i < n; i++)
        sqDiff += (a[i] - mean) *
                  (a[i] - mean);
    return sqDiff / n;
}
 
double standardDeviation(int arr[], int n)
{
    return sqrt(variance(arr, n));
}

int main()
{
    int randomNumberArray[80];    
    int n = sizeof(randomNumberArray) / sizeof(randomNumberArray[0]);

    long sum = 0;
    unsigned long long product = 1;

    for (int i=0; i<80; i++)
        randomNumberArray[i] = rand()%85 + 1;

    cout << " Unsorted Number List\n";
    print(randomNumberArray, n);
    
    sort(randomNumberArray, randomNumberArray + n);

    cout << "\n Sorted Number List\n";
    print(randomNumberArray, n);

    cout << "\n\nThe smallest numbers is:  " << randomNumberArray[0] << endl; 
    cout << "The largest numbers is:  " << randomNumberArray[n - 1] << endl;

    for (int i=0; i < n; i++)
        sum += randomNumberArray[i];
    cout << "The sum of numbers is: " << sum << endl; 

    for (int i=0; i < n; i++)
        product *= randomNumberArray[i];
    cout << "\nThe product of the numbers is: " << product << endl; 

    cout << "\nThe mean of the numbers is: " << average(randomNumberArray, sum, n) << endl; 
    cout << "The median of the numbers is: " << median(randomNumberArray, n) << endl; 
    cout << "The mode of the numbers is: " << mode(randomNumberArray, n) << endl;
    cout << "The Standard Deviation of the numbers is: " << standardDeviation(randomNumberArray, n) << endl;  


    return 0;
}
