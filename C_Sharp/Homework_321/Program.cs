int x1 , x2, x3, y1, y2, y3;

x1 = Koords("Введите координату х первого числа: ");
x2 = Koords("Введите координату y первого числа: ");
x3 = Koords("Введите координату z первого числа: ");
y1 = Koords("Введите координату x второго числа: ");
y2 = Koords("Введите координату y второго числа: ");
y3 = Koords("Введите координату z второго числа: ");

double distance = Distance(x1, x2, x3, y1, y2, y3);
Console.WriteLine(distance);

static int Koords(string message)   
{
    Console.Write(message);
    int res = int.Parse(Console.ReadLine() ?? ""); 
    return res;                     
}

static double Distance(int x1, int x2, int x3, int y1, int y2, int y3)  
{
    double res = Math.Sqrt(Math.Pow(x1 - y1, 2) + Math.Pow(x2 - y2, 2) + Math.Pow(x3 - y3, 2));
    return res;                                         
}