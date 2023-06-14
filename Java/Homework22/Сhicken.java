package Homework22;

public class Сhicken extends Bird implements Fly{

    public Сhicken(Double growth, Double weight, String eyeColor) {
        super(growth, weight, eyeColor, 3.5);
    }

    
    public void voice() {
        System.out.println("Ко ко ко!");;
    }


    public void fly(){
        System.out.printf("Я лечу на %.2f метрах, где %.2f - высота полета", getFlightAltitude(), getFlightAltitude());
    }


    @Override
    public String toString() {
        return "Курица." + super.toString();
    }
}
