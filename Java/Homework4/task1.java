import java.util.Iterator;
import java.util.LinkedList;

//Пусть дан LinkedList с несколькими элементами. Реализуйте метод, который вернет “перевернутый” список. 
//Постараться не обращаться к листу по индексам.
public class task1 {
    public static void main(String[] args) {
        LinkedList<Integer> list = new LinkedList<>();
        for (int i = 0; i < 10; i++) {
            list.addLast(i);
        } 
        for (Integer item: list){
            System.out.print(item + " ");
        }
        System.out.println("\nА теперь перевернутый список:");
        int size =list.size();
        LinkedList<Integer> listReverse = new LinkedList<>();
        while(size > listReverse.size()){
            listReverse.addLast(list.pollLast());
        }
        for (Integer item: listReverse){
            System.out.print(item + " ");
        }
    }
}

