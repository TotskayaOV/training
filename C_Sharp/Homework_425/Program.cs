// Напишите цикл, который принимает на вход два числа (А и В) и возводит число А в натуральную степень В # 3, 5 -> 243

Console.Clear();
int num = GetNumberFromUser("Введите целое число А: ", "Ошибка ввода!");
int count = GetNumberFromUser("Введите целое число В: ", "Ошибка ввода!");
int multNumbers = GetMultNumbers();
Console.WriteLine($"{num}, {count} -> {multNumbers}");

int GetNumberFromUser(string message, string errorMessage)
{
    while(true)     
    {
        Console.Write(message);
        bool isCorrect = int.TryParse(Console.ReadLine(), out int userNumber);
        if(isCorrect)       
            return userNumber;
        Console.WriteLine(errorMessage);
    }
}

int GetMultNumbers()
{
    int number = 1;
    int power = num;
    while(number < count)
    {
        power = power * num;
        number++;
    }
    return power;
}