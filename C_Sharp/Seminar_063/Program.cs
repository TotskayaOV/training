// напишите программу, которая будет преобразовывать десятичное число в двоичное

Console.Clear();
int number = GetNumberFromUser("Введите число: ", "Ошибка ввода!");
string finish = TransformNumbers(number);
Console.WriteLine($"{number} - > {finish}");


string TransformNumbers(int N)
{
    string TransformNumbers = "";
    while(N > 0)
    {
        int count = N % 2;
        TransformNumbers = count + TransformNumbers;
        N = N / 2;
    }
    return TransformNumbers;
}
// int[] ArrayForNumbers(int size)
// {
//     size = 1;
//     for (int i = 0; i > 0; i++)
//     {
//         a = number % 2;
//         b = number - a;
//         return size++;
//         return   
//     }


static int GetNumberFromUser(string message, string errorMessage)   //Метод для ввода данных
{
    Console.Write(message);
    int res = int.Parse(Console.ReadLine()); //ввод с консоли и присваивание этого числа res
    return res;                     // возвращает значения
}

