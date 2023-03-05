

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

int[] MultNumArr(int[] array)
{
  int size = array.Length / 2;
  if (array.Length % 2 == 1) size += 1;
  int[] newArray = new int[size];
  for (int i = 0; i < size; i++)
  {
    if (array[i] == array[array.Length - 1 - i]) newArray[i] = array[i];
    else newArray[i] = array[i] * array[array.Length - 1 - i];
  }
  return newArray;
}

int[] arr = CreateArrayRndInt(5, 1, 10);
int[] newArr = MultNumArr(arr);
Console.WriteLine(String.Join(", ", arr));
Console.WriteLine(String.Join(", ", newArr));