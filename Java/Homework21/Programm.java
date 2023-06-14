package Homework21;


public class Programm {
    
    static void showStocks(Product [] goods){
        System.out.println("-------Товары на складе-------\n");
        int itemNumbering = 1;
        for (Product item: goods) {
            System.out.println(itemNumbering + ". " + item);
            itemNumbering += 1;
        }
    }

    public static void main(String[] args) {
        Milk product1 = new Milk("Зелёный луг", 56.2, 50, "бутылок", "10 марта 2023", 3.2);
        Lemonade product2 = new Lemonade("Добрый Cola", 99.0, 6, "бутылок", 1.5, true);
        Bread product3 = new Bread("Бородинский", 64.2, 5, "штук", "10 марта 2023", "ржаная");
        Egg product4 = new Egg("Яркое утро", 100.9, 30, "пачек", "10 апреля 2023", 10);
        Masks product5 = new Masks("Чистовье", 163.0, 4, "пачек", 50);
        ToiletPaper product6 = new ToiletPaper("Zewa", 213.0, 100, "упаковок", 6, 3);
        Diapers product7 = new Diapers("Pampers", 507.0, 3, "упаковок", 1, true, 2, 2.0, 3.5, "трусики");
        Pacifier product8 = new Pacifier("Happy Baby", 226.0, 2, "штуки", 1, false);

        Product[] goods = {product1, product2, product3, product4, product5, product6, product7, product8};
        showStocks(goods);
    }
}
