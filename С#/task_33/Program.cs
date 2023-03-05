

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

void ConvertNumArr(int[] array)
{
  for (int i = 0; i < array.Length; i++)
  {
    array[i] = array[i] * -1;
  }
  Console.Write(String.Join(", ", array));
}

int[] arr = CreateArrayRndInt(10, -10, 10);
Console.WriteLine(String.Join(", ", arr));
ConvertNumArr(arr);
