

int[] FibonacciNum(int size)
{
  int[] fibArr = new int[size];
  fibArr[0] = 0;
  fibArr[1] = 1;
  for (int i = 2; i < fibArr.Length; i++)
  {
    fibArr[i] = fibArr[i - 1] + fibArr[i - 2];
  }
  return fibArr;
}

int[] fibonacci = FibonacciNum(7);
Console.WriteLine(String.Join(' ', fibonacci));