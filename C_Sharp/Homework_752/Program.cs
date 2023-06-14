// Задайте двумерный массив из целых чисел. Найдите среднее арифметическое элементов в каждом столбце

int rows= 3;
int columns = 4;
int[,] array = GetArray(rows, columns);

double res1 = Math.Round(ModArray(array, 0) / (double)rows, 1);
double res2 = Math.Round(ModArray(array, 1) / (double)rows, 1);
double res3 = Math.Round(ModArray(array, 2) / (double)rows, 1);
double res4 = Math.Round(ModArray(array, 3) / (double)rows, 1);

Console.Clear();
PrintArray(array);
Console.WriteLine($"{res1} {res2} {res3} {res4}.");

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

double ModArray(int[,] array, int num)
{
    double result = 0;
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            if (j == num) result += array[i, j];                        
        }
    }
    return result;
}