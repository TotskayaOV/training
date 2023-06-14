public package seminar3;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.json.JSONException;
import org.json.JSONObject;
import java.io.FileWriter;

public class JsonFile {
    public static void main(String[] args) throws JSONException {
        JSONObject json = new JSONObject();
        json.put("name", "Андрей");
        json.put("age", 30);
        json.put("city", "New York");

        try (FileWriter file = new FileWriter("example.json", StandardCharsets.UTF_8)) {
            file.write(json.toString());
            System.out.println("Файл успешно создан");
        } catch (IOException e) {
            System.out.println("Ошибка при создании файла: " + e.getMessage());
        }

        String fileName = "example.json";

        try {
            // Считываем содержимое файла в строку
            byte[] bytes = Files.readAllBytes(Paths.get(fileName));

            // Извлекаем значения по ключам
            String name = json.getString("name");
            int age = json.getInt("age");
            String city = json.getString("city");

            // Выводим значения на консоль
            System.out.println("Name: " + name);
            System.out.println("Age: " + age);
            System.out.println("City: " + city);

        } catch (IOException e) {
            System.out.println("Ошибка при чтении файла: " + e.getMessage());
        }

    }
} {
    
}
