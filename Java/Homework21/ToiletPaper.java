package Homework21;

public class ToiletPaper extends HygieneItems {
    protected Integer layersPaper;

    protected ToiletPaper(String nameProduct, Double priceProduct, Integer countProduct, String measureUnit,
            Integer countPerPack, Integer layersPaper) {
        super(nameProduct, priceProduct, countProduct, measureUnit, countPerPack);
        this.layersPaper = layersPaper;
    }

    public Integer getLayersPaper() {
        return layersPaper;
    }

    
    @Override
    public String toString(){
        return super.toString() + ", " + layersPaper + "-слойная";
    }
    
}
