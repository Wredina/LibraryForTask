

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

int QuantityNum(int[] array)
{
  int num = 0;
  for (int i = 0; i < array.Length; i++)
  {
    if (array[i] % 2 == 0) num++;
  }
  return num;
}

int[] arr = CreateArrayRndInt(5, 1, 10);
int quanNum = QuantityNum(arr);
Console.Write($"[{String.Join(",", arr)}] -> {quanNum}");