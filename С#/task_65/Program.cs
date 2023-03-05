

int SumNum(int num)
{

  if (num == 0) return 0;
  return num % 10 + SumNum(num / 10);
}


int userNum = new Random().Next(1, 1000);
System.Console.WriteLine(userNum);
int sumNum = SumNum(userNum);
System.Console.WriteLine(sumNum);
