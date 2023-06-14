// Задайте двумерный массив. Напишите программу, которая заменяет строки на столбцы. 
//В случае, если это навозможно, программа должна вывеси сообщение для пользователя.

int rows = new Random().Next(1, 10);
int columns = new Random().Next(1, 10);
int[,] array = GetArray(rows, columns);

Console.Clear();
PrintArray(array);
if (rows == columns)
{
    Console.WriteLine();
    GetChangeArray(array);
    PrintArray(array);
}
else Console.WriteLine("Невозможно произвести замену");


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

static void GetChangeArray(int[,] array)  //Метод изменения массива
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = i; j < array.GetLength(1); j++)
        {
            int temp = array[i, j];
            array[i, j] = array[j, i];
            array[j, i] = temp;
            //Console.WriteLine($"{array[i, j]}  {array[j, i]}" );
        }
    }
}
