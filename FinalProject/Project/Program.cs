// Написать программу, которая из имеющегося массива строк формирует массив из строк, длина которых меньше 
// либо равна 3 символа. Первоначальный массив можно ввести с клавиатуры,  либо задать на старте выполнения 
// алгоритма. При решении не рекомендуется пользоваться коллекциями, лучше обойтись исключительно массивам/

string[] arrayProject = new string[6] { "Hello", "this", "is", "Final", "Project", ":)" };
string[] arrayResult =  GetArray(arrayProject);
PrintArray(arrayResult);

string[] GetArray(string[] array)
{
    int count = 0;
    int temp = 0;
    for (int i = 0; i < array.Length; i++)
    {
        if (array[i].Length <= 3) count++;
    }
    string[] array2 = new string[count];
    for (int j = 0; j < array.Length; j++)
    {
        if (array[j].Length <= 3)
        {
            array2[temp] = array[j];
            temp++;
        }
    }
    return array2;
}

void PrintArray(string[] array)
{
    Console.Write("[");
    for (int i = 0; i < array.Length; i++)
    {
        Console.Write($"{array[i]} ");
    }
    Console.Write("]");
    Console.WriteLine();
}
