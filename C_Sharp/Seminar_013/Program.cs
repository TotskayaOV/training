Console.Write("Введите порядковый номер дня недели: ");
string userInput = Console.ReadLine() ?? "";
int userNumber = int.Parse(userInput);

if (userNumber == 1)
{
    Console.WriteLine("1 -> Понедельник");
}

else if (userNumber == 2)
{
    Console.WriteLine("2 -> Вторник");
}

else if (userNumber == 3)
{
    Console.WriteLine("3 -> Среда");
}

else if (userNumber == 4)
{
    Console.WriteLine("4 -> Четверг");
}

else if (userNumber == 5)
{
    Console.WriteLine("5 -> Пятница");
}

else if (userNumber == 6)
{
    Console.WriteLine("6 -> Суббота");
}

else if (userNumber == 7)
{
    Console.WriteLine("7 -> Воскресенье");
}

else
    Console.WriteLine("Введите порядковый номер дня земной недели");