// Реализовать алгоритм сортировки слиянием
package Homewrok3;

import java.util.Arrays;

public class task1 {
    public static int[] mergeSort(int[] sortArr) {
        int[] temp1 = Arrays.copyOf(sortArr, sortArr.length);
        int[] temp2 = new int[sortArr.length];
        int[] result = mergeSortInner(temp1, temp2, 0, sortArr.length);
        return result;
    }

    public static int[] mergeSortInner(int[] buffer1, int[] buffer2, int startIndex, int endIndex) {
        if (startIndex >= endIndex - 1) {
            return buffer1;
        }

        int middle = startIndex + (endIndex - startIndex) / 2;
        int[] sorted1 = mergeSortInner(buffer1, buffer2, startIndex, middle);
        int[] sorted2 = mergeSortInner(buffer1, buffer2, middle, endIndex);

        int index1 = startIndex;
        int index2 = middle;
        int newIndex = startIndex;
        int[] result = sorted1 == buffer1 ? buffer2 : buffer1;
        while (index1 < middle && index2 < endIndex) {
            result[newIndex++] = sorted1[index1] < sorted2[index2]
                    ? sorted1[index1++] : sorted2[index2++];
        }
        while (index1 < middle) {
            result[newIndex++] = sorted1[index1++];
        }
        while (index2 < endIndex) {
            result[newIndex++] = sorted2[index2++];
        }
        return result;
    }
    public static void main(String args[]) {
        int[] sortArr = {2, 7, 3, 9, 1, 10, 8, 37};
        int[] result = mergeSort(sortArr);
        System.out.println(Arrays.toString(result));
    }
}