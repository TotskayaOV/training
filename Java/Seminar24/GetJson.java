package Seminar24;

public class GetJson {
    public static <E> String returnJson(E el) {

        StringBuilder rez = new StringBuilder();

        if (el instanceof Integer) {
            rez.append(el.toString());
        } else if (el instanceof String) {
            rez.append("\"" + el + "\"");
        } else if (el instanceof Cat) {
            rez.append(el.toString());
        }

        return rez.toString();
    }
}
