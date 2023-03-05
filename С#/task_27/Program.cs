

Console.WriteLine("введите число");
int userNum = Convert.ToInt32(Console.ReadLine());

// if (userNum < 0)
// {
//   Console.WriteLine("ввели отрицательное число");
// }
// else
// {
int result = Numbers(userNum);
Console.WriteLine($"колличество цифр в {userNum} = {result}");
// }


int Numbers(int num)
{
  if (num < 0) num = num * -1;

  int i = 0;
  for (; num > 0; i++)
  {
    num = num / 10;
  }
  return i;
}