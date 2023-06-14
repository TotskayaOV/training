package Homework5;

import java.util.List;
import java.util.Map;
import java.util.ArrayList;
import java.util.HashMap;


public class PhoneBooks {
    private Map<String, List<String>> dumpContact = new HashMap<>();


    void add(String lastName, String phoneNumber){
        if (dumpContact.containsKey(lastName)){
            dumpContact.get(lastName).add(phoneNumber);
        }
        else{
            ArrayList<String> phoneList = new ArrayList<String>();
            phoneList.add(phoneNumber);
            dumpContact.put(lastName, phoneList);
        }
    }


    void showContacts(){
             for (String name : dumpContact.keySet()) {
                System.out.println(name + ":");
                // ArrayList<String> numbers = dumpContact.get(name);
                // System.out.println(Arrays.toString(dumpContact.get(name)));
                int count = 0;
                for (String number : dumpContact.get(name)){
                    System.out.printf("\t%d. %s\n", ++count, number);
                }                    
                }
            }
           
}

