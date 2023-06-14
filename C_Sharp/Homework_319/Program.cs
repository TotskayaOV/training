Console.Write("Введите число: ");
int N = int.Parse(Console.ReadLine() ?? "");

Console.Write($"{N} -> ");


int a1 = N / 10000;
int a2 = N / 1000 % 10;
int a3 = N % 10;
int a4 = N % 100 /10;

if (a1 == a3)
{
    if (a2 == a4)
        Console.Write("да");
}
else
    Console.Write("нет");