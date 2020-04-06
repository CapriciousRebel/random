#include <iostream>
#include "cylinderType.h"

using namespace std;

int main()
{
    cylinderType cylinder1(10, 10, 0, 0);
    cylinder1.print();

    cylinder1.setCenter(1, 1);
    cylinder1.print();

    cylinder1.setHeight(20);
    cylinder1.print();

    cylinder1.setRadius(20);
    cylinder1.print();

    double surfaceArea = cylinder1.surfaceArea();
    double volume = cylinder1.volume();
    cout << "surface Area = " << surfaceArea << ", Volume = " << volume << endl;
}


