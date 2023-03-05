


// А1А2=№(х2 - х1)** + (у2 - у1)**
// Math.Pow(2, 10) // возведение в степень, 2 в 10-ю
// Math.Sqrt(5) // извлечение из корня
// Math.Round(х, 2) // округление числа х до второго знака после запятой
// Math.Round(х, 2, MidpointRounding.ToZero) // более точное округление с учётом нулей

double Cvadro(int num1, int num2)
{
  int sub = num2 - num1;
  return Math.Pow(sub, 2);
}

Console.WriteLine("Введите координаты первой точки");
Console.Write("X1: ");
int x1 = Convert.ToInt32(Console.ReadLine());
Console.Write("Y1: ");
int y1 = Convert.ToInt32(Console.ReadLine());

Console.WriteLine("Введите координаты второй точки");
Console.Write("X2: ");
int x2 = Convert.ToInt32(Console.ReadLine());
Console.Write("Y2: ");
int y2 = Convert.ToInt32(Console.ReadLine());

double additNum = Cvadro(x1, x2) + Cvadro(y1, y2);
double root = Math.Sqrt(additNum);
Console.WriteLine($"расстояние между двемя точками равно {Math.Round(root, 2, MidpointRounding.ToZero)}");

// Console.WriteLine("введите координаты первой точки ");
// Console.Write("X1: ");
// int x1 = Convert.ToInt32(Console.ReadLine());
// Console.Write("Y1: ");
// int y1 = Convert.ToInt32(Console.ReadLine());

// Console.WriteLine("введите координаты второй точки ");
// Console.Write("X2: ");
// int x2 = Convert.ToInt32(Console.ReadLine());
// Console.Write("Y2: ");
// int y2 = Convert.ToInt32(Console.ReadLine());

// double distance = Distance(x1, y1, x2, y2);
// double distance1 = Math.Round(distance, 2, MidpointRounding.ToZero);
// Console.WriteLine($"Расстояние между точками {distance1}");

// double Distance(int a1, int b1, int a2, int b2)
// {
//   return Math.Sqrt(Math.Pow((a2 - a1), 2) + Math.Pow((b2 - b1), 2));
//   
// }