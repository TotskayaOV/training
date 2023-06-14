Console.Write("Введите дистанцию: ");
string distUser = Console.ReadLine();

double distance = double.Parse (distUser);
int count = 0;
int firstFriendSpeed = 1;
int secondFriendSpeed = 2;
int DogSpeed = 5;
int friend = 2;
double time = 0;

while (distance > 10)
{
    if (friend == 1)
    {
        time = distance / (firstFriendSpeed + DogSpeed);
        friend = 2;
    }
    else
    {
        time = distance / (secondFriendSpeed + DogSpeed);
        friend = 1;
    }
    distance = distance - (secondFriendSpeed + firstFriendSpeed) * time;
    count = count + 1;
}
Console.WriteLine(count);