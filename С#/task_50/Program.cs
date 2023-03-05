


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

int[,] NewArray(int[,] array)
{
  for (int i = 0; i < array.GetLength(0); i += 2)
  {
    for (int j = 0; j < array.GetLength(1); j += 2)
    {
      array[i, j] *= array[i, j];
    }
  }
  return array;
}

int[,] arr = CreateArray(3, 4, 0, 10);
PrintaMatrix(arr);
System.Console.WriteLine();
int[,] newArr = NewArray(arr);
PrintaMatrix(newArr);