// Напишите программу, которая принимает на вход число N и выдаёт произведение чисел от 1 до N

Console.Clear();
int num = GetNumberFromUser("Введите целое число N: ", "Ошибка ввода!");
int incNumbers = GetIncreaseNumbers(num);
Console.WriteLine($"{num} -> {incNumbers}");

int GetNumberFromUser(string message, string errorMessage)
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

// Возвращает сумму чисел от 1 до number
int GetIncreaseNumbers(int number)
{
    int increase = 1;
    while(number > 0)
    {
        increase = increase * number;
        number--;
    }
    return increase;
}