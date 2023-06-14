import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;


public class ShopToys {
    private final ArrayList<Toy> toys = new ArrayList<>();


    public void add(int id, String name, int frequency) {
        Toy toy = new Toy(id, name, frequency);
        toys.add(toy);
    }


    public void changeFrequency(int id, int frequency) {
        for (Toy toy: toys) {
            if (toy.getId() == id){
                toy.setFrequency(frequency);
            }
        }
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("\nList of toys:\n");
        for (Toy toy : this.toys) {
            sb.append("\t").append(toy.getId()).append(". ").append(toy).append("\n");
        }
        return sb.toString();
    }

    
    public ArrayList<Toy> getToys() {
        return toys;
    }


    public void put(String filePath) {
        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String[] toyData = line.split(" ");
                int id = Integer.parseInt(toyData[1]);
                String name = toyData[6];
                int frequency = Integer.parseInt(toyData[4]);
                toys.add(new Toy(id, name, frequency));
            }
        } catch (IOException e) {
            System.err.format("Error reading file: %s%n", e);
        }
    }
}
