// Напишите программу, которая принимает на вход три числа и проверяет, может ли существовать треугольник
//со сторонами такой длины.

int sideA = GetNumberFromUser("Введите длинну первой стороны треугольника: ", "Ошибка ввода!");
int sideB = GetNumberFromUser("Введите длинну второй стороны треугольника: ", "Ошибка ввода!");
int sideC = GetNumberFromUser("Введите длинну третьей стороны треугольника: ", "Ошибка ввода!");

if (ResultForNum(sideA, sideB, sideC) == true && ResultForNum(sideB, sideA, sideC) == true && ResultForNum(sideC, sideB, sideA) == true)
{
    Console.WriteLine($"Треугольник со сторонами {sideA}, {sideB}, {sideC} существовать может");
}
else Console.WriteLine($"Треугольник со сторонами {sideA}, {sideB}, {sideC} существовать не может");


static int GetNumberFromUser(string message, string errorMessage)   //Метод для ввода данных
{
    Console.Write(message);
    int res = int.Parse(Console.ReadLine()); //ввод с консоли и присваивание этого числа res
    return res;                     // возвращает значения
}

bool ResultForNum(int a, int b, int c)
{
    return a + b > c;
}
