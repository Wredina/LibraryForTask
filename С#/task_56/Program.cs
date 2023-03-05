

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

int[,] ReverseArrayMatrix(int[,] array)
{
  for (int i = 0; i < array.GetLength(0) - 1; i++)
  {
    for (int j = i + 1; j < array.GetLength(1); j++)
    {
      int num = array[i, j];
      array[i, j] = array[j, i];
      array[j, i] = num;
    }
  }
  return array;
}

int[,] arr = CreateArray(4, 4, 0, 10);
if (arr.GetLength(0) == arr.GetLength(1))
{
  PrintaMatrix(arr);
  System.Console.WriteLine();
  int[,] reverseMatrix = ReverseArrayMatrix(arr);
  PrintaMatrix(reverseMatrix);
}
else
{
  System.Console.WriteLine("элементы должны быть равны");
}