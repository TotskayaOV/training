// Задайте массив вещественных чисел. Найдите разницу между максимальным и минимальным элементов массива.

int size = GetNumberFromUser("Введите размер массива: ", "Ошибка ввода!");
int beforedesjat = GetNumberFromUser("Введите количество цифр перед запятой: ", "Ошибка ввода!");
int afterdesjat = GetNumberFromUser("Введите количество цифр после запятой: ", "Ошибка ввода!");
Console.Clear();
double[] array = GetArray(size);      
double maximumNum = MaxNumber(array);
double minimumNum = MinNumber(array);
double subNum = SubtractingNumber(maximumNum, minimumNum);
Console.Write("[ ");
PrintArray(array);  
Console.Write($"] -> {subNum}");

void PrintArray(double[] array)        //метод вывода массива
{
    for (int i = 0; i < array.Length; i++)
    {
        Console.Write(array[i] + " ");
    }
}

double[] GetArray(int size)        //метод создания массива
{
    double[] res = new double[size];

    for (int i = 0; i < size; i++)
    {
        res[i] = new Random().NextDouble();
        res[i] = res[i] * Math.Pow(10, beforedesjat);
        res[i] = Math.Round(res[i], afterdesjat);
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

double MaxNumber(double[] array)        //метод нахождения максимального
{
    double maximumNum = array[0];
    for (int i = 0; i < array.Length; i++)
    {
        if (maximumNum < array[i]) maximumNum = array[i];       
    }  
    return maximumNum;
}

double MinNumber(double[] array)        //метод нахождения минимального
{
    double minimumNum = array[0];
    for (int i = 0; i < array.Length; i++)
    {
        if (minimumNum > array[i]) minimumNum = array[i];       
    }  
    return minimumNum;
}

double SubtractingNumber(double maximumNum, double minimumNum)  //метод вычитания
{
    double result = maximumNum - minimumNum;
    return result;
}