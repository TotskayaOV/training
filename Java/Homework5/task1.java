// Реализуйте структуру телефонной книги с помощью HashMap, учитывая, что 1 человек может иметь несколько телефонов.
package Homework5;


public class task1 {
    public static void main(String[] args) {
        PhoneBooks phoneBook1 = new PhoneBooks();
        phoneBook1.add("Иванов", "7892673891");
        phoneBook1.add("Иванов", "7856673891");
        phoneBook1.add("Иванов", "7878073891");
        phoneBook1.add("Сидоров", "7892673891");
        phoneBook1.showContacts();;
    }
}
    
