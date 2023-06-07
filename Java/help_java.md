# Настройка
Шаг 1:
Java JDK https://www.oracle.com/java/technologies/downloads/
Шаг 2:
Extension Pack VS Code
https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-javapack
При желаниии:
https://www.jetbrains.com/ru-ru/idea/
println(“Hello world”);

# Типы данных и переменные

В Java весь код пишется внутри класса, в методе Main
```java
public class program {
  public static void main(String[] args){
    //здесь пишем весь код
  }
}
```

## _Типы данных_
1. Ссылочные - Arrays, String и т.д.
2. Примитивные: 
    1. boolean
    2. int - целочисленный тип
    3. short - целочисленный тип
    4. long
    5. byte
    6. float - вещественный тип
    7. double - вещественный тип
    8. char - определяет отдельный символ

# Классы обёртки
___
| Примитив | Обёртка |
|-----------|----------|
|int|Integer|
|short|Short|
|long|Long|
|byte|Byte|
|float|Float|
|double|Double|
|char|Character|
|boolean|Boolean|

Обёртки нужны для обращения ко вложенным методам типа
```java
Integer.MIN_VALUE // минимальное значение int которое в него помещается (4 байта - 2147483648)
```

# _Создание переменной_
<тип> <идентификатор>;

<идентификатор> = <значение>;

Что бы определить тип данных: getType(переменная);
``` java
int a = 123;
System.out.println(getType(a));// Integer
```
Если нужно записать какое-то огромное число, типа 20000000, что бы не запутаться, можно использовать нижнее подчёркивание
```java
int i = 20_000_000;
```

```java
int salary = 123456; // 4 байта
short age = 10; // тоже самое что и int(4 байта), только вмещает меньше информации
float e = 2.7f; // обязательно используется суфикс f
double pi = 3.1415; // 8 байт. есть свой суффикс D, но он не обязательный
char ch = '1'; // определяет отдельный символ
boolean flag1 = 123 <= 234;// true
boolean flag2 = flag1 ^ false; // true. разделительная дизъюнкция, истина только тогда, когда ОДНО из выражений истино. Если оба истины, будет false
```
# _Неявная типизация_
При компиляции вместо var будет подставлен тот тип данных, который больше подходит для данного значения
```java
var i = 123; // при компиляции будет подставленно int
var b = "str"; // при компиляции будет подставленно string
```

# _булевые тонкости_
```java
if a > b & c > b // одна & - обязательная проверка двух условий
if a > b && c > b // если первое условие лож - не будет проверять второе.
if a > b | c > b // проверка двух условий (если первое условие true и второе условие true, выведет false)
if a > b || c > b // если первое условие истино, не будет проверять второе и выведет true
```

<br>
<br>


___

# Работа с терминалом
___
* Вывод информации на терминал
  ```java
  System.out.print("hello");
  ```
  Причём есть немного разные виды вывода информации в терминал через print()
  > System.out.print() - в конце сообщения не будет перехода на новую строку. Т.е. следующий вывод информации будет на этой же строчке

  > System.out.println() - выведет информацию и в конце будет переход на следующую строку.

  После написания кода, для его компиляции и вывода нажимается кнопка **RUN** либо в терминале записывается команда:
  > java имя_файла.java

<br>
<br>

* Ввод информации через терминал

  для того, что бы мы могли ввести какую либо информацию через терминал нужно подключить библиотеку
  ```java
  import java.util.Scanner
  // обозначить, откуда будет подтягиваться информация
  Scanner scanner = new Scanner(System.in);
  // и запросить ввод
  String op = scanner.nextLine("ввод");
  ```

<br>

# Виды спецификаторов (масок)
```java
%d: целочисленных значений
%x: для вывода шестнадцатеричных чисел
%f: для вывода чисел с плавающей точкой
%e: для вывода чисел в экспоненциальной форме, например: 3.1415e+01
%c: для вывода одиночного символа
%s: для вывода строковых значений
```

<br>

Пример работы со спецификаторами
```java
int a = 1, b = 2;
int c = a + b;
String res = String.format("%d + %d = %d \n", a, b, c); // вариант 1, использование явного преобразования для вложения в переменную
System.out.println(res);
System.out.printf("%d + %d = %d \n", a, b, c); // вариант 2 - сразу вывод в консоль при помощи printf
```
> \n - для обозначения окончания ввода. (в VSC по такому форматированию, при выводе в консоль, в конце текста выскакивает % - что бы этого небыло - \n )

<br>

Выводы знаков после запятой
```java
float pi = 3.1415f;
System.out.printf("%f\n", pi); // 3,141500
System.out.printf("%.2f\n", pi); // 3,14
System.out.printf("%.3f\n", pi); // 3,141
System.out.printf("%e\n", pi); // 3,141500e+00
System.out.printf("%.2e\n", pi); // 3,14e+00
System.out.printf("%.3e\n", pi); // 3,141e+00
```

<br>

Получение данных из терминала
> использование Scanner для считывания данных
```java
import java.util.Scanner;
public class Program {
  public static void main(String[] args){
    Scanner iScanner = new Scanner(System.in); //запуск метода
    System.out.printf("name: "); // выводим текст
    String name = iScanner.nextLine(); // определения получаемого типа (строка)
    System.out.printf("Привет, %s!", name) // вывод
    iScanner.close() // закрытие метода
  }
}
```

<br>

Проверка на соответствие получаемого типа

```java
import java.util.Scanner;
public class Program {
  public static void main(String[] args){
    Scanner iScanner = new Scanner(System.in);
    System.out.printf("int a: ");
    boolean flag = iScanner.hasNextInt(); // проверка на то, что пользователь ввёл число 
    System.out.printf(flag); // если вывело true - значит пользовател ввёл число, если fals - то нет.
    String name = iScanner.nextLine(); 
    System.out.printf("Привет, %s!", name) 
    iScanner.close() 
  }
}
```

<br>
 
Форматированный вывод

``` java
int a = 1, b = 2;
int c = a + b;
String res = a + " + " + b + " = " + c;
System.out.println(res); // 1 + 2 = 3
```

