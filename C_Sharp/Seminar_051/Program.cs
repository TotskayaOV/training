// Задать массив из 12 элементов, который будет заполнен случайныи значениями из промежутка от -9 до 9. 
// Найти сумму отрицательных и положительных элементов массива

int[] array = GetArray(12, -9, 9);      //создание пустого массива с диапозоном заданных значений

PrintArray(array);  //вывод массива

int negativeSum = GetNegativeSum(array);
Console.WriteLine($"\nСумма отрицательных чисел массива равна {negativeSum}");
int positiveSum = GetPositiveSum(array);
Console.WriteLine($"Сумма положительных чисел массива равна {positiveSum}"); //убрано \n чтобы не было пробела между строками

void PrintArray(int[] array)        //метод вывода массива
{
    for (int i = 0; i < array.Length; i++)
    {
        Console.Write(array[i] + " ");
    }
}

int GetNegativeSum(int[] array)     //метод суммирования отрицательных значений
{
    int negativeSum = 0;
    foreach(int el in array)
    {
        if(el<0) negativeSum+=el;
    }
    return negativeSum;
}

int GetPositiveSum(int[] array)     //метод суммирования положительных значений
{
    int positiveSum = 0;
    foreach(int el in array)
    {
        if(el>0) positiveSum+=el;
    }
    return positiveSum;
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