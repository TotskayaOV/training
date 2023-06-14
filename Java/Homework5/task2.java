// Пусть дан список сотрудников: Иван Иванов, Светлана Петрова, Кристина Белова, Анна Мусина, Анна Крутова, Иван Юрин, Петр Лыков, Павел Чернов, Петр Чернышов, Мария Федорова, Марина Светлова, Мария Савина, Мария Рыкова, Марина Лугова, Анна Владимирова, Иван Мечников, Петр Петин, Иван Ежов. 
//Написать программу, которая найдет и выведет повторяющиеся имена с количеством повторений. Отсортировать по убыванию популярности. 
//Для сортировки использовать TreeMap.

package Homework5;
import java.util.*;
import java.util.Comparator;
public class task2 {
    public static void main(String[] args) {
        String data = "Иван Иванов,\n" + "Светлана Петрова,\n" + "Кристина Белова,\n" + "Анна Мусина,\n" + "Анна Крутова,\n" + "Иван Юрин,\n" +
                "Петр Лыков,\n" + "Павел Чернов,\n" + "Петр Чернышов,\n" + "Мария Федорова,\n" + "Марина Светлова,\n" + "Мария Савина,\n" +
                "Мария Рыкова,\n" + "Марина Лугова,\n" + "Анна Владимирова,\n" + "Иван Мечников,\n" + "Петр Петин,\n" + "Иван Ежов.";
    
        LinkedList<String> parsedData = parsingNames(data);

        System.out.println("Количество повторений:");
        TreeMap<String, Integer> countMap = getFillingCount(parsedData);
        System.out.println(countMap);


        TreeMap<String, Integer> sortedMap = getSortedByValue(countMap);
        System.out.println("Отсортированный список:");
        System.out.println(sortedMap);
    }

    static LinkedList<String> parsingNames(String data) {
        LinkedList<String> list = new LinkedList<>();
        String[] dataArr = data.replaceAll(",", "").replaceAll("\\.", "").split("\n");
        for (String fullName : dataArr) {
            list.add(fullName.split(" ")[0]);
        }
        return list;
    }

    static TreeMap<String, Integer> getFillingCount(LinkedList<String> data) {
        TreeMap<String, Integer> map = new TreeMap<String, Integer>() {
        };
        for (String name : data) {
            if (map.containsKey(name)) {
                map.put(name, map.get(name) + 1);
            } else {
                map.put(name, 1);
            }
        }
        return map;
    }

    static TreeMap<String, Integer> getPrintMap(TreeMap<String, Integer> unsortedMap) {
        Collection<Integer> values = unsortedMap.values();
        System.out.println(values);
        return unsortedMap;
    }

    static TreeMap<String, Integer> getSortedByValue(TreeMap<String, Integer> unsortedMap) {
        CountComparator vc = new CountComparator(unsortedMap);
        TreeMap<String, Integer> sortedMap = new TreeMap<String, Integer>(vc) {
        };
        sortedMap.putAll(unsortedMap);
        return sortedMap;
    }
}
