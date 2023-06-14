// Задайте двумерный массив. Напишите программу, которая упорядочит по убыванию элементы каждой строки 
// двумерного массива.

int rows= new Random().Next(1, 10);
int columns = new Random().Next(1, 10);
int[,] array = GetArray(rows, columns);

Console.Clear();
PrintArray(array);
Console.WriteLine();
ArrayCollating(array);
PrintArray(array);


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

static void ArrayCollating(int[,] array)  //Метод упорядочивания строк
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int timing = 0; timing < array.GetLength(1); timing++)
        {
            for (int j = 0; j < array.GetLength(1) - 1 - timing; j++)
            {
                if (array[i, j] < array[i, j + 1])
                {
                    int temp = array[i, j];
                    array[i, j] = array[i, j + 1];
                    array[i, j + 1] = temp;
                }
            }
        }
    }
}
