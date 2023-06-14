Console.Write("Введите число: ");
string userInput1 = Console.ReadLine() ?? "";
int a1 = int.Parse(userInput1);

int a2 = 23;
int a3 = 7;

int a4 = a1 % a2;
if(a4 == 0)
{    
    int a5 = a1 % a3;
    if(a5 == 0)
        Console.WriteLine($"число {a1} кратно числу {a3} и числу {a2}");
}
else
    Console.WriteLine($"число {a1} не кратно числу {a3} и числу {a2}");