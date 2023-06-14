// Дана строка sql-запроса "select * from students where ". Сформируйте часть  WHERE этого запроса, используя StringBuilder. 
// Данные для фильтрации приведены ниже в виде json строки. Если значение null, то параметр не должен попадать в запрос.
// Параметры для фильтрации: {"name":"Ivanov", "country":"Russia", "city":"Moscow", "age":"null"}

package Homework2;
import java.util.*;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

public class task1 {
    public static void main(String[] args) {
        String students = "{\"name\":\"Ivanov\", \"country\":\"Russia\", \"city\":\"Moscow\", \"age\": null }";
        System.out.println(createRequest(students));
    }

    static String createRequest(String jsonStr) {
        Gson gson = new Gson();
        Map<String, Object> studentMap = gson.fromJson(jsonStr, new TypeToken<Map<String, Object>>(){}.getType());
        StringBuilder sb = new StringBuilder("SELECT * FROM students WHERE ");
        for (Map.Entry<String, Object> entry : studentMap.entrySet()) {
            if (entry.getValue() != null) {
                sb.append(entry.getKey());
                sb.append("=");
                sb.append(entry.getValue());
                sb.append(" and ");
            }
        }
        return sb.toString().substring(0, sb.toString().length() - 5);
    }
}