#include <stdio.h>

int COLUMNS = 0;
int ROWS = 0;

void getrows(){
    int rows;
    printf("Enter the number of rows: ");
    scanf("%d", &rows);
    ROWS = rows;
}

void getcolumns(){
    int columns;
    printf("Enter the number of columns: ");
    scanf("%d", &columns);
    COLUMNS = columns;
}

void printmaxOfArray2D(int (*array)[COLUMNS])
{
    int max = array[0][0];
    int max_col = 0;
    int max_row = 0;

    for (int i = 0; i < ROWS; i++)
    {
        for (int j = 0; j < COLUMNS; j++)
        {
            if (array[i][j] > max)
            {
                max = array[i][j];
                max_col = j;
                max_row = i;
            }
        }
    }
    printf("maximum value = %d , row number = %d, column number = %d", max, max_row + 1, max_col + 1);
}

int main()
{
    getrows();
    getcolumns();

    int numbers[ROWS][COLUMNS];

    int i, j;
    for (i = 0; i < ROWS; i++)
    {
        for (j = 0; j < COLUMNS; j++)
        {
            printf("Enter value for number at [%d],[%d]:", i, j);
            scanf("%d", &numbers[i][j]);
        }
    }

    printmaxOfArray2D(numbers);

    return 0;
}