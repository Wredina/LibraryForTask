

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

int[] NumArrMatrix(int[,] matrix)
{
  int count = 0;
  int[] array = new int[matrix.Length];
  for (int i = 0; i < matrix.GetLength(0); i++)
  {
    for (int j = 0; j < matrix.GetLength(1); j++)
    {
      array[count] = matrix[i, j];
      count++;
    }
  }
  return array;
}

void SortArrayNum(int[] array)
{
  int cuontNum = 0;
  int res = 1;
  for (int i = 1; i < array.Length; i++)
  {
    if (array[cuontNum] == array[i]) res++;
    else
    {
      System.Console.WriteLine($"{array[cuontNum]} в массиве штук {res}");
      array[cuontNum] = array[i];
      res = 1;
    }
  }
}


int[,] matrix = CreateArray(4, 4, 0, 30);
PrintaMatrix(matrix);
System.Console.WriteLine();
int[] arr = NumArrMatrix(matrix);
Array.Sort(arr);
System.Console.WriteLine(String.Join(", ", arr));
System.Console.WriteLine();
SortArrayNum(arr);

// int NumArrMatrix(int[,] array)
// {
//  int result = 0;
//  int num = array[0, 0];
//  for (int i = 0; i < array.GetLength(0); i++)
//  {
//   for (int j = 0; j < array.GetLength(1); j++)
//   {
//    if (num == array[i, j]) result++;
//   }
//  }
//  return result;
// }



// int size = arr.GetLength(0) * arr.GetLength(1);
// int count = 0;
// while (count < size)
// {
//  int res = NumArrMatrix(arr);
//  if (res == 0) count++;
//  else
//  {
//   System.Console.WriteLine($"в массиве {res} штук");
//   count++;
//  }
// }
