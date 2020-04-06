#ifndef Bug_H
#define Bug_H

class Bug
{
private:
    int position;
    int dir;

public:
    Bug();
    Bug(int position);
    void move();
    void turn();
    void display();
};

#endif


