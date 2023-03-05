Console.WriteLine("Введите трёхзначное число");
int num = Convert.ToInt32(Console.ReadLine());

if (100 > num || num > 999)
{
  Console.Write("Вы ввели не верное число");
}
else
{
  int lastNum = num % 10;
  Console.Write($"Последняя цифра в Вашем числе = {lastNum}");
}