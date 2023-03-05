

Console.WriteLine("Введите число");
int userNum = Convert.ToInt32(Console.ReadLine());

void Conv(int num)
{
  if (num < 0)
  {
    for (int i = -1; i >= num; i--)
    {
      double result = Math.Pow(i, 3);
      Console.Write($"{result}, ");
    }
  }
  else
  {
    for (int i = 1; i <= num; i++)
    {
      double result = Math.Pow(i, 3);
      Console.Write($"{result}, ");
    }
  }
}

Conv(userNum);