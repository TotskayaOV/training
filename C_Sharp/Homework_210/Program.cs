//Напишите программу, которая принимает на вход трехзначное число и на выходе показывает вторую цифру этого числа

int EnterNumber()
{
    int number;
    while (true)
    {
        Console.Write("Введите число: ");
        if (int.TryParse(Console.ReadLine(), out number))
            if  (99 < number && number < 1000)
            break;
        Console.WriteLine($"Ошибка ввода!");
    }
    return number;
}

int num1 = EnterNumber();

Console.Clear();
Console.Write($"{num1} -> ");

int num2 = num1 % 100;
int num3 = num2 / 10;

Console.Write(num3);