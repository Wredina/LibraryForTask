

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

void ReverseArray(int[] array)
{
  for (int i = 0; i < array.Length / 2; i++)
  {
    int temp = array[i];
    array[i] = array[array.Length - 1 - i];
    array[array.Length - 1 - i] = temp;
  }
}

int[] arr = CreateArrayRndInt(5, 1, 10);
Console.WriteLine(String.Join(',', arr));
ReverseArray(arr);
Console.WriteLine(String.Join(',', arr));
Array.Reverse(arr);
Console.WriteLine(String.Join(',', arr));
