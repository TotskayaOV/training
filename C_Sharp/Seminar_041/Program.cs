//Напишите программу, которая принимает на вход число (А) и выдает сумму чисел от 1 до А

Console.Clear();
int num = GetNumberFromUser("Введите целое число А: ", "Ошибка ввода!");
int sumNumbers = GetSumNumbers(num);
Console.WriteLine($"{num} -> {sumNumbers}");

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
int GetSumNumbers(int number)
{
    int sum = 0;
    while(number > 0)
    {
        sum += number;
        number--;
    }
    return sum;
}
