// Напишите программу замены элементов массива: положительные элементы замените
//на соответствующие отрицательные, и наоборот

Console.Clear();
int size = GetNumberFromUser("Введите размер массива: ", "Ошибка ввода!");
int minValue = GetNumberFromUser("Введите минимальное значение массива: ", "Ошибка ввода!");
int maxValue = GetNumberFromUser("Введите максимальное значение массива: ", "Ошибка ввода!");
int[] array = GetArray(size, minValue, maxValue);      //создание пустого массива с диапозоном заданных значений
PrintArray(array);  //вывод массива
Console.Write(" -> ");
ArrayElementSwap(array);
PrintArray(array);


static int GetNumberFromUser(string message, string errorMessage)   //Метод для ввода массива
{
    Console.Write(message);
    int res = int.Parse(Console.ReadLine()); //ввод с консоли и присваивание этого числа res
    return res;                     // возвращает значения координат
}

static void PrintArray(int[] array)        //метод вывода массива
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

static void ArrayElementSwap(int[] array)
{
    for (int i = 0; i < array.Length; i++)
    {
        array[i] = array[i] * (-1);
    }
}