package Homework24;

import java.util.Arrays;

public class DynamicArray<T extends Comparable<T>> {
    private T[] array;
    private int length;

    public int getLength() {
        return length;
    }

    public DynamicArray() {
        this.length = 0;
        this.array = (T[]) new Comparable[0];
    }

    public DynamicArray(T[] values) {
        this.array = Arrays.copyOf(values, values.length);
        this.length = values.length;
    }

    public void insert(T value) {
        if (this.length == this.array.length) {
            array = Arrays.copyOf(array, length + 1);
        }
        array[length] = value;
        length++;
    }

    public void removeByIndex(int index) {
        if (0 > index || index >= length) {
            throw new IndexOutOfBoundsException("Index outside the array");
        }
        for (int i = index; i < length - 1; i++) {
            array[i] = array[i + 1];
        }
        length--;
        array = Arrays.copyOf(array, length);
    }

    public void removeByValue(T value) {
        if (length == 0) throw new IllegalArgumentException("The resulting array is empty");
        int count = 0;
        for (int i = 0; i < length; i++) {
            if (array[i].equals(value)) count++;
            else array[i - count] = array[i];
        }
        length -= count;
        array = Arrays.copyOf(array, length);
    }

    public T getMin() {
        if (length == 0) throw new IllegalArgumentException("The resulting array is empty");
        T min = array[0];
        for (int i = 0; i < length; i++) {
            if (this.array[i].compareTo(min) < 0) {
                min = array[i];
            }
        }
        return min;
    }

    public T getMax() {
        if (length == 0) throw new IllegalArgumentException("The resulting array is empty");
        T max = array[0];
        for (int i = 0; i < length; i++) {
            if (this.array[i].compareTo(max) > 0) {
                max = array[i];
            }
        }
        return max;
    }

    public Object sum() {
        if (length == 0) throw new IllegalArgumentException("The resulting array is empty");
        if (array[0] instanceof Number) {
            Number sum = 0;
            for (int i = 0; i < length; i++) sum = sum.doubleValue() + ((Number) array[i]).doubleValue();
            return sum;
        } else if (array[0] instanceof String) {
            StringBuilder sum = new StringBuilder();
            for (int i = 0; i < length; i++) sum.append((String) array [i]);
            return sum;
        }
        return null;
    }

    public Object multiplication() {
        if (length == 0) throw new IllegalArgumentException("The resulting array is empty");
        if (array[0] instanceof Number) {
            Number multiplication = 1;
            for (int i = 0; i < length; i++) {
                multiplication = multiplication.doubleValue() * ((Number) array[i]).doubleValue();
            }
            return multiplication;
        }
        return null;
    }


    public T get(int index) {
        if (0 > index || index >= length) {
            throw new IndexOutOfBoundsException("Index outside the array");
        }
        return this.array[index];
    }

    public boolean contains(T value) {
        for (int i = 0; i < this.length; i++) {
            if (this.array[i].equals(value)) return true;
        }
        return false;
    }

    public int getIndex(T value) {
        for (int i = 0; i < this.length; i++) {
            if (this.array[i].equals(value)) return i;
        }
        return -1;
    }

    public void print() {
        System.out.println(Arrays.toString(this.array));
    }

    public void set(int index, T value) {
        if (0 > index || index >= length) {
            throw new IndexOutOfBoundsException("Index outside the array");
        } else {
            this.array[index] = value;
        }
    }

    public void bubbleSort() {
        for (int i = 0; i < this.array.length; i++) {
            for (int j = 0; j < this.length - i - 1; j++) {
                if (this.array[j].compareTo(this.array[j + 1]) > 0) {
                    T temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                }
            }
        }
    }

    public void insertionSort() {
        for (int i = 1; i < length; i++) {
            T temp = array[i];
            int j = i - 1;
            while (j >= 0 && array[j].compareTo(temp) > 0) {
                array[j + 1] = array[j];
                j--;
            }
            array[j + 1] = temp;
        }
    }

    public void selectionSort() {
        for (int i = 0; i < length - 1; i++) {
            int minIndex = i;
            for (int j = i + 1; j < length; j++) {
                if (array[j].compareTo(array[minIndex]) < 0) {
                    minIndex = j;
                }
            }
            T temp = array[minIndex];
            array[minIndex] = array[i];
            array[i] = temp;
        }
    }
}