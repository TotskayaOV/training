package Homework21;

// Реализовать класс товар, содержащий следующие свойства:
// 1. Название
// 2. Цена
// 3. Количество
// 4. Единица измерения

public class Product {
    protected String nameProduct;
    protected Double priceProduct;
    protected Integer countProduct;
    protected String measureUnit;


    protected Product(String nameProduct, Double priceProduct, Integer countProduct, String measureUnit){
        this.nameProduct = nameProduct;
        this.priceProduct = priceProduct;
        this.countProduct = countProduct;
        this.measureUnit = measureUnit;
    }


    public String getNameProduct() {
        return nameProduct;
    }

    public Double getPriceProduct() {
            return priceProduct;
    }


    public Integer getCountProduct() {
        return countProduct;
    }


    public String getMeasureUnit() {
        return measureUnit;
    }

    @Override
    public String toString() {
        return "Наименование: " + nameProduct + ", Цена: " + priceProduct + ", Количество: " + countProduct
                + " " + measureUnit;
    }
}