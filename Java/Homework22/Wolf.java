package Homework22;

// 4.Волк со свойством:
// 4.1 Вожак стаи(доступным только для чтения внешним классам)

public class Wolf extends Wild {
    protected Boolean alpha;

    public Wolf(Double growth, Double weight, String eyeColor, String habitat, String discoveryDate, Boolean alpha) {
        super(growth, weight, eyeColor, habitat, discoveryDate);
        this.alpha = alpha;
    }


    public void voice() {
        System.out.println("Ууууууу!");;
    }

    @Override
    public String toString() {
        if (alpha){
            return "Волк. " + super.toString() + ", вожак стаи";
        } else {
            return "Волк. " + super.toString();
        }
    }
    
}
