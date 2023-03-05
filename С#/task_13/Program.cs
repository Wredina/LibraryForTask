
int Del(int one, int two)
{
  if (one % two == 0)
  {
    int result = 0;
    return result;
  }
  else
  {
    int result = one % two;
    return result;
  }
}

Console.WriteLine("Введите случайное число 1");
int num1 = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Введите случайное число 2");
int num2 = Convert.ToInt32(Console.ReadLine());

int final = Del(num1, num2);

if (final == 0)
{
  Console.WriteLine($"число {num1} кратно числу {num2}");
}
else
{
  Console.WriteLine($"число {num1} не кратно числу {num2}, остаток {final}");
}
