

double[,] RndMatrixArray(int row, int colums, double min, double max)
{
  Random rnd = new Random();
  double[,] array = new double[row, colums];
  for (int i = 0; i < array.GetLength(0); i++)
  {
    for (int j = 0; j < array.GetLength(1); j++)
    {
      array[i, j] = Math.Round(rnd.NextDouble() * ((max + 1) - min) + min, 1);
      // System.Console.WriteLine(array[i, j]); моя проверка
    }
  }
  return array;
}

void PrintaMatrix(double[,] matrixArr)
{
  for (int i = 0; i < matrixArr.GetLength(0); i++)
  {
    Console.Write("[");
    for (int j = 0; j < matrixArr.GetLength(1); j++)
    {
      if (j < matrixArr.GetLength(1) - 1) System.Console.Write($"{matrixArr[i, j],4} |"); else System.Console.Write($"{matrixArr[i, j],4} ]");
    }
    System.Console.WriteLine();
  }
}

double[,] matrix = RndMatrixArray(3, 4, -5, 5);
PrintaMatrix(matrix);

