import java.util.LinkedList;

public class ListQueue {
     
    private LinkedList<Integer> linkedList = new LinkedList<>();
    void enqueue(int item) {
        linkedList.addLast(item);
    }
    Integer dequeue() {
        if (linkedList.size()>0) {
            return linkedList.pollFirst();
        }
        return null;
    }
    Integer first() {
        if (linkedList.size()>0) {
            return linkedList.peekFirst();
        }
        return null;
    }
    String doString(){
        return linkedList.toString();
    }
}

