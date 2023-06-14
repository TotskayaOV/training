package Homework22;

import java.util.ArrayList;
import java.util.Scanner;


public class Menu {

    public static void AllPrint(ArrayList<Animal> zoo){
        int count = 1;
        System.out.println("\n-------Список животных в зоопарке-------\n");
        for (Animal element: zoo){
            System.out.println(count + ". " + element);
            count += 1;
        }
        System.out.println();
    }


    public static void AllVoice(ArrayList<Animal> zoo){
        System.out.println("\n-------Все животные привестствуют вас!-------\n");
        for (Animal element: zoo){
            element.voice();;
        }
        System.out.println();
    }


    public static void NewAnimal(ArrayList<Animal> zoo){
        Scanner iScanner3 = new Scanner(System.in);
        System.out.printf("Кого вы привели?\n1. Кошка.\n2. Собака.\n3. Волк.\n4. Тигр.\n5. Курица.\n6. Аист.\nВведите пункт меню: ");
        int animalChoise = iScanner3.nextInt();
        Scanner iScanner7 = new Scanner(System.in);
        System.out.printf("введите высоту животного в холке: ");
        Double growth = iScanner7.nextDouble();
        Scanner iScanner5 = new Scanner(System.in);
        System.out.printf("введите вес животного: ");
        Double weight = iScanner5.nextDouble();
        Scanner iScanner6 = new Scanner(System.in);
        System.out.printf("введите цвет глаз: ");
        String eyeColor = iScanner6.nextLine();
        if (animalChoise == 1 | animalChoise == 2){
            Scanner iScanner8 = new Scanner(System.in);
            System.out.printf("введите кличку: ");
            String nicknamePet = iScanner8.nextLine();
            Scanner iScanner9 = new Scanner(System.in);
            System.out.printf("введите породу: ");
            String breed = iScanner9.nextLine();
            Scanner iScanner10 = new Scanner(System.in);
            System.out.printf("чем вакцинировано животное: ");
            String vaccinations = iScanner10.nextLine();
            Scanner iScanner11 = new Scanner(System.in);
            System.out.printf("укажите окрас: ");
            String coatColor = iScanner11.nextLine();
            Scanner iScanner12 = new Scanner(System.in);
            System.out.printf("напишите дату рождения: ");
            String birthdate = iScanner12.nextLine();
            if (animalChoise == 1){
                Scanner iScanner13 = new Scanner(System.in);
                System.out.printf("есть ли у кошки шерсть (введите 1, если да, и 0, если нет): ");
                Integer bald = iScanner13.nextInt();
                boolean balding = true;
                if (bald == 1){
                    balding = false;
                }
                Animal cat = new Cat(growth, weight, eyeColor, nicknamePet, breed, vaccinations, coatColor, birthdate, balding); 
                zoo.add(cat);
            } else {
                Scanner iScanner14 = new Scanner(System.in);
                System.out.printf("есть ли у кошки шерсть (введите 1, если да, и 0, если нет): ");
                Integer train = iScanner14.nextInt();
                boolean training = true;
                if (train == 0){
                    training = false;
                }
                Animal dog = new Dog(growth, weight, eyeColor, nicknamePet, breed, vaccinations, coatColor, birthdate, training); 
                zoo.add(dog);
            }
        } else if (animalChoise == 3 | animalChoise == 4){
            Scanner iScanner15 = new Scanner(System.in);
            System.out.printf("Место обитания: ");
            String habitat = iScanner15.nextLine();
            Scanner iScanner16 = new Scanner(System.in);
            System.out.printf("Дата нахождения: ");
            String discoveryDate = iScanner16.nextLine();
            if (animalChoise == 3){
                Scanner iScanner17 = new Scanner(System.in);
                System.out.printf("Это альфа (введите 1, если да, и 0, если нет): ");
                Integer alf = iScanner17.nextInt();
                Boolean alfa = true;
                if (alf == 0){
                    alfa = false;
                }
                Animal wolf = new Wolf(growth, weight, eyeColor, habitat, discoveryDate, alfa); 
                zoo.add(wolf);
            } else {
                Animal tiger = new Tiger(growth, weight, eyeColor, habitat, discoveryDate); 
                zoo.add(tiger);
            }
        } else if (animalChoise == 5 | animalChoise == 6){
            if (animalChoise == 5){
                Animal chicken = new Сhicken(growth, weight, eyeColor); 
                zoo.add(chicken);
            } else {
                Animal stork = new Stork(growth, weight, eyeColor); 
                zoo.add(stork);
            }
        }        
    }


