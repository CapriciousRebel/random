import java.lang.Math;

class Circle {

    private final double PI = 3.14159;
    private double x;
    private double y;
    private double radius;

    public Circle(double cx, double cy, double radius) {
        this.x = cx;
        this.y = cy;
        this.radius = radius;
    }

    public void setCenter(double cx, double cy) {
        this.x = cx;
        this.y = cy;
    }

    public void setRadio(double radius) {
        this.radius = radius;
    }

    public double getPerimeter() {
        return 2 * PI * this.radius;
    }

    public double getArea() {
        return PI * this.radius * this.radius;
    }

    public String toString() {
        return "Class name: Circle \nCenter: (" + this.x + ", " + this.y + ") \nRadius: " + this.radius
                + " \nPerimeter: " + this.getPerimeter() + "\nArea: " + this.getArea();
    }

}

class Triangle {

    private double v1x;
    private double v1y;
    private double v2x;
    private double v2y;
    private double v3x;
    private double v3y;

    public Triangle(double v1x, double v1y, double v2x, double v2y, double v3x, double v3y) {
        this.v1x = v1x;
        this.v2x = v2x;
        this.v3x = v3x;
        this.v1y = v1y;
        this.v2y = v2y;
        this.v3y = v3y;
    }

    public void setVertex(int vertNum, double vertX, double vertY) {
        if (vertNum == 1) {
            this.v1x = vertX;
            this.v1y = vertY;
        }
        if (vertNum == 2) {
            this.v2x = vertX;
            this.v2y = vertY;
        }
        if (vertNum == 3) {
            this.v3x = vertX;
            this.v3y = vertY;
        }
    }

    public static double distance(double x1, double y1, double x2, double y2) {
        return Math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
    }

    public double getPerimeter() {
        double s1 = distance(this.v1x, this.v1y, this.v2x, this.v2y);
        double s2 = distance(this.v2x, this.v2y, this.v3x, this.v3y);
        double s3 = distance(this.v3x, this.v3y, this.v1x, this.v1y);
        return s1 + s2 + s3;
    }

    public double getArea() {
        double Area = (0.5) * (this.v1x * (this.v2y - this.v3y) + this.v2x * (this.v3y - this.v1y)
                + this.v3x * (this.v1y - this.v2y));
        if (Area < 0) {
            return (-1) * Area;
        } else {
            return Area;
        }
    }

    public String toString() {
        return "Class name: Triangle \nVertices: (" + this.v1x + ", " + this.v1y + ") , (" + this.v2x + ", " + this.v2y
                + ") , (" + this.v3x + ", " + this.v3y + ")\nPerimeter(Circumference): " + this.getPerimeter()
                + "\nArea: " + this.getArea();
    }
}

class Rectangle {

    private double x1;
    private double y1;
    private double x2;
    private double y2;

    public Rectangle(double x1, double y1, double x2, double y2) {
        this.x1 = x1;
        this.y1 = y1;
        this.x2 = x2;
        this.y2 = y2;
    }

    public void setCoordinates(double x1, double y1, double x2, double y2) {
        this.x1 = x1;
        this.y1 = y1;
        this.x2 = x2;
        this.y2 = y2;
    }

    public static double distance(double x1, double y1, double x2, double y2) {
        return Math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
    }

    public double getPerimeter() {
        double s1 = this.x2 - this.x1;
        double s2 = this.y1 - this.y2;

        return 2 * s1 + 2 * s2;
    }

    public double getArea() {
        double s1 = this.x2 - this.x1;
        double s2 = this.y1 - this.y2;

        return s1 * s2;
    }

    public String toString() {
        return "Class name: Rectangle \nUpper left vertex: (" + this.x1 + ", " + this.y1 + ") \nLower right vertex: ("
                + this.x2 + ", " + this.y2 + ") \nPerimeter: " + this.getPerimeter() + "\nArea: " + this.getArea();
    }
}

class Main {
    public static void main(String args[]) {

        Circle c = new Circle(0, 0, 1);
        Triangle t = new Triangle(15, 15, 23, 30, 50, 25);
        Rectangle r = new Rectangle(0, 2, 4, 0);

        System.out.println(c.toString());
        System.out.println();

        System.out.println(t.toString());
        System.out.println();

        System.out.println(r.toString());
        System.out.println();

        c.setCenter(1, 1);
        c.setRadio(10);
        System.out.println(c.toString());
        System.out.println();

        t.setVertex(2, 10, 13);
        System.out.println(t.toString());
        System.out.println();

        r.setCoordinates(-10, 20, 10, 0);
        System.out.println(r.toString());
        System.out.println();
    }
}