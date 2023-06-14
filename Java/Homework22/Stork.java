package Homework22;

public class Stork extends Bird implements Fly {

    protected Stork(Double growth, Double weight, String eyeColor) {
        super(growth, weight, eyeColor, 3300.0);
    }

    public void voice() {
        System.out.println("Че-ли че-ли че-ли");;
    }

    public void fly(){
        System.out.printf("Я лечу на %.2f метрах, где %.2f - высота полета", getFlightAltitude(), getFlightAltitude());
    }

    @Override
    public String toString() {
        return "Аист. " + super.toString();
    }
    
}
