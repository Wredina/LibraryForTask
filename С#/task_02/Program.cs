Console.WriteLine("Введите первое число");
int numA = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Введите второе число");
int numB = Convert.ToInt32(Console.ReadLine());

if (numA > numB)
{
  if (numA / numB == numB)
  {
    Console.WriteLine("Первое число является квадратом второго");
  }
  else
  {
    Console.WriteLine("Первое число не является квадратом второго");
  }
}
else
{
  if (numB / numA == numA)
  {
    Console.WriteLine("Второе число является квадратом первого");
  }
  else
  {
    Console.WriteLine("Второе число не является квадратом первого");
  }
}