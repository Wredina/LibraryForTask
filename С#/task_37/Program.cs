

int[] CreateArrayRndInt(int size, int min, int max)
{
  int[] array = new int[size];
  Random rnd = new Random();
  for (int i = 0; i < array.Length; i++)
  {
    array[i] = rnd.Next(min, max + 1);
  }
  return array;
}

int SumNumArr(int[] array)
{
  int sum = 0;
  for (int i = 1; i < array.Length; i++)
  {
    sum += array[i];
    i++;
  }
  return sum;
}

int[] arr = CreateArrayRndInt(5, 0, 10);
int sum = SumNumArr(arr);
Console.WriteLine($"[{String.Join(", ", arr)}] -> {sum}");