#include <stdio.h>
#include <string.h>

struct Professor
{
    int ID;
    char firstName[];
};

struct TA
{
    int ID;
    float noOfHours;
    char firstName[];
};

struct Student
{
    int Age;
    int ACT;
    float GPA;
    char firstName[];
};

char get_current_char()
{
    while (1)
    {
        return getchar();
    }
}

int main()
{
    int numberOfTAs;
    int numberOfStudents;

    struct TA listOfTAs[1024];
    struct Student listOfStudents[1024];
    struct Professor prof;

    {

        printf("Please input professor's ID: ");
        scanf("%d", &prof.ID);
        printf("Now, please input professor's first name. Make sure to end with a period. \n");

        int i = 0;
        while (1)
        {
            char c = get_current_char();
            if (c == '.')
            {
                prof.firstName[i] = '\0';
                break;
            }
            else
            {
                prof.firstName[i] = c;
                i++;
            }
        }

        printf("ID of professor is: %d", prof.ID);
        printf("\nFirst Name: %s", prof.firstName);
    }

    {

        printf("\n\nHow many TA's do you have?: ");
        scanf("%d", &numberOfTAs);

        for (int j = 0; j < numberOfTAs; j++)
        {

            printf("\nEnter ID of TA number %d: ", j + 1);
            scanf("%d", &listOfTAs[j].ID);

            printf("Enter number of Hours assigned to TA: ");
            scanf("%f", &listOfTAs[j].noOfHours);

            printf("Input TA's first name. Make sure to end with a period. \n");
            int i = 0;
            while (1)
            {
                char c = get_current_char();
                if (c == '.')
                {
                    listOfTAs[j].firstName[i] = '\0';
                    break;
                }
                else
                {
                    listOfTAs[j].firstName[i] = c;
                    i++;
                }
            }

            printf("\nInfo of TA %d", j + 1);
            printf("\nID: %d", listOfTAs[j].ID);
            printf("\nNo. of hours: %.2f", listOfTAs[j].noOfHours);
            printf("\nFirstName: %s", listOfTAs[j].firstName);
        }
    }

    {

        printf("\n\nHow many student's do you have?: ");
        scanf("%d", &numberOfStudents);

        for (int j = 0; j < numberOfStudents; j++)
        {

            printf("\nEnter age of student number %d: ", j + 1);
            scanf("%d", &listOfStudents[j].Age);

            printf("Enter ACT of student: ");
            scanf("%d", &listOfStudents[j].ACT);

            printf("Enter GPA of student: ");
            scanf("%f", &listOfStudents[j].GPA);

            printf("Input student's first name. Make sure to end with a period. \n");
            int i = 0;
            while (1)
            {
                char c = get_current_char();
                if (c == '.')
                {
                    listOfStudents[j].firstName[i] = '\0';
                    break;
                }
                else
                {
                    listOfStudents[j].firstName[i] = c;
                    i++;
                }
            }

            printf("\nInfo of student %d is:", j + 1);
            printf("\nAge: %d", listOfStudents[j].Age);
            printf("\nACT: %d", listOfStudents[j].ACT);
            printf("\nGPA: %.2f", listOfStudents[j].GPA);
            printf("\nFirstName: %s\n", listOfStudents[j].firstName);
        }
    }

    return 0;
}
