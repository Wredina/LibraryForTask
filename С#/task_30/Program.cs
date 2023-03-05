

int[] GenerateArr(int index)
{
  int[] arr = new int[index];
  for (int i = 0; i < arr.Length; i++)
  {
    arr[i] = new Random().Next();
  }
  return arr;
}

// void PrintArr(int[] arrNum)
// {
//   for (int i = 0; i < arrNum.Length; i++)
//   {
//     Console.Write(arrNum[i] + " ");
//   }
// }

int[] array = GenerateArr(8);
// PrintArr(array);
Console.WriteLine($"{String.Join(", ", array)} ---> [{String.Join(", ", array)}]");