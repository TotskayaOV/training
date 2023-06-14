package Seminar24;

public class Program {
    public static void main(String[] args) {

        int number = 2;
        System.out.println(GetJson.returnJson(number));

        String someSring = "Hello";
        System.out.println(GetJson.returnJson(someSring));

        Cat cat = new Cat("Boris", 50);
        System.out.println(GetJson.returnJson(cat));
    }
}
