#include <stdio.h>
#include <math.h>

long double logOnePlus(long double x0, int N)
{
    long double answer = 0;
    for (int i = 1; i <= N; i++)
    {
        answer = answer + (pow(-1, i + 1) * pow(x0, i)) / i;
    }
    return answer;
}

long double error_value(long double myLog, long double Clog)
{
    long double error_value = myLog - Clog;
    if (error_value > 0)
    {
        return error_value;
    }
    else
    {
        return error_value * (-1);
    }
}

int main()
{
    // using long double datatype for extra precision
    long double x0;
    int N;

    // input the variables from the user
    printf("Enter the value of x0: ");
    scanf("%Lf", &x0);
    printf("Enter the value of N: ");
    scanf("%d", &N);

    long double Clog = log(1 + x0);
    // calculate the value of log(1+x0) using built-in function
    long double myLog = logOnePlus(x0, 100);
    // calculate the value of log(1+x0) using taylor-series approximation
    long double E = error_value(myLog, Clog);
    // calculate the error value

    // print the required values on the screen
    printf("\nThe value of x0: %.Lf", x0);
    printf("\nThe value of log(1+x0), calculated by built-in function: %.19Lf", Clog);
    printf("\nThe value of log(1+x0), calculated by approximation: %.19Lf", myLog);
    printf("\nThe number of elements used in approximation: %d", N);
    printf("\nThe value of error factor is: %Le", E);

    return 0;
}
