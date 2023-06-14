package Homework23.GeometricShape;


import Homework23.GeometricShape.Base.Polygon;
import Homework23.Interface.Perimetr;

public class Triangle extends Polygon implements Perimetr {
    private double[] sides;

    public Triangle(double[] sides) {
        this.sides = sides;
    }


    public double[] getSides() {
        return sides;
    }
    
    public void setSides(double[] sides) throws Exception {
        this.sides = sides;

        if (sides.length < 3 || sides.length > 3 || (sides[0] + sides[1]) < sides[2] || 
        (sides[0] + sides[2]) < sides[1] || (sides[2] + sides[1]) < sides[0]){
            throw new Exception("В треугольнике должно быть 3 стороны.\nТреугольник с такими сторонами не может существовать.");
        } 
        // if ((sides[0] + sides[1]) < sides[2] || (sides[0] + sides[2]) < sides[1] ||
        //     (sides[2] + sides[1]) < sides[0]){
        //         throw new Exception("Треугольник с такими сторонами не может существовать.");
        //     }
    }

    @Override
    public String toString() {
        return "Длины сторон треугольника равны а = " + sides[0] + ", b = " + sides[1] + ", c = " + sides[2];
    }

    @Override
    public double perimetr() {
        double perimeter = 0;
        for (Double side : sides) {
            perimeter += side;
        }
        return perimeter;
    }

    @Override
    public double area() {
        double a = sides[0];
        double b = sides[1];
        double c = sides[2];
        double p = perimetr() / 2;
        double area = Math.sqrt(p * (p - a) * (p - b) * (p - c));
        return area;
    }
    
    
}


// protected double sideA;
//     protected double sideB;
//     protected double sideC;

//     public Triangle(double sideA, double sideB, double sideC) throws Exception{
//         this.sideA = sideA;
//         this.sideB = sideB;
//         this.sideC = sideC;

//         if ((sideA + sideB) < sideC || (sideC + sideB) < sideA || (sideA + sideC) < sideB) {
//             throw new Exception("Треугольника с такими сторонами существовать не может");
//         }
//     }

//     @Override
//     public double perimetr() {
//         return sideA + sideB + sideC;
//     }

//     @Override
//     public double area() {
//         double halfMeter = this.perimetr() / 2;
//         return Math.sqrt(halfMeter * (halfMeter - sideA) * (halfMeter - sideB) * (halfMeter - sideC));
//     }

//     @Override
//     public String toString() {
//         return "Длины сторон треугольника равны а = " + sideA + ", b = " + sideB + ", c = " + sideC;
//     }

//     public void setSideA(double sideA) {
//         this.sideA = sideA;
//     }

//     public void setSideB(double sideB) {
//         this.sideB = sideB;
//     }

//     public void setSideC(double sideC) {
//         this.sideC = sideC;
//     }