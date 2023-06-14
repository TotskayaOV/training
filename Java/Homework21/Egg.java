package Homework21;

public class Egg extends FoodProduct {
    protected Integer numberEggs;

    protected Egg(String nameProduct, Double priceProduct, Integer countProduct, String measureUnit,
            String expirationDate, Integer numberEggs) {
        super(nameProduct, priceProduct, countProduct, measureUnit, expirationDate);
        this.numberEggs = numberEggs;
    }

    public Integer getNumberEggs() {
        return numberEggs;
    }

    
    @Override
    public String toString(){
        return super.toString() + ", упаковка: " + numberEggs + "шт.";
    }
    
}
