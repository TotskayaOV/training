package Projekt;

import java.io.IOException;
import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Scanner;
import java.util.Set;


public class Main {
    public static void userVois(OurNotebook notebookUser, LinkedList list) {
            Scanner iScanner = new Scanner(System.in);
            System.out.printf("Какие параметры вы хотите видеть у своего ноутбука:\n1. Оперативная память\n2. Объем жесткого диска\n3. Предустановленная ОС\n4. цвет\nВведите номер пункта меню для выбора или введите 0: ");
            int userChoise = iScanner.nextInt();
            switch (userChoise) {
                case 1:
                    Scanner iScanner1 = new Scanner(System.in);
                    System.out.printf("Введите желаемое количество Оперативной памяти (число): ");
                    int userRum = iScanner1.nextInt();
                    notebookUser.ram = userRum;
                    list.set(1, true);
                    userVois(notebookUser, list);
                    break;
                case 2:
                    Scanner iScanner2 = new Scanner(System.in);
                    System.out.printf("Введите желаемый объем жесткого диска (число): ");
                    int userHdd = iScanner2.nextInt();
                    notebookUser.hdd = userHdd;
                    list.set(2, true);
                    userVois(notebookUser, list);
                    break;
                case 3:
                    Scanner iScanner3 = new Scanner(System.in);
                    System.out.printf("Введите желаемую операционную систему: ");
                    String userOSystem = iScanner3.nextLine();
                    notebookUser.oSystem = userOSystem;
                    list.set(3, true);
                    userVois(notebookUser, list);
                    break;
                case 4:
                    Scanner iScanner4 = new Scanner(System.in);
                    System.out.printf("Введите желаемый цвет ноутбука: ");
                    String userColore = iScanner4.nextLine();
                    notebookUser.colore = userColore;
                    list.set(0, true);
                    userVois(notebookUser, list);
                    break;
                default:
                    break;
            }
            iScanner.close();
        }


    private static boolean sortByRam(OurNotebook param, OurNotebook param2){
            if (param.ram >= param2.ram) {
                    return true;
                }else {
                    return false;
            }
       }
    
    private static boolean sortByHdd(OurNotebook param, OurNotebook param2){
        if (param.hdd >= param2.hdd) {
                return true;
            }else {
                return false;
        }
   }

    private static boolean sortByColore(OurNotebook param, OurNotebook param2){
        if ((param.colore).equals(param2.colore)) {
            return true;
        }else {
            return false;
        }
    }

    private static boolean sortByOsystem(OurNotebook param, OurNotebook param2){
        if ((param.oSystem).equals(param2.oSystem)) {
            return true;
        }else {
            return false;
    }
    }

    /**
     * @param args
     * @throws IOException
     * @throws ClassNotFoundException
     * @throws CloneNotSupportedException
     */

