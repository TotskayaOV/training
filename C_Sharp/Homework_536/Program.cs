// Задайте одномерный массив, заполненный случайными числами. Найдите сумму элементов, стоящих на нечётных позициях.

Console.Clear();
int size = GetNumberFromUser("Введите размер массива: ", "Ошибка ввода!");
int minValue = GetNumberFromUser("Введите минимальное значение массива: ", "Ошибка ввода!");
int maxValue = GetNumberFromUser("Введите максимальное значение массива: ", "Ошибка ввода!");
int[] array = GetArray(size, minValue, maxValue);      
int summ = SummNumArray(array);
Console.Write("[ ");
PrintArray(array);  
Console.Write($"] -> {summ}");

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
    while(true)     
    {
        Console.Write(message);
        bool isCorrect = int.TryParse(Console.ReadLine(), out int userNumber);
        if(isCorrect)       
            return userNumber;
        Console.WriteLine(errorMessage);
    }
}

int SummNumArray(int[] array)       //метод нахождения суммы
{
    int summ = 0;
    for (int i = 0; i < array.Length; i=i+2)
    {
        summ = summ + array[i];
    }
    return summ;
}