Что будет, если прибавить число к строке и сколько строк будет в итоге?
``` java
String s = "qwe"; // 1 строка
int a = 123;
String q = s + a; // 2 строка = а, т.к. будет неявное преобразование и 3-я строка = s+a которая положится в q = 4-я строка
System.out.println(q); // qwe123
```
Конкатенация строк - это плохой код, его нужно избегать т.к. сильно забивает память и делает сильную просадку.

___

<br>

# Логические операции
___

Присваивание 

Арифметические:

* фокусы с инкрементом и декрементом
  > i++ - постфиксный Инкремент 

  > --i - префиксный Декремент

  ```java
  int a = 123;
  a++;
  System.out.println(a); // 124
  ```
  ```java
  int a = 123;
  System.out.println(a++); // 123
  System.out.println(a); // 124
  ```
  ```java
  int a = 123;
  System.out.println(++a); // 124
  ```

Операции сравнения

Логические операции:
>|| - ИЛИ

>&& - И

>^ - Разделительное ИЛИ

>! - НЕ

Побитовые:
><< - побитовый сдвиг

>\>> - побитовый сдвиг

>& - Побитовое И (если встретит лож, больше не будет ничего проверять)

>| - побитовое ИЛИ (если первым встретит Истину, больше не будет ничего проверять, выведет true)

>^ - Разделительное ИЛИ

Пример побитового сдвига:
```java
int a = 8; 
// сдвигаем на 1 бит влево
System.out.println(a << 1); // 16
System.out.println(a >> 1); // 4
```
<br>

Пример использования побитового ИЛИ
```java
int a = 5; //101
int b = 2; //010
System.out.println(a | b); // 7 (111)
// сравниваем биты
// 101 смотрим по таблице истинности для ИЛИ
// 010 если одно выражение true, а другое fals = true
//-----
// 111 везде истина
```
<br>

Пример использования побитового И

```java
int a = 5; //101
int b = 2; //010
System.out.println(a & b); // 0 (000)
// сравниваем биты
// 101 смотрим по таблице истинности для И
// 010 если одно выражение true, а другое fals = fals
//-----
// 000 везде ложь
```

<br>

Пример использования разделительного ИЛИ
```java
int a = 5; //101
int b = 2; //010
System.out.println(a ^ b); // 7 (111)
// сравниваем биты
// 101 смотрим по таблице истинности для ИЛИ
// 010 если СТРОГО одно выражение true, а другое fals = true
//-----
// 111 везде истина
```

<br>

ФОКУСЫ Обычных и Побитовых логических операций
```java
int a = fals; 
int b = true; 
System.out.println(a && b); // fals - проверит только а и сразу закончит работу
System.out.println(a & b); // Exception - выдаст ошибку с описанием, что не так, т.к. обязательно провери оба выражения
```
```java
int a = true; 
int b = true; 
System.out.println(a || b); // true - т.к. первое выражение true - дальше смотреть не будет
System.out.println(a | b); // fals - т.к. проверит оба выражения и по таблице истинности, для ИЛИ, true и true = fals. Для ИЛИ должно быть СТРОГО только одно верное высказывание.
```
___

<br>

# Массивы
___
В Java у массивах обязательно должно быть указанна длина 
```java
int[] arr = new int[10];
System.out.println(arr.length); // 10
```
> массив из 10 числовых элементов

Присваивание элементу массива значение
```java
int[] arr = new int[10];
arr[3] = 13;
System.out.println(arr[3]); // 13 
```

<br>
<br>

```java
int[] arr = new int[] {1,2,3,4,5};
System.out.println(arr.length); // 5
```
> массив из 5-ти заранее обозначенных элементов

<br>
<br>

```java
int[] arr[] = new int[3][5];//способ 1
int[][] arr = new int[3][5];//способ 2
```
> двумерный массив
___

<br>

# Преобразования из одного типа в другой (явные)
```java
int i = 123;
double d = i; // не явное преобразование
byte b = Byte.parseByte(d); // явное преобразование
```
Но нужно быть осторожным, у каждого типа есть свой размер и если попытаться впихнуть в Byte число 1234 - программа упадёт с ошибкой.
___

<br>

# Область видимости переменных
___


```java
public class Program {
  public static void main(String[] args){
    int a = 123;
    {
      int a = 222;
      System.out.println(a);
    }
  }
}

```
>выведет ошибку

<br>

Переменная доступна только в своём блоке({}) кода. Если переменная находится за блоком, её можно использовать внутри блока, но из блока изъять переменную нельзя.
```java
public class Program {
  public static void main(String[] args){
    {
      int a = 222;
      System.out.println(a);
    }
    int a = 123;
    System.out.println(a); 
  }
}
```
>выведет:
>
>222
>
>123

# Функции и методы
В Java все функции являются методами.
Что бы описать функцию, должен быть класс и использование ключевого слова static
```java
public class Program {
 
 public static void main(String[] args) {
  sayHi(); // hi!
  System.out.println(sum(1, 3)); // 4
  System.out.println(factor(5)); // 120.0
 }
 static void sayHi() {
  System.out.println("hi!");
 }
 static int sum(int a, int b) {
  return a+b;
 }
 static double factor(int n) {
  if(n==1)return 1;
  return n * factor(n-1);
 }
}
```

<br>

Можно ещё создать свою библиотеку в отдельном файле, где будут храниться все нужные методы и обращения к ним идут через: **название_файла.название метода();**

```java
// файл lib.java
public class Program {
 public static void main(String[] args) {
    static void sayHi() { // метод приветствия
      System.out.println("hi!");
    }
    static int sum(int a, int b) { // метод сложения
      return a+b;
    }
    static double factor(int n) { // рекурсивный метод вычисления факториала
      if(n==1)return 1;
      return n * factor(n-1);
    }
  }
}

// файл program.java
public class Program {
 public static void main(String[] args) {
  lib.sayHi(); // hi! - вызываем метод из другого файла
 }
}
```
___

<br>

# Опрераторы в цикле
___
* Continum - как только выполнение программы доходит до этого оператора - программа уходит на следующий шаг цикла. Т.е. то, что было после оператора, на данном шаге, не выполнится, но цикл продолжит работать.

```java
for (int i = 0; i < 10; i++){
  if (i % 2 == 0){
    continum;
  }
  System.out.println(i); // 1,3,5,7,9
}
```

<br>

