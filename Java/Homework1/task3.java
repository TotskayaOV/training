// Реализовать простой калькулятор
package Homework1;
import java.util.Scanner;
import java.util.logging.*;
import java.io.IOException;

public class task3 {
    public static void main(String[] args) {
        Scanner iScanner = new Scanner(System.in);
        System.out.printf("Введите 1 число: ");
        int x = iScanner.nextInt();
        Scanner iScanner2 = new Scanner(System.in);
        System.out.printf("Введите 2 число: ");
        int y = iScanner2.nextInt();
        Scanner iScanner3 = new Scanner(System.in);
        System.out.printf("Введите оператор(+, -, *, /): ");
        String z = iScanner3.nextLine();
        float result = 0;
        switch (z) {
            case "+":
                int res_sum = x + y;
                result = (float)res_sum;
                // lg_result(x, y, res_sum, z);
                System.out.printf("%d + %d = %d. \n", x, y, res_sum);
                break;
            case "-":
                int res = x - y;
                result = (float)res;
                System.out.printf("%d - %d = %d. \n", x, y, res);
                break;
            case "*":
                int res_mult = x * y;
                result = (float)res_mult;
                System.out.printf("%d * %d = %d. \n", x, y, res_mult);
                break;
            case "/":
                float res_div = (float)x / (float)y;
                result = res_div;
                System.out.printf("%d : %d = %f. \n", x, y, res_div);
                break;
            default:
                break;
            }
        try {
            String log_string = Integer.toString(x) + z + Integer.toString(y) + "=" + Float.toString(result);
            lg_result(log_string);
        } catch (Exception e) {
            System.err.println("Неправильный формат строки!");
        }
        
    }
    static void lg_result(String oper) throws IOException {
        Logger log = Logger.getLogger(task4.class.getName());
        FileHandler fh =new FileHandler("Homework1/logCalc.txt", true);
        log.addHandler(fh);
        log.setUseParentHandlers(false);

        SimpleFormatter sf = new SimpleFormatter();
        fh.setFormatter(sf);
        System.out.println(oper);
        StringBuilder sb = new StringBuilder("Результат вычисления: ");
        sb.append(oper);
        String res = sb.toString();

        log.log(Level.INFO, res);
    }  
}
