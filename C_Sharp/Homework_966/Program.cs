// Задайте значения M и N. Напишите программу, которая найдёт сумму натуральных элементов в промежутке от M до N.

Console.Write("Введите число M: ");
int m = int.Parse(Console.ReadLine() ?? "");
Console.Write("Введите число N: ");
int n = int.Parse(Console.ReadLine() ?? "");
Console.Write(PrintNaturals(m, n, 0));

int PrintNaturals(int start, int end, int summ)
{
    if(start > end)
    {
        return summ;
    }
    return(PrintNaturals(start+1, end, summ + start));
}