
int Sum(int num)
{
  int result = 0;
  for (int i = 0; num != 0; i++)
  {
    result += num % 10;
    num /= 10;
  }
  return result;
}

Console.WriteLine("Введите число");
int userNum = Convert.ToInt32(Console.ReadLine());

int sum = Sum(userNum);
Console.WriteLine($"сумма чисел {userNum} = {sum}");