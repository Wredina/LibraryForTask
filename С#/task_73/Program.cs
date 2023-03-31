System.Console.WriteLine("введите трёхзначное число:");

int userNum = Convert.ToInt32(Console.ReadLine());

if (userNum > 999 || userNum < 100)
{
  System.Console.WriteLine("вы ввели не верное число");
}
else
{
  int firstNum = userNum / 100;
  int twoNum = (userNum / 10) % 10;
  int lastNum = userNum % 10;
  int sumNum = firstNum + twoNum + lastNum;
  System.Console.WriteLine(sumNum);
}