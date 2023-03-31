System.Console.WriteLine("введите сколько киллометров проезжает машина в день:");
int n = Convert.ToInt32(Console.ReadLine());
System.Console.WriteLine("введите сколько киллометров машина должна проехать: ");
int s = Convert.ToInt32(Console.ReadLine());

int day = (s + (n - 1)) / n;
System.Console.WriteLine($"{day} - столько дней будет ехать машина");