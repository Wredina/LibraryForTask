

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

void PrintArray(int[] array)
{
  Console.Write("[");
  for (int i = 0; i < array.Length; i++)
  {
    if (i < array.Length - 1) Console.Write($"{array[i]},");
    else Console.Write($"{array[i]}");
  }
  Console.WriteLine("]");
}

int GetSumNegativeNum(int[] array)
{
  int sum = 0;
  for (int i = 0; i < array.Length; i++)
  {
    if (array[i] < 0) sum += array[i];
  }
  return sum;
}

int GetSumPositiveNum(int[] array)
{
  int sum = 0;
  for (int i = 0; i < array.Length; i++)
  {
    if (array[i] > 0) sum += array[i];
  }
  return sum;
}

int[] GetSumPosNegNum(int[] array)
{
  int sumNeg = 0;
  int sumPos = 0;
  for (int i = 0; i < array.Length; i++)
  {
    if (array[i] > 0) sumPos += array[i];
    if (array[i] < 0) sumNeg += array[i];
  }
  return new int[] { sumNeg, sumPos };
}

int[] arr = CreateArrayRndInt(12, -9, 9);
PrintArray(arr);
int negativeNum = GetSumNegativeNum(arr);
int positiveNum = GetSumPositiveNum(arr);
int[] positNegatSum = GetSumPosNegNum(arr);
Console.WriteLine($"Сумма положительных элементов {positiveNum}");
Console.WriteLine($"Сумма отрицательных элементов {negativeNum}");
Console.WriteLine($"Сумма отрицательных элементов {positNegatSum[0]}");
Console.WriteLine($"Сумма положительных элементов {positNegatSum[1]}");
