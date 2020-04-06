

#include <iostream>
#include "Bug.hpp"

using namespace std;

int main()
{

    Bug bug(10);
    bug.display();
    
    bug.move();
    bug.display();
    
    bug.turn();
    bug.display();

    bug.move();
    bug.display();
}
