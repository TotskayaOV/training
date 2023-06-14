Console.Write("Введите свое имя: ");
string username = Console.ReadLine();

if(username.ToLower() == "дима")
{
    Console.WriteLine("Ура, это же Дима!");
}
else
{
    Console.Write("Привет, ");
    Console.Write(username);    
}
