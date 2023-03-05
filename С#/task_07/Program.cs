Console.WriteLine("Введите число");
int num = Convert.ToInt32(Console.ReadLine());

if (num % 2 == 0)
{
  Console.Write($"Число {num} чётное");
}
else
{
  Console.Write($"Число {num} не чётное");
}