

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

int[,] SortMatrix(int[,] matrix)
{
  int num = 0;
  for (int i = 0; i < matrix.GetLength(0); i++)
  {
    for (int j = 0; j < matrix.GetLength(1); j++)
    {
      for (int q = j + 1; q <= matrix.GetLength(1) - 1; q++)
      {
        if (matrix[i, j] < matrix[i, q])
        {
          num = matrix[i, j];
          matrix[i, j] = matrix[i, q];
          matrix[i, q] = num;
        }
      }
    }
  }
  return matrix;
}


int[,] matrix = CreateArray(4, 4, 0, 30);
PrintaMatrix(matrix);
System.Console.WriteLine();
int[,] sortMatrix = SortMatrix(matrix);
PrintaMatrix(sortMatrix);