//  Задайте прямоугольный двумерный массив. 
// Напишите программу, которая будет находить строку с наименьшей суммой элементов.

int rows= new Random().Next(1, 10);
int columns = new Random().Next(1, 10);
int[,] array = GetArray(rows, columns);
Console.Clear();
PrintArray(array);
Console.WriteLine();
int[] resultArray = GetMinSummRow(array);
Console.WriteLine($"В строке № {resultArray[0]} наименьшая сумма элементов ({resultArray[1]}) среди прочих строк массива.");


void PrintArray(int[,] inArray)  //Метод вывода массива
{
    for (int i = 0; i < inArray.GetLength(0); i++)
    {
        for (int j = 0; j < inArray.GetLength(1); j++)
        {
            Console.Write($"{inArray[i, j]} ");
        }
        Console.WriteLine();
    }
}

int[,] GetArray(int m, int n)   //Метод создания массива
{
    int[,] result = new int[m, n];
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            result[i, j] = new Random().Next(0, 10); 
         }
    }
    return result;
}

static int[] GetMinSummRow(int[,] array)    //Метод поиска наименьшего
{
    int[] result = new int[2];
    result[1] = array[0, 0];

    for (int j = 1; j < array.GetLength(1); j++)
    {
        result[1] += array[0, j];
    }

    for (int i = 1; i < array.GetLength(0); i++)
    {
        int sum = array[i, 0];
        for (int j = 1; j < array.GetLength(1); j++)
        {
            sum += array[i, j];
        }

        if (sum < result[1])
        {
            result[1] = sum;
            result[0] = i + 1;
        }
    }
    return result;
}