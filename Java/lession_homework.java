// Задана натуральная степень k. Сформировать случайным
// образом список коэффициентов (значения от 0 до 100)
// многочлена многочлен степени k.
// *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
// 2. Даны два файла, в каждом из которых находится запись
// многочлена. Сформировать файл содержащий сумму
// многочленов.
import java.util.Scanner;
public class lession_homework {
    public static void main(String[] args) {
        
        Scanner iScanner = new Scanner(System.in);
        boolean flag = false;
        while (flag == false){
            System.out.printf("Введите k: ");
            flag = iScanner.hasNextInt();
        }
        System.out.printf("int k: ");
        boolean flag = iScanner.hasNextInt();
        int k = iScanner.nextInt();
        iScanner.close();
        
        int value = 321;
        int count = 0;
        do {
            value /= 10;
            count++;
            } while (k != 0);
        System.out.println(count);
    }

}
