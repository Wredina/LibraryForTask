


int[,,] CreateArray(int rows, int colums, int zIndex, int min, int max)
{
  int[,,] array = new int[rows, colums, zIndex];
  Random rnd = new Random();
  for (int i = 0; i < array.GetLength(0); i++)
  {
    for (int j = 0; j < array.GetLength(1); j++)
    {
      for (int z = 0; z < array.GetLength(2); z++)
      {
        array[i, j, z] = rnd.Next(min, max);
      }
    }
  }
  return array;
}

void PrintaMatrix(int[,,] matrix)
{
  for (int i = 0; i < matrix.GetLength(0); i++)
  {
    Console.Write("[");
    for (int j = 0; j < matrix.GetLength(1); j++)
    {
      for (int z = 0; z < matrix.GetLength(1); z++)
      {
        if (j < matrix.GetLength(1) - 1) System.Console.Write($"{matrix[i, j, z],3} ({i},{j},{z}) |"); else System.Console.Write($"{matrix[i, j, z],3} ({i},{j},{z})]");
      }

    }
    System.Console.WriteLine();
  }
}



int[,,] matrix = CreateArray(2, 2, 2, 10, 100);
PrintaMatrix(matrix);