Console.Write("Введите первое число: ");
string userInput1 = Console.ReadLine() ?? "";
int userNumber1 = int.Parse(userInput1);

Console.Write("Введите второе число: ");
string userInput2 = Console.ReadLine() ?? "";
int userNumber2 = int.Parse(userInput2);

if (userNumber2 * userNumber2 == userNumber1)
{
    Console.WriteLine("a=" + userNumber1 + ", b=" + userNumber2 + "-> ДА");
}
else 
    Console.WriteLine("a=" + userNumber1 + ", b=" + userNumber2 + "-> НЕТ");