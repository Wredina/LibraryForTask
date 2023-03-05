

int NumTwo(int num)
{
  int del = num / 10;
  return del % 10;
}

int number = new Random().Next(100, 1000);
Console.WriteLine($"Случайное трёхзначное число {number}");

int result = NumTwo(number);
Console.WriteLine($"Из трёхначного числа {number} вторая цифра = {result}");

