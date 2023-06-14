// Дано четное число N и символы с1 и с2. Написать метод который вернет строку длины N, который состоится из чередующихся символов с1 и с2, начиная с с1. 

// public class seminar02 {
//     public static void main(String[] args){
//         String c1 = "c1";
//         String c2 = "c2";
//         int N = 8;
//         String result = "";
//         for (int i = 0; i < N/2; i++) {
//             result = result + c1 + c2;
//         }
//         System.out.println(result);


//     }
// }

// Напишите метод, который сжимает строку

// public class seminar02 {
//     public static void main(String[] args){
//         String new_str = "aaaabbbcddf";
//         int count = 1;
//         StringBuilder result = new StringBuilder();
//         // Character temp;
//         for (int i = 1; i < new_str.length(); i++) {
//             var temp = new_str.charAt(i-1);
//             if (i == (new_str.length()-1)){
//                 if (temp == new_str.charAt(i)){
//                     count += 1;
//                     result.append(Integer.toString(count));
//                     result.append(new_str.charAt(i));
//                 } else{
//                     result.append(Integer.toString(count));
//                     result.append(temp);
//                     result.append(Integer.toString(1));
//                     result.append(new_str.charAt(i));
//                 }
//             } else if (temp == new_str.charAt(i)){
//                 count += 1;
//             }
//             else {
//                 result.append(Integer.toString(count));
//                 result.append(temp);
//                 count = 1;
//             }
//         }
//         System.out.println(result);
//     }
// }

// Напишите метод, которвй принимает строку (String) и определяет является ли строка (палиндромом(возвращает boolean значение))
// import java.util.Scanner;
// public class seminar02 {
//     public static void main(String[] args){
//         Scanner reader = new Scanner(System.in);
//         System.out.print("Введите строку: ");
//         String pl = reader.nextLine();
//         reader.close();
//         boolean flag = false;
//         StringBuilder result = new StringBuilder(pl);
//         String pl2 = new String(result.reverse());
//         if (pl.equals(pl2)){
//             flag = true;
//         }
//         System.out.println(flag);
//     }
// }

// Напишите метод, который составляет строку, состоящую из 100 повторений слова TEST и метод, который запишет эту строку в простой текстовый файл, 
//обработайте исключения
// import java.io.FileWriter;
// import java.io.IOException;
// public class seminar02 {
//     public static void main(String[] args){
//         StringBuilder test = new StringBuilder();
//         for (int i = 0; i < 100; i++) {
//             test.append("TEST");
//         }
//         System.out.println(test);
//         String to_file = new String(test);  
//         try (FileWriter fw = new FileWriter("file_seminar02_1.txt", false)) {
//              fw.write(to_file);
//              fw.flush();
//              } catch (IOException ex) {
//              System.out.println("Error!");
//              }
//     }
// }

// Напишите метод, который вернет содержимое текушей папки в виде массива строк.
// Напишите метод, который запишет массив, возвращенный предыдущим методом в файл.
// Обработайте ошибки с помощью try-catch конструкции

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;
import java.util.logging.*;
import java.lang.System.Logger;

public class seminar02 {
    public static void main(String[] args){
        Logger logger = Logger.getLogger(seminar02_Logger.class.getName());
        FileHandler ch = new FileHandler("log.txt");
        logger.addHandler(ch);
        
        ToArray(Arrays.toString(getDirArr()));
        System.out.println("Done!");
    }
    // записывает в файл:
    public static void ToArray(String to_file){
        
        try (FileWriter fw = new FileWriter("file_seminar02_2.txt", false)) {
            fw.write(to_file);
            fw.flush();
            } catch (IOException ex) {
            System.out.println("Error!");
            }
    }
    // создает массив строк из содержимого текущей папки
    public static String[] getDirArr(){
        try{
            String pathProject = System.getProperty("user.dir");
            File dir = new File(pathProject);
            String[] allFiles = dir.list();
            return allFiles;
        } catch (Exception e) {
            System.out.println("Error!");
        }
        return new String[0];
    }
}