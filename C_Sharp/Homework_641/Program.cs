// Пользователь вводит с клавиатуры М чисел. Посчитайте сколько чисел больше 0 ввел пользователь

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
        res[i] = GetNumberFromUser("Введите число: ", "Ошибка ввода!");;
    }
    
    return res;
}

int CountArray(int[] array)     //вычисление количества положительных чисел
{
    int count = 0;
    int j = 0;
    while (j < array.Length)
    {
        if(array[j] > 0) count++;
        j++;
    }
    return count;
}




