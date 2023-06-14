// Задайте две матрицы. Напишите программу, которая будет находить произведение двух матриц.

int rows= 2;
int columns = 2;
int[,] array1 = GetArray(rows, columns);
int[,] array2 = GetArray(rows, columns);
int[,] multiplicationArray = GetArrayMultiplication(array1, array2);
Console.Clear();
Console.WriteLine("Первая матрица: ");
PrintArray(array1);
Console.WriteLine("Вторая матрица: ");
PrintArray(array2);
Console.WriteLine("Произведение двух матриц:");
PrintArray(multiplicationArray);

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

static int[,] GetArrayMultiplication(int[,] firstArray, int[,] secondArray) //Метод произведения
{
    int[,] resultArray = new int[firstArray.GetLength(0), secondArray.GetLength(1)];

    for (int i = 0; i < firstArray.GetLength(0); i++)
    {
        for (int j = 0; j < secondArray.GetLength(1); j++)
        {
            for (int k = 0; k < firstArray.GetLength(1); k++)
            {
                resultArray[i, j] += firstArray[i, k] * secondArray[k, j];
            }
        }
    }
    return resultArray;
}
