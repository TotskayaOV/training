// Задайте значение N. Напишите программу, которая выведет все натуральные числа в промежутке от N до 1

Console.Write("Введите число N: ");
int n = int.Parse(Console.ReadLine() ?? "");

Console.WriteLine(PrintNaturals(n, 1));

string PrintNaturals(int start, int end)
{
    if(start == end)
    {
        return start.ToString();
    }
    return (start + ", " + PrintNaturals(start - 1, end));
}