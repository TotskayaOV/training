package Homework21;

public class Milk extends FoodProduct {
    protected Double percentageFat;

    protected Milk(String nameProduct, Double priceProduct, Integer countProduct, String measureUnit,
            String expirationDate, Double percentageFat) {
        super(nameProduct, priceProduct, countProduct, measureUnit, expirationDate);
        this.percentageFat = percentageFat;
    }
    

    public Double getPercentageFat() {
        return percentageFat;
    }

    
    @Override
    public String toString(){
        return super.toString() + ", жирность: " + percentageFat + "%";
    }
    
}
