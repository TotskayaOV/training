import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

public class Draw {
    private final ArrayList<String> winningToys = new ArrayList<>();

    public void draw(int count, ToysLottery toysLottery) {
        int numberToys = toysLottery.size();
        for (int i = 1; i <= Math.min(count, numberToys); i++) {
            Toy currentToy = toysLottery.poll();
            winningToys.add(currentToy.getName());
        }
    }


    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("\nList of raffled toys:\n");
        for (int i = 0; i < winningToys.size(); i++) {
            sb.append("\t").append(i + 1).append(". ").append(winningToys.get(i)).append("\n");
        }
        return sb.toString();
    }

    public void writeToys(String filePath) throws IOException {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(filePath))) {
            writer.write("List of raffled toys:\n");
            for (int i = 0; i < winningToys.size(); i++) {
                writer.write((i + 1) + ". " + winningToys.get(i) + "\n");
            }
        }
    }
}
