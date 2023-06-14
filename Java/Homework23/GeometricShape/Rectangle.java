package Homework23.GeometricShape;

import Homework23.GeometricShape.Base.Polygon;
import Homework23.Interface.Perimetr;

public class Rectangle extends Polygon implements Perimetr{
    protected double sideA;
    protected double sideB;


    public Rectangle(double sideA, double sideB){
        this.sideA = sideA;
        this.sideB = sideB;
    }


    @Override
    public double perimetr() {
        return 2 * sideA + 2 * sideB;
    }

    
    @Override
    public double area() {
        return sideA * sideB;
    }

    @Override
    public String toString() {
        return "Длины сторон равны а = " + sideA + ", b = " + sideB;
    }

    public void setSideA(double sideA) {
        this.sideA = sideA;
    }

    public void setSideB(double sideB) {
        this.sideB = sideB;
    }
}
    
