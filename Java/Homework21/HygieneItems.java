package Homework21;

public class HygieneItems extends Product {
    Integer countPerPack;

    public HygieneItems(String nameProduct, Double priceProduct, Integer countProduct, String measureUnit, Integer countPerPack) {
        super(nameProduct, priceProduct, countProduct, measureUnit);
        this.countPerPack = countPerPack;
    }

    public Integer getCountPerPack() {
        return countPerPack;
    }

    
    @Override
    public String toString(){
        return super.toString() + ", количество в упаковке: " + countPerPack;
    }
}
