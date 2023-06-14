// Напишите программу, которая заполнит спирально массив 4 на 4.


int rows= 4;
int columns = 4;
int[,] array = GetArray(rows, columns);
Console.Clear();
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
            if (i == 0) result[i, j] = j + 1;
            if (j == 3) result[i, j] = j + 1 + i;
            if (i == 3) result[i, j] = 13 - i - j;
            if (i == 1 & j < 3) result[i, j] = 12 + j;
            if (i == 2) 
            {
                result[i, 0] = 11;
                result[i, 1] = 11 + result[i, 3] - 1;
                result[i, 2] = 11 + result[i, 3] - 2;
            }
        }
    }
    return result;
}