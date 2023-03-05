

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

int QuantNum(int[] array, int min, int max)
{
  int num = 0;
  for (int i = 0; i < array.Length; i++)
  {
    if (array[i] > min && array[i] < max + 1) num++;
  }
  return num;
}

int[] arr = CreateArrayRndInt(123, 1, 200);
int quantNum = QuantNum(arr, 10, 99);
Console.WriteLine($"[{String.Join(", ", arr)}] --> {quantNum}");

