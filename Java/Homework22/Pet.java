package Homework22;

public abstract class Pet extends Animal{
    protected String nicknamePet;
    protected String breed;
    protected String vaccinations;
    protected String coatColor;
    protected String birthdate;

    protected Pet(Double growth, Double weight, String eyeColor, String nicknamePet, String breed, String vaccinations, String coatColor, String birthdate) {
        super(growth, weight, eyeColor);
        this.nicknamePet = nicknamePet;
        this.breed = breed;
        this.vaccinations = vaccinations;
        this.coatColor = coatColor;
        this.birthdate = birthdate;
    }


    public abstract void voice();
 
    
    public String getNickName() {
        return nicknamePet;
    }


    @Override
    public String toString() {
        return "Кличка: " + nicknamePet + ", " + super.toString() +  ", порода: " + breed + ", окрас: " + coatColor + ", дата рождения: " + birthdate + ", проставленные вакцины: " + vaccinations;
    }
}
