#include <iostream>
#include "cylinderType.h"

using namespace std;

void cylinderType::print()
{
    cout << "Radius = " << radius
         << ", Height = " << height
         << ", Center = (" << x << ", " << y << ") "
         << ", Surface Area = " << surfaceArea()
         << ", Volume = " << volume() << "\n\n";
}

void cylinderType::setRadius(double r)
{
    if (r >= 0)
        radius = r;
    else
        radius = 0;
}

double cylinderType::getRadius()
{
    return radius;
}

void cylinderType::setHeight(double h)
{
    if (h >= 0)
        height = h;
    else
        height = 0;
}

double cylinderType::getHeight()
{
    return height;
}

void cylinderType::setCenter(double a, double b)
{
    x = a;
    y = b;
}

double cylinderType::surfaceArea()
{
    circleType base(radius);
    double base_area = base.area();
    double curved_surface_area = base.circumference() * height;

    return 2 * base_area + curved_surface_area;
}

double cylinderType::volume()
{
    circleType base(radius);
    double volume = base.area() * height;

    return volume;
}

cylinderType::cylinderType(double r, double h, double x, double y)
{
    setRadius(r);
    setHeight(h);
    setCenter(x, y);
}