* break - ближайший цикл будет завершён
```java
for (int i = 0; i < 10; i++){
  if (i % 2 == 0){
    break;
  }
  System.out.println(i); // 0, 1 
}
```
```java
for (int i = 0; i < 10; i++){
  for (int j = 0; j < 5; j++){
    break; // будет остановлен цикл с j
  }
}
```

Использование continum и break считается плохим тоном... Типа быдлокод О_о Мол даже до увольнения... о_О

# for in (for each) для работы с коллекциями
```java
int[] arr = int[]{1,2,3,4,5,77};
for (int item : arr) { // взять элемент из коллекции (в данном случае массив) и произвести с ним некоторые действия
  System.out.println(item); // например распечатать
}
```
> выведет: 1,2,3,4,5,77

**Но!!**
если попытаться изменить переменные через цикл for - этого не произойдёт. Внутри цикла будет работа с переменной, которая никак не повлияет на изменения основной коллекции.

___

<br>

# API для Java
это контракт, который предоставляет программа. Использование функционала стороннего сервиса (телеграмм, вк, приложения, погода, карты).

# Строки
Создание миллиона плюсиков используя Тип **String**
```java
String str = "";
for (int i = 0; i < 1_000_000; i++){
  str += "+";
}
```
> скорость выполнения ~ 41000 ms (41 сек.)

<br>

Создание миллиона плюсиков используя Тип **StringBuilder**
```java
StringBuilder sb = "";
for (int i = 0; i < 1_000_000; i++){
  sb.append("+");
}
```
> скорость выполнения ~ 9 ms (0,9 сек)

<br>

# Методы строк
---
**concat()** - объединение строк

**valueOf()** - преобразует Object в строковое 
представление

**join()** - объединяет набор строк в одну с учётом разделителя

**charAt()** - получение сивола по индексу

**indexOf()** - первый индекс вхождения подстроки

**lastIndexOf()** - последний индекс вхождения подстроки

**startsWith() / endsWith()** - определяет, начинается/заканчтвается ли строка с подстроки

**replace()** - замена одной подстроки на другую

**split()** - делит строку на части и возвращает массив строк

>String - лучше использовать, если есть много изменений (если что-то разбираем)
>
>StringBuilder - лучше использовать, если есть много преобразований (если что-то собираем)

# Работа с файлами
___
Для работы с файлами нужно импортировать 2 библиотеки:

>import java.io.FileWriter;
>
>import java.io.IOException;

```java
import java.io.FileWriter;
import java.io.IOException;
public class Program {
 public static void main(String[] args) {
    try (FileWriter fw = new FileWriter("file.txt", false)) {
      fw.write("line 1"); // запись в файл line 1
      fw.append('\n');// добавить в конец строки
      fw.append('2');// добавить в конец строки
      fw.append('\n'); // добавить в конец строки
      fw.write("line 3"); // записать в файл line 3
      fw.flush(); // принудительная запись
    } catch (IOException ex) {
        System.out.println(ex.getMessage()); // для отслеживания ошибок getMessage() - выведет, какая именно ошибка произошла
    }
  } 
}

```
> try (FileWriter fw = new FileWriter("file.txt", false))
>
>try - для обработки ошибок
>
>FileWriter fw - определение экземпляра класса FileWriter
>
>new - идентификация FileWriter при помощи конструктора
>
>"file.txt" - в качестве конструктора будет название будущего файла 
>
>false - аргумент в зависимости, нужно или не нужно дописывать файл.
> 
>Если внести true - тогда, если файл есть, он будет дописываться, если нет - создаст новый
>
>Если false - тогда, даже если файл есть, он будет удалён и создан новый (перезаписан)

<br>

Чтение файла, посимвольно
```java
import java.io.*;
public class Program {
 public static void main(String[] args) throws Exception { // указываем, что main может упасть с ошибкой Exception это вместо блока try
    FileReader fr = new FileReader("file.txt");
    int c;
    while ((c = fr.read()) != -1) { //читать символы при помощи команды read()
      char ch = (char) c;
      if (ch == '\n') {
        System.out.print(ch);
      } else {
        System.out.print(ch);
      }
    }
  } 
}
```

<br>

Чтение файла построчно
```java
import java.io.*;
public class Program {
 public static void main(String[] args) throws Exception {
  BufferedReader br = new BufferedReader(new FileReader("file.txt")); // BufferedReader буферная запись
  String str;
  while ((str = br.readLine()) != null) { // читать строки при помощи команды readline
    System.out.printf("== %s ==\n", str);
  }
  br.close();
 }
}
```
___

<br>

# Работа с файловыми системами
---
для нахождения файла:

File имя_файла = new File(путь_к_файлу.расширение);

```java
String pathproject = System.getProperty("user.dir");// путь к текущей папки в которой запускается проект
String pathFile = pathProject.concat("/file.txt"); // указываем конкретный файл
File f3 = new File(pathFile); // создание файла и связь f3 по текущему пути
System.out.println(f3.getAbsolutePath()); // получаем абсолютный путь к файлу
```
> могут быть ошибки пути при работе с разными системами (винда, линукс...)
---

<br>

# Обработка ошибок try catch finally
Для отлавливания ошибок при работе с файлами используется блок **try catch finally**
```java
try{
  код, в котором может быть ошибка
} catch (Exception e) {
  Обработка, если ошибка случилась
}
finally{
  код, который выполнится в любом случае, не важно, была ошибка или нет
}
```
>Используется, например, когда нет файла, что бы программа не вылетала, вылезает сообщение "файл не найден" или "программа не может продолжить работу т.к. ..."


<br>

Пример:
```java
try{
  String pathproject = System.getProperty("user.dir"); 
  String pathFile = pathProject.concat("/file.txt");
  File f3 = new File(pathFile);
  System.out.println("try");
} catch (Exception e) {
  System.out.println("catch");
}
finally{
  System.out.println("finally");
}
```

<br>

Желательно этим блоком не пользоваться, поэтому часто используют проверку if else. Но всегда могут быть непредвиденные ошибки

```java
try{
  String pathproject = System.getProperty("user.dir"); 
  String pathFile = pathProject.concat("/file.txt");
  File f3 = new File(pathFile);
  if (file.createdNewFile()){ // проверка, что файл был создан
    System.out.println("file.created");
  } else {
    System.out.println("file.existed");
  }
} catch (Exception e) {
  System.out.println("catch");
}
finally{
  System.out.println("finally");
}
```
**isHidden()** - возвращает истину, если каталог или файл является скрытым

