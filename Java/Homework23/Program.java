package Homework23;

import java.util.ArrayList;
import java.util.List;

import Homework23.GeometricShape.Circle;
import Homework23.GeometricShape.Rectangle;
import Homework23.GeometricShape.Square;
import Homework23.GeometricShape.Triangle;
import Homework23.GeometricShape.Base.Shape;
import Homework23.Interface.Perimetr;

public class Program {
    public static void main(String[] args) throws Exception {
        Figures figures = new Figures();
        figures.add(new Rectangle(4, 5));
        figures.add(new Square(5));
        figures.add(new Triangle(new double []{4, 5, 3}));
        figures.add(new Circle(12));
        figures.add(new Triangle(new double [] {3, 7, 9}));


        System.out.println("\nДо сортировки:");
        figures.AllPrint();
        System.out.println("\nПосле сортировки (полные данные):");
        figures.sortByArea();
        figures.AllMathPrint();
        System.out.println("\nПосле удаления пятой фигуры:");
        figures.remove(4);
        figures.AllPrint();
        System.out.println("\nПосле замены второй фигуры на круг с радиусом 5:");
        figures.set(1, new Circle(5));
        figures.AllPrint();
        System.out.println("\nПосле попытки добавить треугольник со стороной длиннее суммы двух других сторон:");
        figures.set(2, new Triangle(new double [] {3, 7, 20}));
    }

}
