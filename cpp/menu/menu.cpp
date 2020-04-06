#include <iostream> // we include iostream header file for handling the user input/output operations
#include <fstream>  // we include the fstream header file for loading the data from the text file.
#include <string>   // we include the string header file since we use string objects

using namespace std;

struct menuItemType
{
    string menuItem;
    double menuPrice;
};

menuItemType menuList[8]; // we declare menuList as a global array

void getData()
// the getData loads the data from Ch9_Ex4Data.txt file to the menuList array
{
    // declare and open the text file containing the data, make sure to place the "Ch9_Ex4Data.txt" file in same directory as this cpp file.
    ifstream textfile;
    textfile.open("menu.txt");

    // textfile.is_open() function returns true
    if (textfile.is_open())
    {
        int lineNumber = 0; // int lineNumber is used to keep a track of which line is currently being pointed at
        string line;        // string line is the line as a string, which is currently being pointed at

        while (getline(textfile, line)) //  getline() returns true, until the end of file line is reached
        {                               // hence we use it to run a while loop which loops over all the lines in the data file
            if (lineNumber % 2 == 0)
            { // when we are on even lineNumber, it is the name of the menuItem
                // This is the logic to properly format the name of menuItem, so that it is left-justifed

                int length = line.length();  // get the length of the name of menuItem
                int addSpaces = 15 - length; // subtract the length from 15, and add that many spaces to the name
                for (int i = 0; i < addSpaces; i++)
                {
                    line = line + " ";
                }

                menuList[lineNumber / 2].menuItem = line; // add the name of menuItem to the global array menulist
            }
            else
            {
                // when we are on odd lineNumber, it is the price of the menuItem since the line is a string, we use the stof() function to convert it to float.
                float price = stof(line);
                menuList[(lineNumber - 1) / 2].menuPrice = price; // add the price which is now a float to the global array menulist
            }
            lineNumber++; // at the end of each iteration, increment the lineNumber, to access the next line in the data file
        }
        textfile.close(); // always remember to close any file that was opened
    }
}

void printCheck(int itemIDs[8], int numberOfItems)
{
    // to understand the logic for this function, kindly first read the showMenu() function
    cout << "Welcome to Johnny's Restaurant\n";
    float tax = 0, totalprice = 0; // we initialize the tax, and totalprice

    for (int k = 0; k < numberOfItems; k++)
    {
        // we run the loop for as many times as there are number of items in the order, so that we can process each item in the order
        int itemID = itemIDs[k] - 1;
        // we subtract 1 from the itemIDs[k] since the array is indexed, starting from 0, but the user entered item ID staring from 1
        float price = menuList[itemID].menuPrice; // price of the current item

        tax += (price) * (0.05); // tax is 5% of the price of each item, we add it to the tax variable for each iteration
        totalprice += price;     // the price of each item is added the the total-price

        // again, printf is used to display the items ordered in a proper format
        printf("%s $%.2f", menuList[itemID].menuItem.c_str(), price);
        printf("\n");
    }
    // finally, we print the tax, and total amount dueƒ
    printf("Tax:            $%.2f\n", tax);
    printf("Amount Due:     $%.2f", tax + totalprice); // total amount due is the sum of totalproce and the tax
}

void showMenu()
{
    cout << "Welcome to Johnny's Restaurant\n----Today's Menu----\n";

    for (int i = 0; i < 8; i++) // run  a for-loop for 8 iterations, because that is how many items we have on the menu
    {
        // using the printf, we print the formatted menu onto the terminal
        // its important to use the c_str() function to convert the c++ string to C- style string,
        // since the %s expects that as an argument.
        // Also, use "%.2f" to print the float upto two decimal places
        printf("%d: %s $%.2f", i + 1, menuList[i].menuItem.c_str(), menuList[i].menuPrice);
        printf("\n");
    }

    printf("You can make up to 8 single order selections\n");
    char input; // A variable to store the user input and process it later
    printf("Do you want to make selection Y/y (Yes), N/n (No): ");
    cin >> input;

    int numberOfItems = 0; // a variable that tracks the number of items ordered by the user
    int itemIDs[8];        // we will store all the item numbers chosen by the user in this array
                           // this array will be passed as an argument while printing the check
    while (input == 'Y' || input == 'y')
    { // the while loop runs only when the input is 'Y' or 'y'
        printf("Enter item number: ");
        cin >> itemIDs[numberOfItems];
        numberOfItems++;

        printf("Select another item Y/y (Yes), N/n (No): ");
        cin >> input; // on each iteration, we update the input, and the loop is terminated when input is not 'Y' or 'y'
    }
    // call the printCheck function and pass it the array of item ids, and also the number of items ordered.
    printCheck(itemIDs, numberOfItems);
}

int main()
{
    // we call the getData and showMenu functions to run the program.
    getData();
    // it is important to call the getData function before showMenu, so that the data first gets loaded in the menuList
    // before we display it
    showMenu();
    return 0;
}