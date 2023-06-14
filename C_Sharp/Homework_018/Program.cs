//Напишите программу, которая на вход принимает число (N), а на выходе показывает все четные числа от 1 до N

Console.Write("Введите число: ");
string userInput = Console.ReadLine() ?? "";
int N = int.Parse(userInput);
int x = 1;

Console.Write(N + " -> ");

while (x <= N)
    if (x%2==0)
    {
        Console.Write(x);
        if(N%2==0)
        {
            if(x < N)
            {
                Console.Write(", ");
            }
        }
        else
        {
            if(x < N -1)
            {
                Console.Write(", ");
            }
        }
        x += 1;
    }
    else
    {
        x +=1;
    }
