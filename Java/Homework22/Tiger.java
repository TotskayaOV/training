package Homework22;

public class Tiger extends Wild {

    public Tiger(Double growth, Double weight, String eyeColor, String habitat, String discoveryDate) {
        super(growth, weight, eyeColor, habitat, discoveryDate);
    }

    
    public void voice() {
        System.out.println("Гррррр!");;
    }

    @Override
    public String toString() {
        return "Тигр. " + super.toString();
    }
}
