

int[] UserArr(int size)
{
  int[] array = new int[size];
  for (int i = 0; i < size; i++)
  {
    Console.WriteLine($"введите {i + 1} число: ");
    array[i] = Convert.ToInt32(Console.ReadLine());
  }
  return array;
}

int PositiveNum(int[] arr)
{
  int positive = 0;
  for (int i = 0; i < arr.Length; i++)
  {
    if (arr[i] > 0) positive++;
  }
  return positive;
}

Console.WriteLine("введите желательное кол-во чисел: ");
int userSize = Convert.ToInt32(Console.ReadLine());
int[] userArray = UserArr(userSize);
Console.WriteLine($"ваши числа: {String.Join(", ", userArray)}");
int positNum = PositiveNum(userArray);
Console.WriteLine($"кол-во чисел больше нуля = {positNum}");
