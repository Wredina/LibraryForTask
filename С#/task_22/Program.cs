// Math.Pow(2, 10) - возведение в степень, 2 в 10-ю
// Math.Sqrt(5) -извлечение из корня
// Math.Round(х, 2) -округление числа х до второго знака после запятой
// Math.Round(х, 2, MidpointRounding.ToZero) -более точное округление с учётом нулей
// А1А2=№(х2 - х1)** + (у2 - у1)**



Console.WriteLine("Введите координаты первой точки");
Console.Write("X1: ");
int x1 = Convert.ToInt32(Console.ReadLine());
Console.Write("Y1: ");
int y1 = Convert.ToInt32(Console.ReadLine());
Console.Write("Z1: ");
int z1 = Convert.ToInt32(Console.ReadLine());

Console.WriteLine("Введите координаты второй точки");
Console.Write("X2: ");
int x2 = Convert.ToInt32(Console.ReadLine());
Console.Write("Y2: ");
int y2 = Convert.ToInt32(Console.ReadLine());
Console.Write("Z2: ");
int z2 = Convert.ToInt32(Console.ReadLine());

double Distance(int xc1, int yc1, int zc1, int xc2, int yc2, int zc2)
{
  return Math.Sqrt(Math.Pow((xc2 - xc1), 2) + Math.Pow((yc2 - yc1), 2) + Math.Pow((zc2 - zc1), 2));
}

double dis = Distance(x1, y1, z1, x2, y2, z2);
double result = Math.Round(dis, 2, MidpointRounding.ToZero);
Console.WriteLine($"Расстояние между точками {result}");


