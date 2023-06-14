//Напишите программу, которая выводит третью цифру заданного числа или сообщает, что третьей цифры нет.

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

Console.Clear();
Console.Write($"{num1} -> ");

if  (num1 < 100)            //вывод при длинне числа меньше 3
{
 Console.WriteLine($"третьей цифры нет");
}
else
{
    int num2 = num1;        //определяем длинну числа
    int count = 0;
    while (num2 > 0)
    {
        num2 = num2 / 10;
        count = count + 1;
    }

    count = count - 2;
    double then1 = Math.Pow(10, count);     //возведение делителя в степень

    int num3 = num1 % (int)then1;
    int num4 = num3 / (int)(then1 / 10);

    Console.Write(num4);
}