**length()** - возвращает размер файла в байтах

**lastModified()** - возвращает время последнего изменения файла или каталога

**list()** - возвращает массив файлов и подкаталогов, которые находятся в каталоге

**listFiles()** - возвращает массив файлов и подкаталогов, которые находятся в определённом каталоге

**mkdir()** - создаёт новый каталог

**renameTo(file dest)** - переименновывает файл или каталог


<br>

Работа с каталогами (папками)
```java
String pathProject = System.getProperty("user.dir");
String pathDir = pathProject.concat("/files");
File dir = new File(pathDir);
System.out.println(dir.getAbsolutePath ());
if (dir.mkdir()) {
System.out.println("+");
} else {
System.out.println("-");
}
for (String fname : dir.list()) {
System.out.println(fname);
}
```
---

<br>

# Логирование(Журналирование)
---
Позволяет при помощи API использовать некоторые функции.

Логирование - запись в журнал всех действий, для отладки систем и отлавливания ошибок.
Для использования логирования и внедрения в систему:
```java
Logger logger = Logger.getLogger(имя_класса_для_кого)
```
Уровни важности ошибок:
INFO

DEBUG

ERROR

WARNING

и т.д. 


<br>
Вывод (куда и в каком формате)

```java
Logger logger = Logger.getLogger(Ex005_Logger.class.getName());
ConsoleHandler ch = new ConsoleHandler(); // все сообщения будут выводиться в терминал

logger.addHandler(ch); // указываем вывод консоли в качестве аргумента для logger

SimpleFormatter sFormat = new SimleFormatter(); // записываем формат, в рамкох которого будет производиться запись этих сообщения. Это классический текстовый формат
ch.setFormatter(sFormat);

logger.log(Level.WARNING, "Тестовое логирование 1");// вариант 1 -позволяет указать уровень сообщений и то сообщение которое требуется показать (но это не обязательно)
logger.info("Тестовое логирование 2"); //вариант два, упрощённый код.
```
```java
Logger logger = Logger.getLogger(Ex005_Logger.class.getName());
ConsoleHandler ch = new ConsoleHandler();

logger.addHandler(ch); 

XMLFormatter xml = new XMLFormatter(); // XML формат
ch.setFormatter(xml);

logger.info("Тестовое логирование 2");
```
```java
Logger logger = Logger.getLogger(Ex005_Logger.class.getName());
FileHandler fh = new FileHandler("log.xml");// создание и запись лога в файл (текстовый формат можно в txt)

logger.addHandler(fh); 

XMLFormatter xml = new XMLFormatter(); // XML формат
fh.setFormatter(xml);

logger.info("Тестовое логирование 2");
```

# тип данных Object
**Упаковка** - любой тип можно положить в переменную типа Object

**Распаковка** - преобразование Object - переменной в нужный тип

**Иерархия типов** - любой тип ниже Object
```java
Object o = 1; 
GetType(o); // java.lang.Integer
o = 1.2; 
GetType(o); // java.lang.Double

static void GetType(Object obj) {
 System.out.println(obj.getClass().getName());
 }
```

<br>

При помощи Object, который може хранить любой тип и давать информацию о нём, можно усовершенствовать некоторые методы, которые предпологают использование изменяющихся аргументов
```java
public static void main(String[] args) {
 System.out.println(Sum(1, 2)); // int, int
 System.out.println(Sum(1.0, 2)); // double, int
 System.out.println(Sum(1, 2.0)); // int , double
 System.out.println(Sum(1.2, 2.1)); // double, double
}

static Object Sum(Object a, Object b) {//возвращаем Object и ипользуем объекты для переменных
  
 if (a instanceof Double && b instanceof Double) {// если а относится к типу double И b относится к типу double
  return (Object)((Double) a + (Double) b); // вернуть Объект (сложения double a и b)
 } else if(a instanceof Integer && b instanceof Integer) {
  return (Object)((Integer) a + (Integer) b); // явное приведение типов нужно для наглядного описания, какие типы возвращаются (это не обязательно)
 } else return 0;
}

```
> стараться использовать Object как можно меньше


<br>

# Массивы
Увеличение размера массива

```java
int[] a = new int[] { 1, 9 };//есть некий массив с длиной 2
int[] b = new int[3]; // создали новый пустой массив с длиной 3
System.arraycopy(a, 0, b, 0, a.length);//копирование одного массива в другой начиная с нулевого элемента и всю длину первого масства
for (int i : a) { System.out.printf("%d ", i);} // 1 9
for (int j : b) { System.out.printf("%d ", j);}

```

<br>

при помощи создания методов
```java
public static void main(String[] args) {
 int[] a = new int[] { 0, 9 }; // наш массив
 for (int i : a) { System.out.printf("%d ", i); }
 a = AddItem(a, 2); // вызываем метод в который передаём массив и значение, которое вложим в конец нового массива
 a = AddItem(a, 3);
 for (int j : a) { System.out.printf("%d ", j); }
}

static int[] AddItem(int[] array, int item) {// используем метод в который передаём массив и переменную, которую будем добавлять в конец нового массива
 int length = array.length; // сохраняем длину первого массива
 int[] temp = new int[length + 1]; // создаём новый массив сохраняя в него увеличинную длину от первого массива
 System.arraycopy(array, 0, temp, 0, length); // копируем все данные из первого массива в новый
 temp[length] = item; // в последний элемент вкладываем аргумент который передавали для добавления в конец массива
 return temp; // возвращаем новый массив
}
```

<br>

# Иерархия списков. ArrayList
ArrayList - немного медленнее массивов, но гораздо удобнее.
Разные способы создания
```java
ArrayList<Integer> list1 = new ArrayList<Integer>();
ArrayList<Integer> list2 = new ArrayList<>();
ArrayList<Integer> list3 = new ArrayList<>(10);
ArrayList<Integer> list4 = new ArrayList<>(list3);

```
List - пронумерованный набор элементов. 

Пользователь этого интерфейса имеет точный контроль на тем, где в списке вставляется каждый элемент.

