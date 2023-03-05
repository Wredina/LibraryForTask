// можно решить через свич

Console.WriteLine("введите целое число от 1 до 7");
int numA = Convert.ToInt32(Console.ReadLine());

if (numA == 1)
{
  Console.WriteLine("Понедельник");
}
else if (numA == 2)
{
  Console.WriteLine("Вторник");
}
else if (numA == 3)
{
  Console.WriteLine("Среда");
}
else if (numA == 4)
{
  Console.WriteLine("Четверг");
}
else if (numA == 5)
{
  Console.WriteLine("Пятница");
}
else if (numA == 6)
{
  Console.WriteLine("Суббота");
}
else if (numA == 7)
{
  Console.WriteLine("Воскресение");
}
else
{
  Console.WriteLine("Вы ввели некорректные данные");
}