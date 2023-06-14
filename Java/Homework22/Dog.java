package Homework22;

// 3.Собака со свойством:
// 3.1 Наличие дрессировки(доступным только для чтения внешним классам)
// и методом:
// 3.2 Дрессировать

public class Dog extends Pet implements ShowAffection {
    protected Boolean training;

    public Dog(Double growth, Double weight, String eyeColor, String nicknamePet, String breed, String vaccinations,
            String coatColor, String birthdate, Boolean training) {
        super(growth, weight, eyeColor, nicknamePet, breed, vaccinations, coatColor, birthdate);
        this.training = training;
    }
    

    public void voice() {
        System.out.println("Гав ав!");;
    }

    public void showAffection() {
        System.out.println("Собака трется об ноги: Урррр");
    }


    @Override
    public String toString() {
        if (training){
            return "Собака. " + super.toString() + ", дрессированная";
        } else {
            return "Собака. " + super.toString();
        }
    }
    
}