Пользователь может обращаться к элементам по их целочисленному индексу (позиции в списке) и искать элементы в списке. (методы: ArrayList, LinkedList(устаревшие: Vector, Stack))
```java
List list = new ArrayList(); // можно явно прописать ArrayList
list.add(2809); // добавляем некое значение
// если явно не указать тип передаваемого значения - это считается сырым типом (неявное преобразование к Object)
list.add("string line"); // при использовании сырого типа, код скомпилируется
for (Object o : list) {
  System.out.println(o);
}
```

<br>

Явная типизация (обобщение)
```java
ArrayList<Intger> list = new ArrayList<Integer>();
list.add(2809);
list.add("string line"); // т.к. явно указан тип значений, которые должны храниться в массиве - код упадёт с ошибкой
for (Object o : list) {
  System.out.println(o);
}
```

<br>

* Row Type (сырые данные)
```java
List list = new ArrayList();
list.add(2809);
list.add("string line");
for (Object o : list) {
  System.out.println(o);
}
```

<br>

* Save Tape (явное обобщение (типизация))
Избавит от кучи ошибок во время работы с кодом
```java
List<Integer> list = new ArrayList<Integer>();
list.add(1);
list.add(123);
// list.add("string line");
for (Object o : list) {
  System.out.println(o);
}
```

<br>

# Методы списков (функционал)
**add(arg)** - добавляет элемент в список (на нужную позицию) add(arg,pos)

**list2.addAll(list1)** - добавть все элементы из list1 в list2 

**get(pos, elem)** - возвращает эл. из списка по указанной позиции

**indexOf(item)** - ищет эл и возвращает его индекс с начала списка

**lastIndexOf(item)** - ищет эл и возвращает его индекс с конца списка

**remove(pos)** - удаление эл - та на указанной позиции и его возвращение

**set(int pos, T item)** - Возвращает элемент списка по указанному индексу

**sort(Comparator)** - сортирует набор данных по правилу
```java
list = [3,4,2,5,1];
list.sort(Comparator.naturalOrder());
list = [1,2,3,4,5]
```
```java
list = [3,4,2,5,1];
list.sort(Comparator.reversOrder());
list = [5,4,3,2,1]
```
```java
//можно написать свой компаратор
list.sort(new Comparator <Integer>(){
  public int compare(Integer o1, Ibteger o2){
    if (o1 % 3 != 0 && o2 > 6) return 0;
    if (o1 % 3 != 0 && o1 == 1) return 1;
    return -1;
  }
});
```


**subList(int start, int end)** - получение набора данных от позиции start до end

**clear()** – очистка списка

**toString()** – «конвертация» списка в строку

**Arrays.asList** – преобразует массив в список

**containsAll(col)** – проверяет включение всех элементов из col

**list1.removeAll(list2)** – удаляет иэлементы из list1, которые находятся в list2 
```java
list1 = [1,2,3,4,5];
list2 = [2,4,5,7,8];
list1.removeAll(list2); = [1,3,4]
list2.removeAll(list1); = [7,8]
```

**list1.retainAll(list)** – оставляет элементы перечения list1 с list2
```java
list1 = [1,2,3,4,4,5];
list2 = [2,4,5,5,7,8];
list1.retainAll(list2); = [2,4,4,5]
list2.retainAll(list1); = [2,4,5,5]
```

**toArray()** – конвертация списка в массив Object’ов

**toArray(type array)** – конвертация списка в массив type

**List.copyOf(col)** – возвращает копию списка на основе имеющегося

**List.of(item1, item2,...)** – возвращает неизменяемый список

**size()** - вернёт размер списка (как length в массиве)

**isEmpty()** - возвращает истину или ложь в зависимости, есть ли элементы в списке

**clear** - очистка списка

<br>

```java
int day = 29;
int month = 9;
int year = 1990;
Integer[] date = { day, month, year };
List<Integer> d = Arrays.asList(date);
System.out.println(d); // [29, 9, 1990]
```
```java
StringBuilder day = new StringBuilder("28");
StringBuilder month = new StringBuilder("9");
StringBuilder year = new StringBuilder("1990");
StringBuilder[] date = new StringBuilder[] { day, month, year }; // создаём массив date
List<StringBuilder> d = Arrays.asList(date); // создаём коллекцию d
System.out.println(d);// [29, 9, 1990]
date[1] = new StringBuilder("09");// меняем значение в массиве
System.out.println(d); // [29, 09, 1990] значение в коллекции изменится
```

<br>

Создание массива через list.of и его приключения
```java
Character value = null;
List<Character> list1 =
List.of('S', 'e', 'r', 'g', 'e', 'y');// создание массива символов на основе list.of
System.out.println(list1);
list1.remove(1); // при попытки удалить элемент - выпадет ошибка, т.к. коллекция создана при помощи List.of
List<Character> list2 = List.copyOf(list1);
```
Если создать через ArrayList и попытаться удалить элемент
```java
Character value = null;
List<Character> list1 = new ArrayList<Character>();
list1.add('S');
list1.add('e');
list1.add('r');
list1.add('g');
list1.add('e');
list1.add('y');
System.out.println(list1);// [S, e, r, g, e, y]
list1.remove(1); 
System.out.println(list1);//[e, r, g, e, y]
List<Character> list2 = List.copyOf(list1);
```
# Итератор (итерация объектов)
Итераторы позволяют вызывающей стороне удалять элементы из
базовой коллекции во время итерации с четко определенной
семантикой.

<br>


**Есть классический итератор  Iterator<E>:**

hasNext() - если есть следующий эл. (с лева на право)

next() - взять этот следующий элемент

remove() - удаление

<br>


**Более обобщённый ListIterator<E>:** 

hasPrevious() - если есть предыдущий эл (с права на лево)

E previous(), 

nextIndex(), 

previousIndex(), 

set(E e), 

add(E e)


```java
List<Integer> list = List.of(1, 12, 123, 1234, 12345);

for (int item : list){ // forEach - упрощённая версия iterator (в forEach нельзя изменять эл-ты)
  System.out.println(item); 
}

Iterator<Integer> col = list.iterator();// получаем на основе коллекции list итератор

while (col.hasNext()) { // пока есть следующий элемент
  System.out.println(col.next()); // дай этот следующий элемент
  // col.next(); если попытаться ещё раз вызвать next - будет ошибка
  // col.remove(); если попытаться удалить элемент - будет ошибка
  int i = col.next();
  col.remove(); // удалит элемент
}
```
Движение итератора с последнего элемента
```java
Listiterator<Integer> iterator = list.listIterator(list.size()-1); // с последнего элемента
while(iterator.hasPrevious()){ // пока есть предыдущий элемент
  int i = iterator.previous();
  System.out.println(i);
  iterator.remove();
}
```

