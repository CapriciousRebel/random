#include <stdio.h>

int generate_checksum(char c, int so_far)
{
    int Ascii = (int)c;
    int checkSum = (Ascii + so_far) % 64;
    return checkSum;
}

char get_string_and_checksum()
{
    while (1)
    {
        return getchar();
    }
}

int main()
{
    char c;
    int so_far;

    printf("Enter a string: ");
    c = get_string_and_checksum();
    if (c == '.')
    {
        return 0;
    }
    else
    {
        so_far = generate_checksum(c, 0);
        while (1)
        {
            c = get_string_and_checksum();
            if (c == '.')
            {
                int checkSum = so_far;
                if (checkSum == 0)
                {
                    return 0;
                }

                so_far = -10;
                printf("checkSum = %d\n", checkSum);
                printf("Enter next string: ");
            }
            else
            {
                so_far = generate_checksum(c, so_far);
            }
        }
    }
    return 0;
}