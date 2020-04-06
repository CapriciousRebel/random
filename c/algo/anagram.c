#include <stdlib.h>
#include <stdio.h>

// (Helper function)
// First implement the 'merge sort' algorithm to sort integer arrays

// (No explanation is needed for merge sort algorithm
// as that is irrelavant to this question)
void merge(int arr[], int l, int m, int r)
{
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;

    int L[n1], R[n2];
    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];

    i = 0;
    j = 0;
    k = l;
    while (i < n1 && j < n2)
    {
        if (L[i] <= R[j])
        {
            arr[k] = L[i];
            i++;
        }
        else
        {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1)
    {
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j < n2)
    {
        arr[k] = R[j];
        j++;
        k++;
    }
}

// (Helper function)
// sorts the integer array arr[]
void mergeSort(int arr[], int l, int r)
{
    if (l < r)
    {
        int m = l + (r - l) / 2;
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}

// (Helper function)
// compares two arrays to check if they are the same
int compareArrays(int A[], int B[], int n)
{
    // loop through the
    for (int i = 0; i < n; i++)
    {
        if (A[i] != B[i])
        {
            return 0;
        }
    }
    return 1;
}

// (Helper function)
// returns a single character read from keyboard input
char get_current_char()
{
    while (1)
    {
        return getchar();
    }
}

// (Helper function)
// used to filter the string to filter out other characters
int verify(char c)
{
    // include the numbers from 0 to 9 including 0 and 9
    if (c >= 48 && c <= 57)
    {
        return 1;
    }

    // include the Capital letters
    else if (c >= 65 && c <= 90)
    {
        return 1;
    }
    // include the non-capital letters
    else if (c >= 97 && c <= 122)
    {
        return 1;
    }
    // return 0 for all other cases
    else
    {
        return 0;
    }
}

// (Helper function)
// converts the non-capital letters to capital letters
// used to implement cas-insensitivity
int convertToCapital(int c)
{
    // check if the letter is non-capital
    if (c >= 97 && c <= 122)
    {
        // return its capital counterpart
        return c - 32;
    }
    else
    {
        // otherwise return the same letter
        return c;
    }
}

// (Driver code)
int main()
{

    int i = 0;               // counter
    int l1 = 0;              // length of first string
    int l2 = 0;              // length of second string
    int j = 0;               // second counter
    char string1[1024];      // first string
    char string2[1024];      // second string
    int line1filtered[1024]; // filtered first string
    int line2filtered[1024]; // filtered second string

    /* Take user input */
    // take the first string from user
    printf("Enter line: ");
    while (1)
    {

        char c = get_current_char();
        
        if (c == '\n')
        {
            // when a newline(\n) is encountered, null terminate the string and break the loop
            string1[i] = '\0';
            break;
        }
        else
        {
            // add to the string, each character from key board input,
            // until \n(newline) is encountered when user presses enter
            string1[i] = c;
            i++;
        }
    }
    l1 = i; // set the length of first string
    i = 0;  // reset the counter

    // take the second string from user (same logic as above)
    printf("Enter anagram: ");
    while (1)
    {
        char c = get_current_char();
        if (c == '\n')
        {
            string2[i] = '\0';
            break;
        }
        else
        {
            string2[i] = c;
            i++;
        }
    }
    l2 = i; // set the length of second string

    /* Filter the strings */
    // filter the first string

    for (i = 0; i < l1; i++)
    {
        // verify each character in the 
        if (verify(string1[i]))
        {
            int temp = (int)string1[i];
            temp = convertToCapital(temp);
            line1filtered[j] = temp;

            j++;
        }
    }
    line1filtered[j] = '\0'; // null terminate the first filtered string
    l1 = j;                  // set the length of first filtered string
    j = 0;                   // reset the second counter

    // filter the second string
    for (i = 0; i < l2; i++)
    {
        if (verify(string2[i]))
        {
            int temp = (int)string2[i];
            temp = convertToCapital(temp);
            line2filtered[j] = temp;

            j++;
        }
    }
    line2filtered[j] = '\0'; // null terminate the second filtered string
    l2 = j;                  // set the length of second filtered string

    if (l1 != l2)
    {
        // if the arrays are of unequal length, then it is not an anagram
        printf("Not an anagram\n");
        return 0;
    }

    // use merge-sort to sort both the arrays in ascending order
    mergeSort(line1filtered, 0, l1 - 1);
    mergeSort(line2filtered, 0, l2 - 1);

    // compare the sorted arrays
    printf("\n");
    if (compareArrays(line1filtered, line2filtered, l1))
    {
        // if they are both same, then it is an anagram
        printf("Anagram!\n");
    }
    else
    {
        // otherwise it is not an anagram
        printf("Not an anagram\n");
    }
    return 0;
}