import java.util.*;

public class ToysLottery {
    private final Queue<Toy> toysQueue;


    public ToysLottery(ShopToys shopToys) {
        ArrayList<Toy> playableToys = new ArrayList<>();
        toysQueue = new LinkedList<>();
        for (Toy toy : shopToys.getToys()) {
            for (int i = 0; i < toy.getFrequency(); i++) {
                playableToys.add(toy);
            }
        }
        Collections.shuffle(playableToys);
        toysQueue.addAll(playableToys);
    }


    public int size() {
        return toysQueue.size();
    }


    public Toy poll() {
        return toysQueue.poll();
    }
}
