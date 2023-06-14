//Напишите программу, которая принимает на вход три числа и выдаёт максимальное из этих чисел

Console.Write("Введите первое число: ");
string userInput1 = Console.ReadLine() ?? "";
int userNumber1 = int.Parse(userInput1);

Console.Write("Введите второе число: ");
string userInput2 = Console.ReadLine() ?? "";
int userNumber2 = int.Parse(userInput2);

Console.Write("Введите третье число: ");
string userInput3 = Console.ReadLine() ?? "";
int userNumber3 = int.Parse(userInput3);

int max = userNumber1;

if (max < userNumber2)
{
    max = userNumber2;
}
else if (max < userNumber3)
{
    max = userNumber3;
}

Console.WriteLine("максимальное число: " + max);