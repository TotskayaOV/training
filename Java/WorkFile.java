public package JAVA;

import java.io.File;
import java.io.IOException;
import java.io.FileOutputStream;
import java.io.FileInputStream;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.nio.charset.StandardCharsets;

public class WorkFile {
    public static void main(String[] args) {
        /*
         * Класс File
         * Класс File позволяет создавать объекты, которые представляют собой путь к
         * файлу
         * или директории в файловой системе. С помощью объектов класса File можно
         * выполнять различные операции
         * с файлами, например, создавать, копировать, перемещать, переименовывать и
         * удалять файлы.
         */
        File file = new File("example.txt");
        try {
            boolean result = file.createNewFile();
            if (result) {
                System.out.println("Файл успешно создан");
            } else {
                System.out.println("Файл уже существует");
            }

            /*
             * Для решения проблемы c кодировкой можно воспользоваться классом
             * OutputStreamWriter,
             * который позволяет указать кодировку при создании объекта.
             */
            FileOutputStream fos = new FileOutputStream(file);
            OutputStreamWriter osw = new OutputStreamWriter(fos, StandardCharsets.UTF_8);
            BufferedWriter writer = new BufferedWriter(osw);

            writer.write("Пример записи в файл");
            writer.newLine();
            writer.write("Еще одна строка");
            writer.close();

            System.out.println("Запись в файл выполнена");
        } catch (IOException e) {
            System.out.println("Ошибка при создании файла: " + e.getMessage());
        }
        /*
         * копирование файла
         */
        File targetFile = new File("target.txt");

        try (FileInputStream in = new FileInputStream(file); // класс для использования чтения данных
                FileOutputStream out = new FileOutputStream(targetFile)) { // класс для записи данных
            byte[] buffer = new byte[1024]; // для записи файла, так как метод ниже read() считывает по 1 биту
            int length;
            while ((length = in.read(buffer)) > 0) { // смотрим до тех пор пока бит в файле не станет 0
                out.write(buffer, 0, length);
            }

            System.out.println("Файл успешно скопирован");
        } catch (IOException e) {
            System.out.println("Ошибка при копировании файла: " + e.getMessage());
        }
    }
} {
    
}
