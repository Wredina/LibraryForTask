// А1А2=№(х2 - х1)** + (у2 - у1)**
// Math.Pow(2, 10) // возведение в степень, 2 в 10-ю
// Math.Sqrt(5) // извлечение из корня
// Math.Round(х, 2) // округление числа х до второго знака после запятой
// Math.Round(х, 2, MidpointRounding.ToZero) // более точное округление с учётом нулей

Console.WriteLine("Введите число");
int userNum = Convert.ToInt32(Console.ReadLine());

void Conv(int num)
{
  for (int i = 1; i <= num; i++)
  {
    double result = Math.Pow(i, 2);
    Console.Write($"{result}, ");
  }
}

Conv(userNum);