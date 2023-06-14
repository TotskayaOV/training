// Задайте массив заполненный случайными положительными трёхзначными числами. Напишите программу, которая покажет количество чётных чисел в массиве.
//[345, 897, 568, 234] -> 2

Console.Clear();
int size = GetNumberFromUser("Введите размер массива: ", "Ошибка ввода!");
int[] array = GetArray(size);
int count = CountArray(array);
Console.Write("[ ");
PrintArray(array);
Console.Write($"] -> {count}");


void PrintArray(int[] array)        //метод вывода массива
{
    for (int i = 0; i < array.Length; i++)
    {
        Console.Write(array[i] + " ");
    }
}

int GetNumberFromUser(string message, string errorMessage)  //метод ввода числа
{
    while(true)     
    {
        Console.Write(message);
        bool isCorrect = int.TryParse(Console.ReadLine(), out int userNumber);
        if(isCorrect)       
            return userNumber;
        Console.WriteLine(errorMessage);
    }
}

int[] GetArray(int size)        //метод создания массива
{
    int[] res = new int[size];

    for (int i = 0; i < size; i++)
    {
        res[i] = new Random().Next(100, 1000);
    }

    return res;
}

int CountArray(int[] array)     //вычисление количества четных чисел
{
    int count = 0;
    int j = 0;
    while (j < array.Length)
    {
        int x = array[j] % 2;
        if(x == 0)
        {
            count++;
        }
        j++;
    }
    return count;
}