package Homework21;

public class Drinks extends Product{
    protected Double value;

    protected Drinks(String nameProduct, Double priceProduct, Integer countProduct, String measureUnit, Double value) {
        super(nameProduct, priceProduct, countProduct, measureUnit);
        this.value = value;
    }
    
    public Double getValueDrinks() {
        return value;
    }

    
    @Override
    public String toString(){
        return super.toString() + " Объем: " + value + "л.";
    }
}
