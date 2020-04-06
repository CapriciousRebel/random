#include <iostream>

int main()
{
    int j, k;

    for (j = 0; j < 3; j++)
    {
        for (k = 0; k < 4; k++)
        {
            if (k == 0 || k == 3 || j == 0 || j == 2)
                printf("*");
            else
                printf(" ");
        }
        printf("\n");
    }

    return 0;
}


