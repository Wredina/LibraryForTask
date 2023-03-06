int[] arr = { 1, 5, 4, 3, 2, 6, 7, 1, 1 };
void PrintArray(int[] array)
{
  int count = array.Length;
  for (int i = 0; i < count; i++)
  {
    Console.Write($"{array[i]}");
  }
  Console.WriteLine();
}
void SelectionSort(int[] array)
{
  for (int i = 0; i < array.Length - 1; i++)
  {
    int minPosition = i;
    for (int j = i + 1; j < array.Length; j++)
    {
      if (array[j] < array[minPosition]) minPosition = j;
    }
    int temporary = array[i]; // в переменную записываем число с начальной позиции (аrray[0] = 5) (предположим что массив 5,1)
    array[i] = array[minPosition]; // в эту позицию записываем минимальное число (array[0] = 1, т.к. array[minposition] = 1)
    array[minPosition] = temporary; // в позицию минимального числа записываем число, которое записали в начальную позицию (array[minposition] = 5, т.к temporary = 5);
  }
}
PrintArray(arr);
SelectionSort(arr);
PrintArray(arr);
