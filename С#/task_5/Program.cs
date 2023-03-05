Console.WriteLine("Введите первое число");
int a = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Введите второе число");
int b = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Введите третье число");
int c = Convert.ToInt32(Console.ReadLine());

if (a > b && a > c)
{
  Console.Write($"Максимальное число из {a}, {b}, {c} = {a}");
}
else if (b > a && b > c)
{
  Console.Write($"Максимальное число из {a}, {b}, {c} = {b}");
}
else
{
  Console.Write($"Максимальное число из {a}, {b}, {c} = {c}");
}