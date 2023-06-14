int num = new Random().Next(100, 1000);
Console.WriteLine(num);
int a1 = num/100;
int a2 = num%10;
Console.WriteLine($"{a1}  {a2}");
int a3 = a1*10;
int a4 = a3 + a2;
Console.WriteLine(a4);