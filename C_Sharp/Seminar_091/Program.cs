// Задайте значение N. Напишите программу, которая выведет все натуральные числа в промежутке от 1 до N

Console.Write("Введите число: ");
int n = int.Parse(Console.ReadLine() ?? "");
Console.WriteLine(PrintNaturals(1, n));


string PrintNaturals(int start, int end)
{
    if(start == end)
    {
        return start.ToString();
    }
    return (start + ", " + PrintNaturals(start + 1, end));
}