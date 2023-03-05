


int MulNum(int numOne, int numTwo)
{
  if (numTwo == 0 || numOne == 0) return 1;
  if (numOne >= numTwo) return numTwo * MulNum(numOne - 1, numTwo);
  else return numOne * MulNum(numOne, numTwo - 1);
}



int userNumOne = new Random().Next(1, 10);
System.Console.Write($"{userNumOne}, ");
int userNumTwo = new Random().Next(1, 10);
System.Console.WriteLine(userNumTwo);
int mulNum = MulNum(userNumOne, userNumTwo);
System.Console.WriteLine(mulNum);