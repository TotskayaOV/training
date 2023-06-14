// Вывести все простые числа от 1 до 1000
package Homework1;
public class task2 {
    public static void main(String[] args) {
        int [] arr = new int[1000];
        int value = 1;
        for(int i = 0; i < arr.length; i++){
           arr[i] = value;
           value += 1;        
        }
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] != 0){
                for (int j = i+1; j < arr.length; j++) {
                    if (arr[j] != 0){
                        if (arr[j] % arr[i] == 0){
                            arr[j] = 0;
                }}}
            }
        }
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] != 0){
                System.out.print(arr[i] + " ");    
            }
        }        
    }
}