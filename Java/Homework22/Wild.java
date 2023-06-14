package Homework22;

public abstract class Wild extends Animal{
    protected String habitat;
    protected String discoveryDate;

    protected Wild(Double growth, Double weight, String eyeColor, String habitat, String discoveryDate) {
        super(growth, weight, eyeColor);
        this.habitat = habitat;
        this.discoveryDate = discoveryDate;
    }
    
    public abstract void voice();

    @Override
    public String toString() {
        return super.toString() + ", место обитания: " + habitat + ", дата нахождения: " + discoveryDate;
    }

}
