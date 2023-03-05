

int Extent(int num1, int num2)
{
  int res = num1;
  for (int i = 1; i < num2; i++)
  {
    res *= num1;
  }
  return res;
}

Console.WriteLine("введите первое число");
int userNum1 = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("введите второе натуральное число");
int userNum2 = Convert.ToInt32(Console.ReadLine());

if (userNum2 < 1) Console.WriteLine("ввели не верные данные");
else
{
  int result = Extent(userNum1, userNum2);
  Console.WriteLine($"число {userNum1} возведённое в степень {userNum2} = {result}");
}




