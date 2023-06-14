package Homework22;

// 1.Рост животного
// 2.Вес животного
// 3.Цвет глаз животного
// И методы:
// 1.Издать звук
// 2.Напечатать информацию о животном

public abstract class Animal {
    /**
     * growth - рост
     * weight - вес
     * eyeColor - цвет глаз
     */
    private Double growth;
    private Double weight;
    private String eyeColor;


    protected Animal(Double growth, Double weight, String eyeColor){
        this.growth = growth;
        this.weight = weight;
        this.eyeColor = eyeColor;
    }
    

    public abstract void voice();


    @Override
    public String toString() {
        return "рост: " + growth + ", вес: " + weight + ", цвет глаз: " + eyeColor;
    }
}
