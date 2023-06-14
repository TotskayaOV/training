// Дана json строка (можно сохранить в файл и читать из файла)
// [{"фамилия":"Иванов","оценка":"5","предмет":"Математика"},{"фамилия":"Петрова","оценка":"4","предмет":"Информатика"},{"фамилия":"Краснов","оценка":"5","предмет":"Физика"}]
// Написать метод(ы), который распарсит json и, используя StringBuilder, создаст строки вида: Студент [фамилия] получил [оценка] по предмету [предмет].
// Пример вывода:
// Студент Иванов получил 5 по предмету Математика.
// Студент Петрова получил 4 по предмету Информатика.
// Студент Краснов получил 5 по предмету Физика.

package Homework2;
import com.google.gson.Gson;
import com.google.gson.annotations.SerializedName;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;


public class task3 {
    public static void main(String[] args) throws IOException {

        String jsonStr = Files.readString(Paths.get("data.json"));
        String result = getString(jsonStr); // парсинг и формирование заданной строки
        System.out.println(result);
    }

    private static String getString(String jsonStr) {
        Gson gson = new Gson();
        Student[] students = gson.fromJson(jsonStr, Student[].class);
        StringBuilder sb = new StringBuilder();
        for (Student student : students) {
            sb.append("Студент ");
            sb.append(student.surname);
            sb.append(" получил ");
            sb.append(student.mark);
            sb.append(" по предмету ");
            sb.append(student.subject);
            sb.append("\n");

        }
        return sb.toString();
    }

    private static class Student {
        @SerializedName("фамилия")
        String surname;
        @SerializedName("оценка")
        String mark;
        @SerializedName("предмет")
        String subject;

        public Student(String surname, String mark, String subject) {
            this.surname = surname;
            this.mark = mark;
            this.subject = subject;

        }
    }
}