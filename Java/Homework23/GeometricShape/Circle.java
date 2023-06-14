package Homework23.GeometricShape;

import Homework23.GeometricShape.Base.ClosedLine;
import Homework23.Interface.Circumference;

public class Circle extends ClosedLine implements Circumference{
    protected double radius;

    public Circle (double radius) throws Exception{
        this.radius = radius;
        if (radius <= 0){
            throw new Exception(String.format("Кург с радиусом %f не может существовать", radius));
        }
    }

    @Override
    public double area() {
        return Math.PI * radius * radius;
    }

    @Override
    public double circumference() {
        return 2* Math.PI * this.radius;
    }

    @Override
    public String toString() {
        return "Радиус круга = " + radius;
    }

    public void setRadius(double radius) {
        this.radius = radius;
    }
}
