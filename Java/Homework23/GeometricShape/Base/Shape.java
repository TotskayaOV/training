package Homework23.GeometricShape.Base;

public abstract class Shape implements Comparable<Shape> {

    public abstract double area();
    
    @Override
    public int compareTo(Shape o) {
        return Double.compare(this.area(), o.area());
    }
}
