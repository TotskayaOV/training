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

//Console.Write("Введите первое число: ");
//int a1 = int.Parse(Console.ReadLine() ?? "");
//Console.Write("Введите второе число: ");
//int a2 = int.Parse(Console.ReadLine() ?? "");

Console.Clear();
Console.Write($"{a1}, {a2} -> ");


int a3 = a1 % a2;
if(a3==0)
    Console.WriteLine($"число {a1} кратно числу {a2}");
else
    Console.WriteLine($"число {a1} не кратно числу {a2}, остаток от деления: {a3}");
