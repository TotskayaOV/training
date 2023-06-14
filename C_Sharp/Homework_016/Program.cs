//Напишите программу, которая на вход принимает число и выдаёт, является ли число чётным.

Console.Write("Введите число: ");
string userInput = Console.ReadLine() ?? "";
double a = double.Parse(userInput);

if (a%2 == 0)
{
    Console.WriteLine( a + " - четное" );
}
else 
{
    Console.WriteLine( a + " - нечетное" );
}