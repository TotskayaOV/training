package Homework21;

public class Diapers extends BabyProducts {
    protected Integer size;
    protected Double minimumWeight;
    protected Double maximumWeight;
    protected String typeDiaper;

    protected Diapers(String nameProduct, Double priceProduct, Integer countProduct, String measureUnit, Integer age,
            Boolean hypoallergenic, Integer size, Double minimumWeight, Double maximumWeight, String typeDiaper) {
        super(nameProduct, priceProduct, countProduct, measureUnit, age, hypoallergenic);
        this.size = size;
        this.minimumWeight = minimumWeight;
        this.maximumWeight = maximumWeight;
        this.typeDiaper = typeDiaper;
    }
    
    public Integer getSize() {
        return size;
    }

    public Double getMinimumWeight() {
        return minimumWeight;
    }

    public Double getMaximumWeight() {
        return maximumWeight;
    }

    public String getTypeDiaper() {
        return typeDiaper;
    }
    
    @Override
    public String toString(){
        return super.toString() + ", размер: " + size + ", от" + minimumWeight + " до " + maximumWeight + " кг., " + typeDiaper;
    }

}
