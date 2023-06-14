// Напишите программу вычисления функции Аккермана с помощью рекурсии. Даны два неотрицательных числа m и n.

Console.Write("Введите число M: ");
int m = int.Parse(Console.ReadLine() ?? "");
Console.Write("Введите число N: ");
int n = int.Parse(Console.ReadLine() ?? "");
Console.WriteLine(MethAkker(m, n));


static int MethAkker (int n, int m)
{
  if (n == 0)
    return m + 1;
  else
    if ((n != 0) && (m == 0))
      return MethAkker(n - 1, 1);
    else
      return MethAkker(n - 1, MethAkker(n, m - 1));
}