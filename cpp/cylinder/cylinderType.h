#ifndef cylinderType_H
#define cylinderType_H
#include "circleType.h"

class cylinderType : public circleType
{
private:
    double height, radius, x, y;

public:
    void print();

    void setRadius(double r);
    double getRadius();

    void setHeight(double h);
    double getHeight();

    void setCenter(double a, double b);

    double surfaceArea();
    double volume();

    cylinderType(double x = 0, double y = 0, double r = 0, double h = 0);
};

#endif


