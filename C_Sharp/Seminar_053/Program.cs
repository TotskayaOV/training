// Задайте массив. Напишите программу, которая определяет присутствует ли заданное число в массиве.

Console.Clear();
int num = GetNumberFromUser("Введите число: ", "Ошибка ввода!");
int size = GetNumberFromUser("Введите размер массива: ", "Ошибка ввода!");
int minValue = GetNumberFromUser("Введите минимальное значение массива: ", "Ошибка ввода!");
int maxValue = GetNumberFromUser("Введите максимальное значение массива: ", "Ошибка ввода!");
int[] array = GetArray(size, minValue, maxValue);      //создание пустого массива с диапозоном заданных значений
Console.Write($"{num}; ");
PrintArray(array);  //вывод массива
bool res = PrintResult(array, num);

if (res) Console.Write(" -> yes");
else Console.Write(" -> no");

void PrintArray(int[] array)        //метод вывода массива
{
    for (int i = 0; i < array.Length; i++)
    {
        Console.Write(array[i] + " ");
    }
}
int[] GetArray(int size, int minValue, int maxValue)        //метод создания массива
{
    int[] res = new int[size];

    for (int i = 0; i < size; i++)
    {
        res[i] = new Random().Next(minValue, maxValue+1);
    }

    return res;
}
int GetNumberFromUser(string message, string errorMessage)  //метод ввода числа
{
    while(true)     //бесконечный цикл за счет true, выполняется пока не будет корректный ввод
    {
        Console.Write(message);
        bool isCorrect = int.TryParse(Console.ReadLine(), out int userNumber);
        if(isCorrect)       //в bool проводится проверка на true, если true, то ветвь if
            return userNumber;
        Console.WriteLine(errorMessage);
    }
}
bool PrintResult(int[] array, int num)        //метод вывода результата
{
    foreach (int element in array)
    {
        if (element == num) return true;       
    }
    return false;
}
    