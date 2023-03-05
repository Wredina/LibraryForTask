

int[,] CreateMatrixArray(int rows, int colums, int min, int max)
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

// можно решить через булев тип, но мне это больше нравится
int FindElementMatrix(int[,] array, int x, int y)
{
  if (x > array.GetLength(0) || y > array.GetLength(1)) return 0;
  else return array[x - 1, y - 1];
}

int[,] arr = CreateMatrixArray(6, 6, 0, 10);
PrintaMatrix(arr);
System.Console.Write("введите первую позицию элемента: ");
int positionX = Convert.ToInt32(Console.ReadLine());
System.Console.Write("введите вторую позицию элемента: ");
int positionY = Convert.ToInt32(Console.ReadLine());
int findEl = FindElementMatrix(arr, positionX, positionY);
if (findEl == 0) System.Console.WriteLine($"по позиции {positionX} и {positionY} элемента нет");
else System.Console.WriteLine($"искомый элемент {findEl}");

