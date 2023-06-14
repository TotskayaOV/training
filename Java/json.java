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
        json.put("name", "РђРЅРґСЂРµР№");
        json.put("age", 30);
        json.put("city", "New York");

        try (FileWriter file = new FileWriter("example.json", StandardCharsets.UTF_8)) {
            file.write(json.toString());
            System.out.println("Р¤Р°Р№Р» СѓСЃРїРµС€РЅРѕ СЃРѕР·РґР°РЅ");
        } catch (IOException e) {
            System.out.println("РћС€РёР±РєР° РїСЂРё СЃРѕР·РґР°РЅРёРё С„Р°Р№Р»Р°: " + e.getMessage());
        }

        String fileName = "example.json";

        try {
            // РЎС‡РёС‚С‹РІР°РµРј СЃРѕРґРµСЂР¶РёРјРѕРµ С„Р°Р№Р»Р° РІ СЃС‚СЂРѕРєСѓ
            byte[] bytes = Files.readAllBytes(Paths.get(fileName));

            // РР·РІР»РµРєР°РµРј Р·РЅР°С‡РµРЅРёСЏ РїРѕ РєР»СЋС‡Р°Рј
            String name = json.getString("name");
            int age = json.getInt("age");
            String city = json.getString("city");

            // Р’С‹РІРѕРґРёРј Р·РЅР°С‡РµРЅРёСЏ РЅР° РєРѕРЅСЃРѕР»СЊ
            System.out.println("Name: " + name);
            System.out.println("Age: " + age);
            System.out.println("City: " + city);

        } catch (IOException e) {
            System.out.println("РћС€РёР±РєР° РїСЂРё С‡С‚РµРЅРёРё С„Р°Р№Р»Р°: " + e.getMessage());
        }

    }
}
