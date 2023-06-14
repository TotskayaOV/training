import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;

// Найдите сумму всех элементов LinkedList, сохраняя все элементы в списке. Используйте итератор

public class task3 {
    public static void main(String[] args) {
        Integer[] arr = {7, 8, 4, 6, 1, 9, 3, 2, 5};
        LinkedList<Integer> linkedList = new LinkedList<Integer>();
        Collections.addAll(linkedList, arr);
        int result = 0; 
        for (Integer item : linkedList) {
            result = result+ item;            
        }
        System.out.println("Сумма всех элементов списка:" + linkedList + " -> " + result);
    }
}