    public static void DelAnimal(ArrayList<Animal> zoo){
        Scanner iScanner19 = new Scanner(System.in);
        System.out.printf("1. Показать список животных.\n2. Вы знаете номер животного, которое хотите забрать.\nВведите пункт меню: ");
        Integer move = iScanner19.nextInt();
        if (move == 1){
            AllPrint(zoo);
            DelAnimal(zoo);
        } else {
            Scanner iScanner20 = new Scanner(System.in);
            System.out.printf("Введите порядковый номер животного, которое хотите забрать\n(Внимание! Держать диких животных дома опасно!): ");
            Integer choise_del = iScanner20.nextInt();
            zoo.remove(choise_del-1);
        }
    }


    public static void OneAnimal(ArrayList<Animal> zoo){
        Scanner iScanner21 = new Scanner(System.in);
        System.out.printf("1. Показать список животных.\n2. Вы знаете номер животного.\nВведите пункт меню: ");
        Integer move = iScanner21.nextInt();
        if (move == 1){
            AllPrint(zoo);
            OneAnimal(zoo);
        } else {
            Scanner iScanner22 = new Scanner(System.in);
            System.out.printf("Введите порядковый номер: ");
            Integer choiseAnimal = iScanner22.nextInt();
            Animal thisAnimal = zoo.get(choiseAnimal-1);
            if (thisAnimal instanceof Fly){
                Scanner iScanner23 = new Scanner(System.in);
                System.out.printf("\nВы хотите узнать как летает эта птица?\n1. да\n2. нет\nВведите число: ");
                Integer userChoiseFly = iScanner23.nextInt();
                if (userChoiseFly == 1){
                    ((Fly) thisAnimal).fly();
                }
            }
            if (thisAnimal instanceof ShowAffection){
                Scanner iScanner25 = new Scanner(System.in);
                System.out.printf("\nВы хотите погладить %s?\n1. да\n2. нет\nВведите число: ", ((Pet) thisAnimal).getNickName());
                Integer userChoiseAff = iScanner25.nextInt();
                if (userChoiseAff == 1){
                    ((ShowAffection) thisAnimal).showAffection();
                }
            }
            Scanner iScanner24 = new Scanner(System.in);
            System.out.printf("\nВы хотите услышать его голос?\n1. да\n2. нет\nВведите число: ");
            Integer userChoiseVoice = iScanner24.nextInt();
            if (userChoiseVoice == 1){
                thisAnimal.voice();
            }
            Scanner iScanner26 = new Scanner(System.in);
            System.out.printf("\nВы хотите узнать данные этого животного?\n1. да\n2. нет\nВведите число: ");
            Integer userChoiseThisAnimal = iScanner26.nextInt();
            if (userChoiseThisAnimal == 1){
                System.out.println();
                System.out.println(thisAnimal.toString());
                System.out.println();
            }
        }
    }


    public static void userVois(ArrayList<Animal> zoo) {
        Scanner iScanner = new Scanner(System.in);
        System.out.printf("Что вы хотите сделать?\n1. Узнать какие животные уже есть в зоопарке.\n2. Услышать голоса животных в зоопарке.\n3. Поселить животное в зоопарк.\n4. Забрать животное из зоопарка.\n5. Поработать с отдельным животным в зоопарке.\nВведите пункт меню или 0 для выхода из программы: ");
        int userChoise = iScanner.nextInt();
        switch (userChoise) {
            case 1:
                AllPrint(zoo);
                userVois(zoo);                
                break;
            case 2:
                AllVoice(zoo);
                userVois(zoo);
                break;
            case 3:
                NewAnimal(zoo);
                userVois(zoo);
                break;
            case 4:
                DelAnimal(zoo);
                userVois(zoo);
                break;
            case 5:
                OneAnimal(zoo);
                userVois(zoo);
                break;
            default:
                break;
        }
        iScanner.close();
    }
}
