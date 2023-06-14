package Homework21;

public class Bread extends FoodProduct {
    protected String typeFlour;

    protected Bread(String nameProduct, Double priceProduct, Integer countProduct, String measureUnit,
            String expirationDate, String typeFlour) {
        super(nameProduct, priceProduct, countProduct, measureUnit, expirationDate);
        this.typeFlour = typeFlour;
    }
    
    public String getTypeFlour() {
        return typeFlour;
    }

    
    @Override
    public String toString(){
        return super.toString() + ", тип муки: " + typeFlour;
    }
}
