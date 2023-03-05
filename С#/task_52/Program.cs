


int[,] CreateArray(int rows, int colums, int min, int max)
{
  int[,] array = new int[rows, colums];
  Random rnd = new Random();
  for (int i = 0; i < array.GetLength(0); i++)
  {
    for (int j = 0; j < array.GetLength(1); j++)
    {
      array[i, j] = rnd.Next(min, max);
    }
  }
  return array;
}

void PrintaMatrix(int[,] matrix)
{
  for (int i = 0; i < matrix.GetLength(0); i++)
  {
    Console.Write("[");
    for (int j = 0; j < matrix.GetLength(1); j++)
    {
      if (j < matrix.GetLength(1) - 1) System.Console.Write($"{matrix[i, j],3} |"); else System.Console.Write($"{matrix[i, j],3} ]");
    }
    System.Console.WriteLine();
  }
}

int SumIndexArray(int[,] array)
{
  int res = 0;
  int size = array.GetLength(0);
  if (array.GetLength(0) > array.GetLength(1)) size = array.GetLength(1);

  for (int i = 0; i < size; i++)
  {
    res += array[i, i];
  }
  return res;
}


int[,] arr = CreateArray(3, 4, 0, 10);
PrintaMatrix(arr);
System.Console.WriteLine();
int sumIndexArr = SumIndexArray(arr);
System.Console.WriteLine(sumIndexArr);