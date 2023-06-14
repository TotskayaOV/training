package Homework21;


public class FoodProduct extends Product{
    protected String expirationDate;

    protected FoodProduct(String nameProduct, Double priceProduct, Integer countProduct, String measureUnit, String expirationDate) {
        super(nameProduct, priceProduct, countProduct, measureUnit);
        this.expirationDate = expirationDate;
    }
    

    public String getExpirationDate() {
        return expirationDate;
    }

    
    @Override
    public String toString(){
        return super.toString() + ", срок годности: " + expirationDate;
    }
}
