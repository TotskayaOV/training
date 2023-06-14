// Напишите программу, которая принимает на вход число и выдаёт количество цифр в числе.

Console.Clear();
int num = GetNumberFromUser("Введите целое число А: ", "Ошибка ввода!");
int count = GetCountNumbers(num);
Console.WriteLine($"{num} -> {count}");

int GetNumberFromUser(string message, string errorMessage)  //проверка корректности ввода
{
    while(true)     //бесконечный цикл за счет true, выполняется пока не будет корректный ввод
    {
        Console.Write(message);
        bool isCorrect = int.TryParse(Console.ReadLine(), out int userNumber);
        if(isCorrect)       //в bool проводится проверка на true, если true, то ветвь if
            return userNumber;
        Console.WriteLine(errorMessage);
    }
}

int GetCountNumbers(int number)
{
    int count = 0;
    while(number > 0)
    {
        number = number / 10;
        count++;
    }
    return count;
}