<br>

Однострочный forEach (в 8-й джаве появился)
```java
list.forEach(n -> System.out.println(n)); //переберёт и выведет все элементы (те же ограничения, что и в обычном)
```

# Приоритетные списки (LinkedList)
Представляет собой двусвязный список

Список - гибкая структура данных, позволяющая легко менять свой размер. Элементы доступны для вставки или удаления в любой позиции.

**односвязный список**
Если хранится информация о следующем элементе

Если последний элемент имеет информацию о следующем элементе (т.е. первом) - это **циклический односвязный** список

**двусвязный список**
Если хранится информация о следующем и предыдущем элементе

Если последний элемент имеет информацию о следующем элементе (т.е. первом), а первый элемент о предыдущем (т.е. последним) - **двунаправленный циклический список**

LinkedList нужен для небольшого количества элементов, в которых операции добавления\удаления встречаются чаще операций чтения.

LinkedList использует тот же функционал, что и ArrayList

```java
LinkedList<Integer> ll = new LinkedList<Integer>();

ll.add(1);
ll.add(2);
ll.add(3);
```

<br>

# Списки Queue
Какой элемент первый пришёл, тот и будет первым обработан

```java
Queue<Integer> queue = new LinkedList<Integer>();
queue.add(n);
```

Для добавления эл-та в переменную, но элементы в памяти располагаются в разном порядке
```java
Queue<Integer> queue = new LinkedList<Integer>();
ll.add(1);
ll.add(2);
ll.add(3); // [1,2,3]
int item = queue.remove();// удалиться первый элемент, который был добавлен. Т.е. [2,3]
```

# PriorityQueue
Наивысший приоритет имеет «наименьший» элемент.
```java
PriorityQueue<Integer> pq = new PriorityQueue<Integer>();
pq.add(123);
pq.add(3);
pq.add(13);
pq.add(1);
System.out.println(pq); // [1,3,13,123]
// посмотрим порядок извлечения
System.out.println(pq.poll()); // 1
System.out.println(pq.poll()); // 3
System.out.println(pq.poll()); // 13
```
# Deque
Линейная коллекция, которая поддерживает вставку и удаление элементов на обоих концах.

```java
public static void main(String[] args) {
 Deque<Integer> deque = new ArrayDeque<>();
 deque.addFirst(1); deque.addLast(2);
 deque.removeLast(); deque.removeLast();
 deque.offerFirst(1); deque.offerLast(2);
 deque.pollFirst(); deque.pollLast();
 deque.getFirst(); deque.getLast();
 deque.peekFirst(); deque.peekLast();
 }

```
# Stack (устаревшая коллекция списков)
Stack представляет собой обработку данных по принципу LIFO. Те данные которые пришли первыми, обрабатываются в последнюю очередь (альтернатива Stack - рекурсия, но рекурсия тяжёлая и долгая)

Расширяет Vector пятью операциями, которые позволяют рассматривать
вектор как стек.

push(E item)

pop()

```java
Stack<Integer> stack = new Stack<>();
 stack.push(1);
 stack.push(12);
 stack.push(123);
 System.out.println(stack.pop()); // 123
 System.out.println(stack.pop()); // 12
 System.out.println(stack.pop()); // 1
```

<br>
Вычислить значение выражения в постфиксной форме записи

>1 + 2 * 3 - есть пример
>
>123*+ - посфиксная форма записи
>
>бует в стеке
>
>3 /// * как только доходит до математических символов, берутся 2 последних элемена и используем:
>
>2 /// 6 /// + было умножение 2 и 3
>
>1 /// 1 /// 7 /// было сложение 6 и 1

>(1 + 2) * 3
>
>12+3*
>
>\+ /// * ///
>
>2 /// 3 /// 
>
>1 /// 3 /// 9


# Коллекции из множества MAP
Map – это множество коллекций, работающих с данными по принципу <Ключ / Значение>. Ключь всегда должен быть уникальным, а значения нет.

# HashMap
В HashMap элементы располагаются как угодно и могут менять свое положение.

Хэш функции - возвращают цифры (в большинстве (всегда) случаев)

Ключевые особенности:

● ускоренная обработка данных;

● порядок добавления не запоминается.

● допускаются только уникальные ключи, значения
могут повторяться;

● Может содержать в качестве ключа null (это плохо и за этим надо следить)

```java
public class Ex001_HashMap {
 public static void main(String[] args) {
  Map<Integer, String> db = new HashMap<>(); // мап ключ, значение
  db.putIfAbsent(1, "один"); System.out.println(db); // метод делает проверку, что если такой ключь есть, то ничего не будет добавляться, если нет, он создатся
  db.put(2, "два"); System.out.println(db); // добавление в коллекцию ключ и значение
  db.put(2, "три"); System.out.println(db); // значение перезапишется
  db.put(null, "!null"); System.out.println(db); // добавление константного ключа null
  System.out.println(db.containsValue(value:"один"));// true - проверка на значение 
  System.out.println(db.containsKey(value:1)); // true - проверка на ключь
  System.out.println(db.keySet()); // вывести всю коллекцию ключей
  System.out.println(db.values()); // вывести всю коллекцию значений
 }
}
```

# Функционал HashMap
put(K,V) – добавить пару если или изменить значение,если ключ имеется.

putIfAbsent(K,V) – произвести добавление если ключ не найден.

putAll(new HashMap<>()) - добавить все элементы из другого словаря 

get(K) - получение значения по указанному ключу.

getOrDefault(k, "def") - поиск по ключу. Если ключ найден - выведет его значение. Если нет, выведет дефолтное значение

replace(k, newV) || replace(k, oldV, newV) - перезапись значения по данному ключу. Если ключа нет - будет ошибка.
```java
hashMap.replace(1,"1",  "2");
```

remove(K) – удаляет пару по указанному ключу.

containsValue(V) – проверка наличия значения.

containsKey(V) – проверка наличия ключа.

keySet() – возвращает множество ключей.

values() – возвращает набор значений.

