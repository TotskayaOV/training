package task1;

import java.util.InputMismatchException;
import java.util.Scanner;


public class PowerCalculator {


    public static double inputNum() throws InputMismatchException {
        Scanner sc = new Scanner(System.in);
        return sc.nextDouble();
    }


    public static double calculatePower(double num1, double num2) throws InvalidInputException{
        if (num1 == 0) throw new InvalidInputException("Основание не может быть равным нулю");
        if (num2 < 0) throw new InvalidInputException("Сстепень не может быть отрицательной!");
        return Math.pow(num1, num2);
    }


    public static void main(String[] args) {
        try {
            System.out.print("Введите основание: ");
            double num1 = inputNum();
            System.out.print("Введите степень: ");
            double num2 = inputNum();
            double result = calculatePower(num1, num2);
            System.out.printf("%.2f ^ %.2f = %.2f",num1, num2, result);
        }catch (InputMismatchException e){
            System.out.println("Некорректный ввод");
        }catch (InvalidInputException e){
            System.out.println("Ошибка: " + e.getMessage());
        }
    }
}


class InvalidInputException extends Exception{
    public InvalidInputException(String message) {
        super(message);
    }
}