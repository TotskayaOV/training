// Задайте двумерный массив размером m×n, заполненный случайными вещественными числами.

Console.Clear();
int rows = GetNumberFromUser("Введите количество строк: ", "Ошибка ввода!");
int columns = GetNumberFromUser("Введите количество столбцов: ", "Ошибка ввода!");


double[,] array = GetArray(rows, columns, 0, 10);
PrintArray(array);



static int GetNumberFromUser(string message, string errorMessage)   //Метод для ввода данных
{
    Console.Write(message);
    int res = int.Parse(Console.ReadLine()); //ввод с консоли и присваивание этого числа res
    return res;                     // возвращает значения
}

void PrintArray(double[,] inArray)  //Метод вывода массива
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


double[,] GetArray(int m, int n, int minValue, int maxValue)    //Метод заполнения массива случайными вещественными числами
{
    double[,] result = new double[m, n];
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            result[i, j] = Math.Round(new Random().NextDouble() * 10, 1); 
         }
    }
    return result;
}
