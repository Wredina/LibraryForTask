
bool SumSide(int side1, int side2, int side3)
{
  return side1 + side2 > side3 && side1 + side3 > side2 && side2 + side3 > side1;
}

string result = SumSide(4, 3, 7) ? "yes" : "no";
Console.WriteLine(result);