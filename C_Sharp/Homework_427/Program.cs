// Напишите программу, которая принимает на вход число и выдаёт сумму цифр в числе # 452 -> 11

int userNumber = EnterNumber();
int sum = AddingNumbers();

Console.Write($"{userNumber} -> {sum}");

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

int AddingNumbers()
{
    int sum = 0;
    int number = userNumber;
    while (number > 0)
    {
        sum = sum + number % 10;
        number = number / 10;
    }
    return sum;
}