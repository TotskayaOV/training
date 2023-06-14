// Напишите программу, которая найдет точку пересечения двух прямых, заданных уровнениями y=k1*x+b1, y=k2*x+b2;
//значения b1, k1, b2 и k2 задаются пользователем

double b1 = GetNumberFromUser("Введите b1: ", "Ошибка ввода!");
double k1 = GetNumberFromUser("Введите k1: ", "Ошибка ввода!");
double b2 = GetNumberFromUser("Введите b2: ", "Ошибка ввода!");
double k2 = GetNumberFromUser("Введите k2: ", "Ошибка ввода!");
Console.Clear();
double x = (b2 - b1) / (k1 - k2);
double y = k1 * x + b1;
Console.WriteLine($"b1={b1}, k1={k1}, b2={b2}, k2={k2} -> ({x}, {y})");

static double GetNumberFromUser(string message, string errorMessage)   //Метод для ввода данных
{
    Console.Write(message);
    double res = double.Parse(Console.ReadLine()); //ввод с консоли и присваивание этого числа res
    return res;                     // возвращает значения
}

