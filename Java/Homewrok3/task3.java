//Задан целочисленный список ArrayList. Найти минимальное, максимальное и среднее арифметическое этого списка
package Homewrok3;


public class task3 {
    public static void main(String[] args) {        
        int[] list2 = {2, 7, 3, 9, 1, 10, 8, 37};
        int min = list2[0];
        int max = list2[0];
        int summ = 0;

        for (int i = 0; i < list2.length; i++) {
            if (list2[i] < min){
                min = list2[i];                
            }
            if (list2[i] > max){
                max = list2[i];                
            }
            summ += list2[i];
        }
        float result = summ / list2.length;
        
        System.out.printf("Максимальное значение: %d; минимальное значение: %d; среднее арифметическое = %f. \n", max, min, result);
    }
    
}
