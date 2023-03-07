// n-m+1
// n = 15
// m = 5
// 15-5+1 = 11

int[] GetRangeSum(int[] array, int m)
{
  int n = array.Length;
  int[] t = new int[n - m + 1];

  int index = 0;

  for (int i = 0; i < m - n; i++)
  {
    for (int j = i; j <= i + m; j++)
    {
      t[index] += array[j];
    }
    index++;
  }
  return t;
}

int[] CreateArray(int size) => new int[size];

string Print(int[] array) => $"[{String.Join(", ", array)}]";

void Fill(ref int[] array) => array = array.Select(e => Random.Shared.Next(10)).ToArray();

int[] numbers = CreateArray(15);
Fill(ref numbers);
System.Console.WriteLine(Print(numbers));

int count = 5;
int[] sumNum = GetRangeSum(numbers, count);
System.Console.WriteLine(Print(sumNum));
