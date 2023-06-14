package Homework21;

public class Lemonade extends Drinks {
    protected Boolean sugarContent;

    protected Lemonade(String nameProduct, Double priceProduct, Integer countProduct, String measureUnit, Double value, Boolean sugarContent) {
        super(nameProduct, priceProduct, countProduct, measureUnit, value);
        this.sugarContent = sugarContent;
    }
    
    public Boolean getSugarContant() {
        return sugarContent;
    }
    
    @Override
    public String toString(){
        if (sugarContent){
            return super.toString();
        } else {
            return super.toString() + ", не содержит сахара";
        }
    }
}
