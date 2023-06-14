static void Quarter(int quarter)
{
    if (quarter == 1)
        Console.Write ("x > 0, y > 0");
    else if (quarter == 2)
        Console.Write ("x < 0, y > 0");
    else if (quarter == 3)
        Console.Write ("x < 0, y < 0");
    else if (quarter == 4)
        Console.Write ("x > 0, y < 0");
    else
        Console.WriteLine("Некорректно введена четверть");
}

// int EnterNumber()
// {
//     int number;
//     while (true)
//     {
//         Console.Write("Введите число: ");
//         if (int.TryParse(Console.ReadLine(), out number))
//             break;
//         Console.WriteLine($"Ошибка ввода!");
//     }
//     return number;
// }

// int firstNumber = EnterNumber();
// int secondNumber = EnterNumber();

// //Console.Write("Введите первое число: ");
// //int firstNumber = int.Parse(Console.ReadLine() ?? "");
// //Console.Write("Введите второе число: ");
// //int secondNumber = int.Parse(Console.ReadLine() ?? "");
int quarter;

Console.Write("Введите номер четверти: ");
quarter = int.Parse(Console.ReadLine() ?? "");

Quarter(quarter);