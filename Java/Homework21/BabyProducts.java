package Homework21;

public class BabyProducts extends Product {
    protected Integer age;
    protected Boolean hypoallergenic;

    protected BabyProducts(String nameProduct, Double priceProduct, Integer countProduct, String measureUnit, Integer age, Boolean hypoallergenic) {
        super(nameProduct, priceProduct, countProduct, measureUnit);
        this.age = age;
        this.hypoallergenic = hypoallergenic;
    }

    public Integer getAge() {
        return age;
    }

    public Boolean getHypoallergenic() {
        return hypoallergenic;
    }
    
    @Override
    public String toString(){
        if (hypoallergenic){
            return super.toString() + ", минимальный возраст: " + age + ", гипоаллергенно";
        } else {
            return super.toString() + ", минимальный возраст: " + age;
        }
    }
    
}
