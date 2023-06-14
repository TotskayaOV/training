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

int a1 = EnterNumber();
int a2 = EnterNumber();

Console.Clear();
Console.Write($"{a1}, {a2} -> ");

if(a1 == Math.Pow(a2, 2))
    Console.WriteLine($"да");
else if (a2 == Math.Pow(a1, 2))
    Console.WriteLine($"да");
else
    Console.WriteLine($"нет");