The project is implemented in the paradigm of Object Oriented Programming: 

### class Main: ###

        void main()

### class ToysLottery: ###

        Queue<Toy> toysQueue

        - create ToysLottery()
        - size()
        - pull()

### class ShopToys: ###

        ArrayList<Toy> toys

        - void add()
        - changeFrequency()
        - toString()
        - put(String filePath)

### class Toy: ###

        int id;
        String name;
        frequency;

        - create Toy()
        - getId()
        - getName()
        - getFrequency()
        - setFrequency()
        - toString()
### class Draw: ###

        ArrayList<String> winningToys

        - void draw()
        - toString()
        - void writeToys()

___        
1. The "Prizes" file has been created (file name: prizesStorage).
2. A Toy class has been created containing three: 
 + toy id fields, 
 + text name,
 + the frequency of toy dropout.
3. Three arrays (lists) are filled in: a list of all toys, a list of toys to draw according to the frequency of dropouts, a list of winning toys.
4. A queue of toys for the Toys Lottery has been created
The draw was held 10 times, the results are recorded in a file(file name: winningToys).