

void NaturalNum(int num)
{
  if (num == 0) return;
  NaturalNum(num - 1);
  System.Console.Write($"{num} ");
}

int rndNum = new Random().Next(1, 10);
System.Console.WriteLine(rndNum);
NaturalNum(rndNum);

