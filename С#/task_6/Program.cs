Console.WriteLine("введите целое положительное число");
int numA = Convert.ToInt32(Console.ReadLine());
if (numA > 0)
{
  for (int i = -numA; i <= numA; i++)
  {
    int count = i;
    Console.Write($"{count} ");
  }
}
else
{
  Console.Write("введены не корректные данные");
}

// string count = "0";
// for (int i = 1; i <= numA; i++){
//    count = $"{-i}" + count + $"{i}"
// }
// return count;
// уменьшает кол-во итерраций вдвое.