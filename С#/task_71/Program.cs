string[] СreationArrString(int sizeArr)
{
 string[] array = new string[sizeArr];
 string[] letters = new string[26] { "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" };
 for (int j = 0; j < sizeArr; j++)
 {
  string word = "";
  Random rnd = new Random();
  int wordSize = rnd.Next(1, 10);
  for (int i = 0; i < wordSize; i++)
  {
   word += letters[rnd.Next(0, 26)];
  }
  array[j] = word;
 }
 return array;
}


int SizeForMiniArray(string[] array)
{
 int sizeMiniArr = array.Length;
 for (int i = 0; i < array.Length; i++)
 {
  if (array[i].Length > 3) sizeMiniArr -= 1;
 }
 return sizeMiniArr;
}

string[] CreateNewMiniArrayString(int size, string[] BigArr)
{
 int j = 0;
 string[] miniArr = new string[size];
 for (int i = 0; i < BigArr.Length; i++)
 {
  if (BigArr[i].Length <= 3)
  {
   miniArr[j] = BigArr[i];
   j++;
  }
 }
 return miniArr;
}


string[] arr = СreationArrString(new Random().Next(4, 8));
Console.WriteLine(String.Join(", ", arr));
int sizeMiniArray = SizeForMiniArray(arr);
if (sizeMiniArray == 0) System.Console.WriteLine("нет элементов менее 4-х символов");
else
{
 string[] miniArr = CreateNewMiniArrayString(sizeMiniArray, arr);
 Console.WriteLine(String.Join(", ", miniArr));
}


