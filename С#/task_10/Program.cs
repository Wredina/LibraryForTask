

int number = new Random().Next(10, 100);
Console.WriteLine($"Случайное число из отрезка 10 - 99 => {number}");

// int firstDigit = number / 10; // получаем первое число из двух
// int secondDigit = number % 10; // получаем второе число из двух

// if (firstDigit > secondDigit) // сравнение чисел между собой
// {
//   Console.WriteLine($"Наибольшая цифра числа => {firstDigit}");
// }
// else { Console.WriteLine($"Наибольшая цифра числа => {secondDigit}"); }

int MaxDigit(int num)
{
  int firstDigit = num / 10;
  int secondDigit = num % 10;
  if (firstDigit > secondDigit) return firstDigit; // если тру, вернёт первое число, если нет - пропустит и перейдёт к следующей записи кода.
  return secondDigit; // если не пройдёт проверку выше, выведет второе число.
}

int maxDigit = MaxDigit(number);
Console.WriteLine($"Наибольшая цифра числа => {maxDigit}");
