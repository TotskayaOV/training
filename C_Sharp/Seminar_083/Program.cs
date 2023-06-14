// Составить частотный словарь элементов двумерного массива. 
// Частотный словарь содержит информацию о том, сколько раз встречается элемент входных данных.


int rows = new Random().Next(1, 10);
int columns = new Random().Next(1, 10);
int[,] array = GetArray(rows, columns);

Console.Clear();
PrintArray(array);
Console.WriteLine();

for (int i = 0; i < 10; i++)
{
    int number = i;
    int count = GetElement(array, number);
    if (count > 0) Console.WriteLine($"Количесво {i} в массиве = {count}");
}


void PrintArray(int[,] inArray)  //Метод вывода массива
{
    for (int i = 0; i < inArray.GetLength(0); i++)
    {
        for (int j = 0; j < inArray.GetLength(1); j++)
        {
            Console.Write($"{inArray[i, j]} ");
        }
        Console.WriteLine();
    }
}

int[,] GetArray(int m, int n)   //Метод создания массива
{
    int[,] result = new int[m, n];
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            result[i, j] = new Random().Next(0, 10); 
         }
    }
    return result;
}

static int GetElement(int[,] array, int number) //Метод поиска числа
{
    int count = 0;

    foreach (int element in array)
    {
        if (number == element)
            count += 1;
    }
    return count;
}

