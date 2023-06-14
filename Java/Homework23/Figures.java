package Homework23;

import java.util.ArrayList;
import java.util.Collections;

import Homework23.GeometricShape.Base.Shape;
import Homework23.Interface.Circumference;
import Homework23.Interface.Perimetr;

public class Figures {
    private final ArrayList<Shape> figures = new ArrayList<>();
    
    public void AllPrint(){
        int count = 1;
        for (Shape element: figures){
            System.out.println(count + ". " + element);
            count += 1;
        }
        System.out.println();
    }

    public void AllMathPrint(){
        int count = 1;
        for (Shape element: figures){
            System.out.println(count + ". " + element);
            if (element instanceof Perimetr){
                System.out.printf("\tПериметр фигуры: %.2f, площадь фигуры: %.2f.\n", ((Perimetr) element).perimetr(), element.area());
            }
            if (element instanceof Circumference){
                System.out.printf("\tОкружность фигуры: %.2f, площадь фигуры: %.2f.\n", ((Circumference) element).circumference(), element.area());
            }
            count += 1;
        }
        System.out.println();
    }

    public void add(Shape figure){
        this.figures.add(figure);
    }

    public void sortByArea(){
        Collections.sort(this.figures);
    }

    public void remove(int i){
        this.figures.remove(i);
    }

    public void set(int i, Shape figure){
        this.figures.set(i, figure);
    }

}
