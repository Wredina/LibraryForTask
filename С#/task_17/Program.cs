

int Mul(int numOne, int numTwo)
{
  if (numOne > numTwo)
  {
    return numTwo * numTwo;
  }
  return numOne * numOne;
}

Console.WriteLine("Введите случайное число 1");
int num1 = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Введите случайное число 2");
int num2 = Convert.ToInt32(Console.ReadLine());

int result = Mul(num1, num2);

if (result == num1 || result == num2)
{
  Console.WriteLine("одно число является квадратом другого");
}
else
{
  Console.WriteLine("одно число не является квадратом другого");
}