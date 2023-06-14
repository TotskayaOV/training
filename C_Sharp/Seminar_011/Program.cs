Console.WriteLine("Напишите целое число: ");

string userInput = Console.ReadLine() ?? "";

int userNumber = int.Parse (userInput);

Console.WriteLine (userNumber + " -> " + userNumber * userNumber);

