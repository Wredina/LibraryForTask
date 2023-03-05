Console.WriteLine("введите первое число");
int numOne = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("введите второе число");
int numTwo = Convert.ToInt32(Console.ReadLine());

if (numOne > numTwo)
{
  Console.WriteLine($"Максимальное число = {numOne}, минимальное число = {numTwo}");
}
else if (numTwo > numOne)
{
  Console.WriteLine($"Максимальное число = {numTwo} минимальное число = {numOne}");
}
else
{
  Console.WriteLine($"Чсло {numOne} равно числу {numTwo}");
}