compute(k, (k,v)) -> - изменения значения по данному ключу
```java
hashMap.compute(1, (k, v) -> v += k); // к значению v прибавится ключ (сложение строк)
```

computeIfPresent(k, (k,v)) -> "" - изменение значения только тогда, когда найден ключ

computeIfAbsent(k, v -> "") - срабатывает только тогда, когда нет данного ключа (добавит пару)

merge(k, v, (oldV,newV) -> "") - 1пар. - ключ, 2пар. - новое значение. (3пар.-старое значение, 4пар. - новое значение) -> что с этим делаем. Изменение значения по ключу
```java
hashMap.put(1,"One");
hashMap.merge(1, "!", (oldV, newV) - > oldV + newV); // 1 = One!
```

<br>

Проход по коллекции при помощи forEach

```java
Map<Integer, String> db = new HashMap<>();
 db.putIfAbsent(1, "один");
 db.put(2, "два");
 db.put(3, "три");
 System.out.println(db);
 for (var item : db.entrySet()) {
  System.out.printf("[%d: %s]\n", item.getKey(), item.getValue()); // getKey - получение ключа и getValue - получение значений
 }
```
ускорение работы HashMap
```java
Map<Integer,String> map1 = new HashMap<>(); // стандартное объявление
 Map<Integer,String> map2 = new HashMap<>(9); // указание кол-ва элементов
 Map<Integer,String> map3 = new HashMap<>(9, 1.0f); // указание кол-ва эл-тов и вторым, в процентном соотношении, до которого момента нужно заполнять текущие значения, для того, что бы произвелось удвоения кол-ва элементов в хранилище
```

<br>

Для самостоятельного изучения:
* Хэш-функции и хэш-таблицы

* Прямое связывание (хэширование с цепочками)

* Хэширование с открытой адресацией

* Теория графов:

  * деревья построенные на списках

  * бинарные деревья

  * сбалансированные деревья

  * *алгоритм балансировки дерева

  * ** красно-черные деревья, деревья поиска

# TreeMap
В процессе добавления, пары будут упорядочиваться
по ключу, поэтому этим коллекциям обязательно нужно указывать, по какому принципу будет упорядочивание. (через компаратор например) Добавление парами.

# Функционал TreeMap
put(K,V) – добавить пару если или изменить значение,если ключ имеется.

get(K) - получение значения по указанному ключу.

remove(K) – удаляет пару по указанному ключу.

descendingKeySet(V) - полчение всех ключей или значений

descendingMap() - показато в обратном порядке

tailMap() - показать кол-во эл. больше чем

headMap() - кол-во эл. меньше чем

lastEntry() - 

firstEntry()

```java
TreeMap<Integer,String> tMap = new TreeMap<>();
 tMap.put(1,"один"); System.out.println(tMap);
 // {1=один}
 tMap.put(6,"шесть"); System.out.println(tMap);
 // {1=один, 6=шесть}
 tMap.put(4,"четыре"); System.out.println(tMap);
 // {1=один, 4=четыре, 6=шесть}
 tMap.put(3,"три"); System.out.println(tMap);
 // {1=один, 3=три, 4=четыре, 6=шесть}
 tMap.put(2,"два"); System.out.println(tMap);
 // {1=один, 2=два, 3=три, 4=четыре, 6=шесть}
```

# LinkedHashMap
Помнит порядок добавления элементов ➜ более медлительный. Добавление так же парами. Использует так же все функции, что и HashMap

```java
Map<Integer,String> linkmap = new LinkedHashMap<>();
 linkmap.put(11, "один один");
 linkmap.put(1, "два");
 linkmap.put(2, "один");
 System.out.println(linkmap); // {11=один один, 1=два, 2=один}
 Map<Integer,String> map = new HashMap<>();
 map.put(11, "один один");
 map.put(2, "два");
 map.put(1, "один");
 System.out.println(map); // {1=один, 2=два, 11=один один}

```

# HashTable
«Устаревший брат» коллекции HashMap,
который не знает про null. Добавление так же парами. Использует так же все функции, что и HashMap

```java
Map<Integer,String> table = new Hashtable<>();
 table.put(1, "два");
 table.put(11, "один один");
 table.put(2, "один");
 System.out.println(table); // {2=один, 1=два, 11=один один}
 // table.put(null, "один"); // java.lang.NullPointerException
```
____

<br>

# Set (Множества)
- Коллекции, содержащие уникальные элементы.
- Быстрая работа с данными
- "Основан" на Map`ах без пары
- Порядок добавления не хранится

# HashSet
isEmpty() - проверка на пустоту

add(v) - добавление эллемента в коллекцию

remove(v) - удаление эл. из коллекции

contains(v) - проверка на включение элемента в коллекцию

clear() - удаление всех элементов коллекции

size() - возвращает количество эл. коллекции

```java
Set<Integer> set = new HashSet<>();
set.add(1); set.add(12); set.add(123); // добавление эл-та
set.add(1234); set.add(1234);
System.out.println(set.contains(12)); // true
set.add(null);
System.out.println(set.size()); // 5
System.out.println(set); // [null, 1, 1234, 123, 12]
set.remove(12); // удаление
for (var item : set) System.out.println(item); // null 1 1234 123
set.clear(); // очищение
System.out.println(set); // []
```

addAll(Coll) – объединение множеств.

retainAll(Coll) – пересечение множеств.

removeAll(Coll) – разность множеств.

```java
var a = new HashSet<>(Arrays.asList(1,2,3,4,5,6,7));
var b = new HashSet<>(Arrays.asList(2,3,5,7,11,13,17));
var u = new HashSet<Integer>(a); u.addAll(b);
var r = new HashSet<Integer>(a); r.retainAll(b);
var s = new HashSet<Integer>(a); s.removeAll(b);
System.out.println(a); // [1, 2, 3, 4, 5, 6]
System.out.println(b); // [17, 2, 3, 5, 7, 11]
System.out.println(u); // [1, 17, 2, 3, 4, 5, 6, 11]
System.out.println(r); // [2, 3, 5, 7]
System.out.println(s); // [1, 4, 6]
boolean res = a.addAll(b);
```
first()

last()

headSet(E) - меньше чем

tailSet(E) - больше и равно

subSet(E1, E2) - в диапазоне от (включительно ОТ) до (не включительно)

```java
var a = new TreeSet<>(Arrays.asList(1,7,2,3,6,4,5));
 var b = new TreeSet<>(Arrays.asList(13,3,17,7,2,11,5));
 System.out.println(a); // [1, 2, 3, 4, 5, 6, 7]
 System.out.println(b); // [2, 3, 5, 7, 11, 13, 17]
 System.out.println(a.headSet(4)); // [1, 2, 3]
 System.out.println(a.tailSet(4)); // [4, 5, 6, 7]
 System.out.println(a.subSet(3, 5)); // [3, 4]
