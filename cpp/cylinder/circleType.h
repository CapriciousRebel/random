//circleType.h

#ifndef circleType_H
#define circleType_H

class circleType
{
private:
    double radius;

public:
    void print();
    void setRadius(double r);
    double getRadius();
    double area();
    double circumference();
    circleType(double r = 0);
};

#endif