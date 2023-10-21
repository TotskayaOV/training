import java.io.IOException;

/**
 * shopToys - creating a 'toy store' (filling in the list of toys from the "prizesStorage" file, the method of adding toys, the method of changing the frequency of dropping toys by id).
 * toysLottery - creation of a prize pool (an arbitrary queue of toys in accordance with the frequency of loss).
 * winningToys - raffle of toys + recording of raffled toys in a file ("winningToys").
 */

public class Main {
    public static void main(String[] args) throws IOException {
        ShopToys shopToys = new ShopToys(); 
        shopToys.put("prizesStorage"); 
        shopToys.add(5, "keychain", 8); 
        shopToys.changeFrequency(6,60); 
        System.out.println(shopToys);

        ToysLottery toysLottery = new ToysLottery(shopToys);

        Draw winningToys = new Draw(); 
        winningToys.draw(10, toysLottery); 
        winningToys.writeToys("winningToys"); 
        System.out.println(winningToys);
    }
}
