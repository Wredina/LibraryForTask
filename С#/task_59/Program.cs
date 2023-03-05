

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
      if (j < matrix.GetLength(1) - 1) System.Console.Write($"{matrix[i, j],4} |"); else System.Console.Write($"{matrix[i, j],3} ]");
    }
    System.Console.WriteLine();
  }
}

int[,] MulMatrix(int[,] m1, int[,] m2)
{
  int[,] m3 = new int[m1.GetLength(0), m2.GetLength(1)];
  for (int i = 0; i < m1.GetLength(0); i++)
  {
    for (int j = 0; j < m2.GetLength(1); j++)
    {
      m3[i, j] = 0;

      for (int k = 0; k < m1.GetLength(1); k++)
      {
        m3[i, j] += m1[i, k] * m2[k, j];
      }
    }
  }
  return m3;
}

System.Console.WriteLine("матрица А");
int[,] matrixA = CreateArray(2, 2, 0, 10);
PrintaMatrix(matrixA);
System.Console.WriteLine();
System.Console.WriteLine("матрица Б");
int[,] matrixB = CreateArray(2, 2, 0, 10);
PrintaMatrix(matrixB);
System.Console.WriteLine();
if (matrixA.GetLength(0) != matrixB.GetLength(1)) System.Console.WriteLine("кол-во строк матрицы 1 не равно кол-ву столбцов матрицы 2");
else
{
  int[,] matrixC = MulMatrix(matrixA, matrixB);
  System.Console.WriteLine("матрица C");
  PrintaMatrix(matrixC);
}