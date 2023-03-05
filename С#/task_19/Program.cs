


string Quarter(string num)
{

  // if (num == "1") return "x > 0 и y > 0";
  // if (num == "2") return "x < 0 и y > 0";
  // if (num == "3") return "x < 0 и y < 0";
  // if (num == "4") return "x > 0 и y < 0";
  // return "Введены некорректные координаты";

  switch (num)
  {
    case "1": return "Допустимые координаты: x > 0 и y > 0";
    case "2": return "Допустимые координаты: x < 0 и y > 0";
    case "3": return "Допустимые координаты: x < 0 и y < 0";
    case "4": return "Допустимые координаты: x > 0 и y < 0";
    default: return "Неккоректный ввод!";
  }
}

Console.Write("Введите номер плоскости: ");
string number = Console.ReadLine();
string quarter = Quarter(number);

Console.WriteLine(quarter);

