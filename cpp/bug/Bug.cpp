

#include <iostream>
#include "Bug.hpp"

using namespace std;

Bug::Bug()

{

    position = 0;
    dir = 1;
}

Bug::Bug(int p)

{

    position = p;
    dir = 1;
}

void Bug::move()

{

    position = position + dir;
}

void Bug::turn()

{

    dir = dir * (-1);
}

void Bug::display()

{

    cout << "position = " << position
         << ", direction = " << dir << "\n";
}
