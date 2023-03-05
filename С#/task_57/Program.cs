


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

int[] SortMatrix(int[,] matrix)
{
  int res = 0;
  int[] arr = new int[matrix.GetLength(0)];
  for (int i = 0; i < matrix.GetLength(0); i++)
  {
    for (int j = 0; j <= matrix.GetLength(1); j++)
    {
      {
        if (j < matrix.GetLength(1)) res += matrix[i, j];
        else arr[i] = res;
      }
    }
    res = 0;
  }
  return arr;
}

int ComparArrIndex(int[] arr)
{
  int count = 0;
  int minIndex = 0;
  for (int i = 0; i < arr.Length; i++)
  {
    if (arr[count] >= arr[i])
    {
      arr[count] = arr[i];
      minIndex = i + 1;
    }
  }
  return minIndex;
}

int[,] matrix = CreateArray(5, 4, 0, 30);
PrintaMatrix(matrix);
System.Console.WriteLine();
int[] sortMatrix = SortMatrix(matrix);
System.Console.WriteLine(String.Join(", ", sortMatrix));
System.Console.WriteLine();
int findMinIndex = ComparArrIndex(sortMatrix);
System.Console.WriteLine($"строка с наименьшей суммой элементов: {findMinIndex} строка");


