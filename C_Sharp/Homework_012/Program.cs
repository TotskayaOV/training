// Напишите программу, которая на вход принимает два числа и выдает, какое число большее, а какое меньшее

Console.Write("Введите первое число: ");
string userInput1 = Console.ReadLine() ?? "";
int userNumber1 = int.Parse(userInput1);

Console.Write("Введите второе число: ");
string userInput2 = Console.ReadLine() ?? "";
int userNumber2 = int.Parse(userInput2);

if (userNumber2 > userNumber1)
{
    Console.WriteLine(userNumber1 + " меньше чем " + userNumber2);
}
else if (userNumber2 < userNumber1)
{
    Console.WriteLine(userNumber2 + " меньше чем " + userNumber1);
}
else
    Console.WriteLine(userNumber1 + " равно " + userNumber2);