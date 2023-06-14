//создаем новый нулевой массив и рандомайзером заполняем его
void FillArray(int[] collection)
{
    int length = collection.Length;
    int index = 0;
    while (index < length)
    {
        collection[index] = new Random().Next(1, 10);
        index++;
    }
}

//выводим в терминале элементы массива
void PrintArray(int[] col)
{
    int count =col.Length;
    int position = 0;
    while (position < count)
    {
        Console.Write(col[position] + " ");
        position++;
    }
}

int IndexOf(int[] collection, int find)
{
    int count = collection.Length;
    int index = 0;
    int position = -1; //обозначение -1 вместо 0 вводится для обозачения случаев ненахождения find в массиве

    while (index < count)
    {
        if(collection[index] == find)
        {
            position = index;
            break;  //останавливает исполнение цикла на первом же найденном find
        }
        index++;
    }
    return position;

}

int[] array = new int[10];

FillArray(array);
PrintArray(array);
Console.WriteLine();

int pos = IndexOf(array, 40);
Console.WriteLine(pos);