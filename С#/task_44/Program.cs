
// k1*x+b1 = k2*x+b2
// k1*x - k2*x = b2 - b1;
// x = (b2-b1) / (k1-k2)
// y = k1*x + b1

// 5x + 2 = 9x + 4;
// 5x-9x = 4 - 2;
// -4 = 2
// x = 2 / -4;
// x = -0.5
// y = 5 * -0.5 + 2
// y = -0.5


// Вариант решения 1

// void AxisXY(double a1, double a2, double b1, double b2)
// {
//  double x = (b2 - a2) / (a1 - b1);
//  double y = a1 * x + a2;
//  if (a1 * x + a2 == b1 * x + b2) Console.WriteLine($"координаты точки пересечения двух прямых: ({x}; {y})");
//  else Console.WriteLine("прямые не пересекаются");
// }

// Console.WriteLine("задайте значения прямых: "); якобы пользователь задавал так
// double k1 = Convert.ToDouble(ReadLine());
// double b1 = Convert.ToDouble(ReadLine());
// double k2 = Convert.ToDouble(ReadLine());
// double b2 = Convert.ToDouble(ReadLine());

// AxisXY(k1, b1, k2, b2); 



// вариант решения 2 
// (я понимаю, что если ввести другой размер, программа крашнется. У меня просто пошёл творческий процесс. И мне лень было каждый раз переписывать код и спрашивать у пользователя одно и тоже, поэтому в голову пришёл вариант с массивом и циклом)

double[] Direct(int size)
{
  double[] arr = new double[size];
  int i = 0;
  while (i < arr.Length)
  {
    Console.WriteLine($"задайте значения прямых: ");
    arr[i] = Convert.ToDouble(Console.ReadLine());
    i++;
  }
  return arr;
}

void AxisXY(double[] arr)
{
  double x = (arr[3] - arr[1]) / (arr[0] - arr[2]);
  double y = arr[0] * x + arr[1];
  // if (arr[0] == arr[2] && arr[1] == arr[3]) Console.WriteLine("прямые совпадают");
  if (arr[0] * x + arr[1] == arr[2] * x + arr[3]) Console.WriteLine($"координаты точки пересечения двух прямых: ({x}; {y})");
  else Console.WriteLine("прямые не пересекаются");
}

AxisXY(Direct(4));




