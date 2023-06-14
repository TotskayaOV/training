//Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, 
//является ли этот день выходным.

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

int num1 = EnterNumber();

if (5 < num1 && num1 < 8)
    Console.WriteLine($"{num1} -> да");
else if (num1 < 6)
    Console.WriteLine($"{num1} -> нет");
else if (7 < num1)
    Console.WriteLine($"Ошибка ввода!");