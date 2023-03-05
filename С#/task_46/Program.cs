

int[] ArrOne(int size)
{
  int[] array = new int[size];
  for (int i = 0; i < array.Length; i++)
  {
    array[i] += new Random().Next(1, 10);
  }
  return array;
}

int[] ArrTwo(int[] array, int size)
{
  int[] newArr = new int[size];
  for (int i = 0; i < array.Length; i++)
  {
    newArr[i] += array[i];
  }
  return newArr;
}

Console.Write("введите длину массива: ");
int sizeArr = Convert.ToInt32(Console.ReadLine());
int[] arrOne = ArrOne(sizeArr);
Console.WriteLine(String.Join(", ", arrOne));
int[] arrTwo = ArrTwo(arrOne, sizeArr);
Console.WriteLine(String.Join(", ", arrTwo));
