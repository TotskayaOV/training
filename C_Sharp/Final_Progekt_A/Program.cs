// 

string[] arrayProject = new string[6] { "Hello", "this", "is", "Final", "Project", ":)" };

Console.Write("[ ");
for (int i = 0; i < arrayProject.Length; i++)
{
    if (arrayProject[i].Length <= 3) Console.Write($"{arrayProject[i]} ");
}
Console.Write("]");


// string[] array2 =  GetArray2(array1);
// PrintArray(array2);
// string[] GetArray2(string[] Array1)
// {
//     int count = 0;
//     int temp = 0;
//     for (int i = 0; i < Array1.Length; i++)
//     {
//         if (Array1[i].Length <= 3) count++;
//     }
//     string[] array2 = new string[count];
//     for (int j = 0; j < Array1.Length; j++)
//     {
//         if (Array1[j].Length <= 3)
//         {
//             array2[temp] = Array1[j];
//             temp++;
//         }
//     }
//     return array2;
// }
	
// void PrintArray(string[] array)
// {
//     Console.Write("[");
//     for (int i = 0; i < array.Length; i++)
//     {
//         Console.Write($"{array[i]} ");
//     }
//     Console.Write("]");
//     Console.WriteLine();
// }
