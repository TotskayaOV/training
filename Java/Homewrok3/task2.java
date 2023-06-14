// Пусть дан произвольный список целых чисел, удалить из него четные числа
package Homewrok3;
import java.util.ArrayList;

public class task2 {
    public static void main(String[] args) {
        int[] list2 = {2, 7, 3, 9, 1, 10, 8, 37};
        ArrayList<Integer> list = new ArrayList<Integer>();
        
        for (int i = 0; i < list2.length; i++) {
            if (list2[i] % 2 != 0){
                list.add(list2[i]);                
            }
        }
        for (Object o: list){
            System.out.println(o);
        }
    }
    
}
