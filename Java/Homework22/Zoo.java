package Homework22;

import java.util.ArrayList;


public class Zoo {
    public static void main(String[] args) {
        ArrayList<Animal> zoo = new ArrayList<>();
        Cat cat = new Cat(0.6, 5.0, "зеленый", "Тефтелька", "сфинкс", "бешенство", "розовый", "11 марта 1999", true);
        Wolf wolf = new Wolf(0.9, 90.1, "жёлтые", "Новосибирская область", "02 февраля 2020", true);
        Tiger tiger = new Tiger(0.6, 250.2, "жёлтые", "Дальний Восток", "10 июля 2016");
        Stork stork = new Stork(1.16, 3.0, "черные");

        zoo.add(cat);
        zoo.add(wolf);
        zoo.add(tiger);
        zoo.add(stork);
   
        Menu.userVois(zoo);
        
    }
}