```

<br>

# TreeSet
- в основе HashMap

- Упорядочен по возрастанию

- не должно быть null

```java
var a = new TreeSet<>(Arrays.asList(1,7,2,3,6,4,5));
var b = new TreeSet<>(Arrays.asList(13,3,17,7,2,11,5));
System.out.println(a); // [1, 2, 3, 4, 5, 6, 7]
System.out.println(b); // [2, 3, 5, 7, 11, 13, 17]
System.out.println(a.contains(1)); // true
```

# LinkedHashSet

- в основе HashMap

- помнит порядок добавления

Используется когда нужен HashSet с запоминанием порядка элемента

isEmpty() – проверка на пустоту.

add(V) – добавление элемента в коллекцию.

remove(V) – удаление элемента из коллекцию.

contains(V) – проверка на включение элемента в коллекции.

clear() – удаление всех элементов коллекции.

size() – возвращает количество элементов коллекции.

```java
var a = new LinkedHashSet<>(Arrays.asList(1,7,2,3,6,4,5));
var b = new LinkedHashSet<>(Arrays.asList(13,3,17,7,2,11,5));
a.add(28);
System.out.println(a); // [1, 7, 2, 3, 6, 4, 5, 28]
System.out.println(b); // [13, 3, 17, 7, 2, 11, 5]
```

<br>

# Создание собственных типов

Java является объектно-ориентированным языком.

Программа, написанная на Java, должна соответствовать
парадигме объектно-ориентированного программирования.
Следует понимать, что принципы ООП не просто определяют
структуру программы. Это некий фундаментальный подход,
с которым нам предстоит разобраться.

Спагетти-код – код, в котором данные связаны с методами
для их обработки и в итоге может получиться так, что отдельные
ветви алгоритма переплетаются, образуя запутанный клубок,
в котором невозможно разобраться

Решение проблемы получило название объектно-ориентированное
программирование или объектно-ориентированное проектирование или ООП.

При использовании данного подхода, упорядочивание кода базируется
на объединении данных, с одной стороны, и методов для обработки этих
данных, с другой стороны, в одно целое. Это «одно целое» в ООП называется
экземпляром класса.

Вся программа при этом имеет блочную структуру, что существенно упрощает
анализ кода и внесение в него изменения.

ООП – искусственный прием, в большинстве случаев не зависящий, от языка
программирования.

Если говорят, что разработка идет с использованием ООП – это говорит о
том, что используются классы и экземпляры этих классов.
Каждый экземпляр класса определяется общим шаблоном, который
называется классом.

В рамках класса задается общая структура, на основе которой затем
создаются экземпляры.

Данные, относящиеся к классу, называются полями класса, а код для их
обработки — методами класса

___

<br>

```java
// Создаём файл под названием Worker.java и работаем в нём

public class Worker { // класс работник (сущность)
  int id; // идентификатор
  int salary; // заработная плата
  String firstName; // имя
  String lastName; // фамилия
}

```

Клиентский код - код, который вызывает эхкземпляр класса

```java
// создаём другой файл, общий, где будем создавать экземпляры работников
public static void main(String[] args){
  Worker w1 = new Worker(); // создание экземпляра (конструктор)
  w1.firstName = "Имя_1";
  w1.lastName = "Фамилия_1"; 
  w1.salary = 100;
  w1.id = 1000;

  Worker w4 = new Worker(); 
  w4.firstName = "Имя_1";
  w4.lastName = "Фамилия_1"; 
  w4.salary = 100;
  w4.id = 1000;

  Worker w2 = new Worker(); 
  w2.firstName = "Имя_2";
  w2.lastName = "Фамилия_2"; 
  w2.salary = 200;
  w2.id = 2000;

  System.out.println(w1 == w4); // false попытка сравнить 2 экземпляра с одинаковыми данными
  System.out.println(w1.equals(w4)); // false попытка сравнить 2 экземпляра с одинаковыми данными

  var workers = new HashSet<Worker>(Arrays.asList(w1,w2)); // наполнение коллекции экземплярами
  System.out.println(workers.contains(w4)); // false попытка определить значения этого экземпляра в других

   System.out.println(w1); // попытка вывести экземпляр - выведет хэш-код экземпляра
}
```
Что бы суметь вывести в консоль значения экземпляра, нужно вернуться в файл Worker.java

```java
public String toString(){ // создаём класс, который будет переводить в строку нужныем нам данные
  return String res = String.format("id:%d,  Name:%s, S_Name:%s, salary:%d", id, firstName, lastName, salary); // создаём переменную, вкладываем в неё все значения, которые хотим распечатать и возвращаем.
}
```
И теперь в клиентском коде можно смело выводить значения
```java
System.out.println(w1); // id:Имя_1, Name:Фамилия_1, S_Name:100, salary:1000
```

Теперь, что бы сравнить два экземпляра и это работало так, как нам нужно - придётся поменять базоваое поведение метода equals

Для этого возвращаемся в класс Worker.java

```java
// сравнивать только по одному - два полю сравнивать нельзя, это тестовый код. Код в реальности сложнее.
public boolean equals(Object obj) { // equals принимает объект
  var t = (Worker) obj; // этот объяект соединяем с worker, который нам дали и записывам в переменную. т.е. вместо t будет wirker
  return id == t.id && firstName == t.firstName // если id текущего воркера совпадает с тем, что у дали и имя совпадает с тем именем, которое находится в воркере, то считаем, что эти два сотрудника равны.
}

// 
public int hashCode(){
  return id
}
```
И теперь код сравнивания сработает в клиентском файле

```java
System.out.println(w1 == w4); // false
System.out.println(w1.equals(w4)); // true т.к. мы переобпределили логику сравнивания
```
