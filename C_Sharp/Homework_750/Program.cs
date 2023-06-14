// Напишите программу, которая на вход принимает позиции элемента в двумерном массиве, 
// и возвращает значение этого элемента или же указание, что такого элемента нет.

int rows= 3;
int columns = 4;
int[,] array = GetArray(rows, columns);
int index0 = GetNumberFromUser("Введите номер строки нужного элемента: ", "Ошибка ввода!") - 1;
int index1 = GetNumberFromUser("Введите номер столбца нужного элемента: ", "Ошибка ввода!") - 1;

Console.Clear();
PrintArray(array);
Console.WriteLine();
PrintResult(array);


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

static int GetNumberFromUser(string message, string errorMessage)   //Метод для ввода данных
{
    Console.Write(message);
    int res = int.Parse(Console.ReadLine()); //ввод с консоли и присваивание этого числа res
    return res;                     // возвращает значения
}

void PrintResult(int[,] array)  //Метод поиска числа и вывода результата
{
    if (index0<array.GetLength(0) && index1<array.GetLength(1)) 
    {
        int result = array[index0, index1];
        Console.WriteLine($"В {index0+1} строке {index1+1} столбце расположено число {result}.");
    }
    else Console.WriteLine("В данной таблице такого числа нет.");
}