    public static void main(String[] args) throws IOException, ClassNotFoundException, CloneNotSupportedException {
        Set<OurNotebook> set = new HashSet<>();
        
        OurNotebook notebook1 = new OurNotebook("ASD098FD39048", "GameKiller", "black", 16, 256, "Linux", "Core i3");
        OurNotebook notebook2 = new OurNotebook("FGHD098FD3943", "Banan", "black", 16, 512, "Windows", "Core i");
        OurNotebook notebook3 = new OurNotebook("QGHD098567948", "Turbo", "pink", 64, 512, "Linux", "Core i7");
        OurNotebook notebook4 = new OurNotebook("VDFHD05667991", "Turbo", "black", 64, 512, "Linux", "Core i7");
        OurNotebook notebook5 = new OurNotebook("12HD09FG67948", "GMV500", "pink", 32, 256, "Windows", "Core i5");
        OurNotebook notebook6 = new OurNotebook("BMFGW85679041", "GMV500", "pink", 32, 256, "Windows", "Core i5");
        OurNotebook notebook7 = new OurNotebook("QGHD098567945", "GMV500", "black", 32, 256, "Linux", "Core i3");
        OurNotebook notebook8 = new OurNotebook("JKLD011567444", "GMV500", "black", 32, 256, "Linux", "Core i5");
        OurNotebook notebook9 = new OurNotebook("JKLD011534548", "GameKiller", "black", 32, 256, "Linux", "Core i3");
        OurNotebook notebook10 = new OurNotebook("TKLD018657440", "GMV500", "black", 2, 124, "Linux", "Core i5");
        OurNotebook notebook11 = new OurNotebook("HG56711567444", "GMV400", "green", 32, 256, "Windows", "Core i5");
        OurNotebook notebook12 = new OurNotebook("BNV0115645454", "GMV100", "white", 128, 512, "Linux", "Core i7");
        OurNotebook notebook13 = new OurNotebook("PO849934JH993", "GameKiller", "black", 16, 256, "Windows", "Core i5");

        set.add(notebook1);
        set.add(notebook2);
        set.add(notebook3);
        set.add(notebook4);
        set.add(notebook5);
        set.add(notebook6);
        set.add(notebook7);
        set.add(notebook8);
        set.add(notebook9);
        set.add(notebook10);
        set.add(notebook11);
        set.add(notebook12);
        set.add(notebook13);

        OurNotebook notebookUserchoise = new OurNotebook("default", "default", "default", 0, 0, "default", "default");
        LinkedList<Boolean> list = new LinkedList<>();
        list.add(false);
        list.add(false);
        list.add(false);
        list.add(false);
        userVois((OurNotebook) notebookUserchoise, list);
        Set<OurNotebook> setResult = new HashSet<>();

        Iterator<OurNotebook> iterator = set.iterator();
        while (iterator.hasNext()) {
            OurNotebook element = iterator.next();
            if (list.get(0) && list.get(1) && list.get(2) && list.get(3)){
                if (element.equalityHdd(notebookUserchoise) && element.equalityRam(notebookUserchoise) && element.equalsColore(notebookUserchoise) && element.equalsOS(notebookUserchoise)){
                    setResult.add(element);
                }
            } else if (list.get(1) && list.get(0) && list.get(2) && !(list.get(3))){
                if (element.equalityRam(notebookUserchoise) && element.equalsColore(notebookUserchoise) && element.equalityHdd(notebookUserchoise)){
                setResult.add(element);
                }
            } else if (list.get(3) && list.get(0) && list.get(2) && !(list.get(1))){
                if (element.equalityHdd(notebookUserchoise) && element.equalsColore(notebookUserchoise) && element.equalsOS(notebookUserchoise)){
                setResult.add(element);
                }         
            } else if (list.get(3) && list.get(1) && list.get(2) && !(list.get(0))){
                if (element.equalityRam(notebookUserchoise) && element.equalsOS(notebookUserchoise) && element.equalityHdd(notebookUserchoise)){ 
                setResult.add(element);
                }
            } else if (list.get(0) && list.get(1) && !(list.get(3)) && !(list.get(2))){
                if (sortByRam(element, notebookUserchoise) && sortByColore(element, notebookUserchoise)){
                setResult.add(element);
                }
            } else if (list.get(0) && list.get(2) && !(list.get(1)) && !(list.get(3))){ 
                if (sortByColore(element, notebookUserchoise) && sortByHdd(element, notebookUserchoise)){
                setResult.add(element);
                }
            } else if (list.get(2) && list.get(1) && !(list.get(0)) && !(list.get(3))){
                if (sortByRam(element, notebookUserchoise) && sortByHdd(element, notebookUserchoise)){
                setResult.add(element);
                }
            } else if (list.get(0) && list.get(3) && !(list.get(1)) && !(list.get(2))){ 
                if (sortByColore(element, notebookUserchoise) && sortByOsystem(element, notebookUserchoise)){
                setResult.add(element);
                }
            } else if (list.get(3) && list.get(1) && !(list.get(0)) && !(list.get(2))){ 
                if (sortByRam(element, notebookUserchoise) && sortByOsystem(element, notebookUserchoise)){ 
                setResult.add(element);
                }
            } else if (list.get(2) && list.get(3) && !(list.get(1)) && !(list.get(0))){ 
                if (sortByHdd(element, notebookUserchoise) && sortByOsystem(element, notebookUserchoise)){
                setResult.add(element);
                }
            } else if (list.get(0) && !(list.get(1)) && !(list.get(2)) && !(list.get(3))){
                if (sortByColore(element, notebookUserchoise)){
                setResult.add(element);
                }
            } else if (list.get(1) && !(list.get(0)) && !(list.get(2)) && !(list.get(3))){
                if (sortByRam(element, notebookUserchoise)){
                setResult.add(element);
                }
            } else if (list.get(2) && !(list.get(1)) && !(list.get(0)) && !(list.get(3))){ 
                if (sortByHdd(element, notebookUserchoise)){
                setResult.add(element);
                }
            } else if (list.get(3) && !(list.get(1)) && !(list.get(2)) && !(list.get(0))){ 
                if (sortByOsystem(element, notebookUserchoise)){ 
                setResult.add(element);
                }
            } else {
                break;
            }
        }            
        int count = 1;
        if (setResult.isEmpty()){
            System.out.println("Ноутбуки в наличии: ");
            for (OurNotebook e : set) {
                System.out.println(count + ". " + e);
                count += 1;
            }
        } else {
            System.out.println("По вашему запросу найдены ноутбуки в наличии: ");
            for (OurNotebook e : setResult) {
                System.out.println(count + ". " + e);
                count += 1;
            }
        }
        
    }
}
