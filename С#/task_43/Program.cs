

int Binar(int num)
{
  int bin = 0;
  int count = 1;
  while (num != 0)
  {
    bin += num % 2 * count;
    num /= 2;
    count *= 10;
  }
  return bin;
}

int result = Binar(45);
Console.WriteLine(result);