

void NaturalNum(int numOne, int numTwo)
{
  System.Console.Write($"{numOne}  ");
  if (numOne == numTwo) return;
  else if (numOne > numTwo)
  {
    NaturalNum(numOne - 1, numTwo);
  }
  else
  {
    NaturalNum(numOne + 1, numTwo);
  }
}

int userNumOne = new Random().Next(1, 10);
System.Console.Write($"{userNumOne}, ");
int userNumTwo = new Random().Next(1, 10);
System.Console.WriteLine(userNumTwo);
NaturalNum(userNumOne, userNumTwo);