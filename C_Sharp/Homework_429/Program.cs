// Напишите программу, которая задает массив из 8 элементов и выводит их на экран

Console.Clear();
int[] array = new int[8];


for (int i = 0; i < array.Length; i++)
{
    array[i] = EnterNumber();
}

Console.Write("[ ");

for (int i = 0; i < array.Length; i++)
{
    Console.Write($"{array[i]} ");
}
Console.Write("]");

int EnterNumber()
{
    int number;
    while (true)
    {
        Console.Write("Введите число: ");
        if (int.TryParse(Console.ReadLine(), out number))
            break;
        Console.WriteLine($"Ошибка ввода!");
    }
    return number;
}