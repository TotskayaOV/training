package Homework21;

public class Pacifier extends BabyProducts {

    protected Pacifier(String nameProduct, Double priceProduct, Integer countProduct, String measureUnit, Integer age,
            Boolean hypoallergenic) {
        super(nameProduct, priceProduct, countProduct, measureUnit, age, hypoallergenic);
    }
    

    @Override
    public String toString(){
        return super.toString();
    }
}
