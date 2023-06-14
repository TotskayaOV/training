package Homework24;

import java.util.Arrays;

public class Programm {
    public static void main(String[] args) {
        Integer[] setValues = {3, 23, 4, 2, 843, 2, 12, 32, 5};
        DynamicArray<Integer> myArray = new DynamicArray<>(setValues);

        System.out.print("Массив: ");
        myArray.print();

        myArray.insert(1);
        System.out.print("Массив после добавления элемента со значением 1: ");
        myArray.print();

        myArray.removeByIndex(2);
        System.out.print("Массив после удаления элемента по индексу 2: ");
        myArray.print();

        myArray.removeByValue(2);
        System.out.print("Массив после удаления элемента со значением 2: ");
        myArray.print();

        System.out.println("Минимальное значение: " + myArray.getMin());
        System.out.println("Максимальное значение: " + myArray.getMax());

        System.out.println("Сумма элементов массива: " + myArray.sum());
        System.out.println("Произведение элементов массива: " + myArray.multiplication());

        System.out.println("Индекс элемента со значением 12: " + myArray.getIndex(12));
        System.out.println("Индекс элемента со значением 2: " + myArray.getIndex(2));


        System.out.println("Проверка наличия в массиве цифры 843: " + myArray.contains(843));
        System.out.println("Проверка наличия в массиве цифры 845: " + myArray.contains(845));

        myArray.bubbleSort();
        System.out.print("Сортировка пузырьком: ");
        myArray.print();

        DynamicArray<Integer> array2 = new DynamicArray<>(setValues);
        System.out.print("\nИзначальный массив: ");
        array2.print();
        array2.insertionSort();
        System.out.print("Сортировка вставками: ");
        array2.print();
        System.out.println();

        DynamicArray<Integer> array3 = new DynamicArray<>(setValues);
        System.out.print("\nИзначальный массив: ");
        array3.print();
        array3.selectionSort();
        System.out.print("Сортировка выбором:");
        array3.print();
        System.out.println();

        System.out.println("Элемент по индексу 1: " + myArray.get(1));


        myArray.set(6, 45);
        System.out.print("Результат замены элемента по индексу 6 на элемент - 45: ");
        myArray.print();

        System.out.println("Длина массива: " + myArray.getLength());
        System.out.println();

        String[] arrayString = {"H", "e", "l", "l", "o", " ", "W", "o", "r", "l", "d", "!"};
        DynamicArray<String> strArray = new DynamicArray<>(arrayString);
        System.out.println("Конкатенация строк: " + strArray.sum());
        System.out.println();
    }
}
