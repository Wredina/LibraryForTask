# SOAP API

**SOAP** (от англ. Simple Object Access Protocol — простой объект с доступом протокола) — протокол
обмена структурированными сообщениями в распределённой вычислительной среде. Протокол
используется для обмена произвольными сообщениями в формате XML.

SOAP используется с различными протоколами, таким как SMTP, FTP, HTTP, HTTPS. Чаще всего — с
HTTP, как с наиболее универсальным: его поддерживают все браузеры и серверы.

**SOAP API** — это веб-сервис, использующий протокол SOAP для обмена сообщениями между
серверами и клиентами. При этом сообщения должны быть написаны на языке XML в соответствии
со строгими стандартами, иначе сервер вернёт ошибку.

# Основные определения

## XML

**XML** (или Extensible Markup Language) — это простой, очень гибкий текстовый формат,
устанавливающий набор правил для структурирования сообщений. XML создали для удобного
хранения и передачи данных. У XML есть ряд преимуществ, которые позволяют успешно справляться
с этой задачей. Например, его может прочитать абсолютно любой желающий:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<book>
  <title>iPhone 12 Pro</title>
  <memory>512</memory>
  <price>100 000</price>
</book>
```

А также при передаче данных от клиента на сервер и наоборот нет проблем с совместимостью
данных

## XSD

XSD (XML Schema Definition) — язык описания структуры XML-документа. Он используется для
определения правил, которым должен подчиняться документ, и был разработан, чтобы его можно
было использовать в создании программного обеспечения для обработки XML-документов. Файл,
содержащий XML Schema, обычно имеет расширение «.xsd» (XML Schema definition). Перед
тестированием SOAP первым делом необходимо проверить документацию XSD, так как там довольно
часто встречаются ошибки (например, некорректно заданы ограничения).

В XML Schema Definition необходимо понимать описание типов данных и наложение ограничений на
возможные значения. Например, сервис сам сможет валидировать полученные данные и
возвращать пользователю ошибку.

В следующем примере определяется элемент age с ограничением. В этом элементе предполагается
указывать возраст человека, а возраст человека, как известно, не может быть меньше 0 и больше
120:

```xml
<xs:element name="age">
  <xs:simpleType>
    <xs:restriction base="xs:integer">
      <xs:minInclusive value="0"/>
      <xs:maxInclusive value="120"/>
    </xs:restriction>
  </xs:simpleType>
</xs:element>
```

В следующем примере определяется другой элемент password с ограничением. Длина его значения
должна быть минимум 5 и максимум 8 символов:

```xml
<xs:element name="password">
  <xs:simpleType>
    <xs:restriction base="xs:string">
      <xs:minLength value="5"/>
      <xs:maxLength value="8"/>
    </xs:restriction>
  </xs:simpleType>
</xs:element>
```

Как уже было сказано выше, схема подключается и находится в отдельном файле:

```xml
<?xml version="1.0"?>
<note xmlns="http://mysite.ru"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://mysite.ru note.xsd">
  <title>iPhone 12 Pro</title>
  <memory>512</memory>
  <price>100 000</price>
</note>
```

Фрагмент xmlns:xs="<http://www.w3.org/2001/XMLSchema>" указывает на то, что используемые в схеме
элементы и типы данных относятся к пространству имён "<http://www.w3.org/2001/XMLSchema>".
Также здесь указывается, что элементы и типы данных, относящиеся к пространству имён
"<http://www.w3.org/2001/XMLSchema>", должны иметь префикс xs:

Фрагмент targetNamespace="<http://msiter.ru>" указывает на то, что определяемые этой схемой
элементы (note, to, from, heading, body) относятся к пространству имён "<http://msiter.ru>".

Фрагмент xmlns="<http://mysite.ru>" указывает на то, что пространством имён по умолчанию является
"<http://mysite.ru>"

XML схемы предназначены для определения допустимых строительных блоков XML документа. XML
схема определяет :

- элементы, которые могут появляться в XML документе;
- атрибуты, которые могут появляться в XML документе;
- какие элементы являются дочерними;
- порядок дочерних элементов;
- количество дочерних элементов;
- пустой ли элемент или может содержать текст;
- типы данных элементов и атрибутов;
- фиксированные значения и значения по умолчанию элементов и атрибутов.

Комментарии могут появляться в любом месте документа за пределами другой разметки, кроме
того, они могут появляться в объявлении типа документа в местах, разрешённых грамматикой. Они
не являются частью символьных данных документа.

Пример комментариев:
<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/1.jpg?raw=true">

Таблица ограничения для типов данных
<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/2_1.jpg?raw=true">
<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/2_2.jpg?raw=true">

## WSDL

**Web Services Description Language** (WSDL) — это язык на основе XML, который используется для
описания веб-сервисов. Эта аббревиатура также используется для любого конкретного
WSDL-описания сервиса. Описание представляет собой текстовый WSDL-файл, который содержит
описание того, как можно вызвать службу, какие параметры она ожидает и в каком формате она
возвращает данные. Документ WSDL использует следующие элементы в определении сетевых
служб:

- Типы — контейнер для определений типов данных с использованием некоторой системы
типов (например, XSD).
- Сообщение — абстрактное типизированное определение передаваемых данных.
- Операция — абстрактное описание действия, поддерживаемого сервисом.
- Тип порта — абстрактный набор операций, поддерживаемых одной или несколькими
конечными точками.
- Привязка — конкретный протокол и спецификация формата данных для определённого типа
порта.
- Порт — единая конечная точка, определяемая как комбинация привязки и сетевого адреса.
- Сервис – набор связанных конечных точек.

# Структура SOAP-сообщения

Корректное SOAP-сообщение состоит из нескольких структурных элементов: Envelope, Header, Body
и Fault.

```xml
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <getProductDetails xmlns="http://warehouse.example.com/ws">
      <productID>8239</productID>
    </getProductDetails>
  </soap:Body>
</soap:Envelope>
```

В самой первой строке объявляется XML.

```xml
<?xml version="1.0" encoding="utf-8"?>
```

Объявление XML указывает версию языка, на которой написан документ. Поскольку интерпретация
содержимого документа зависит от версии языка, то Спецификация предписывает начинать
документ с объявления XML. В первой (1.0) версии языка использование объявления не было обязательным, в последующих версиях оно обязательно. Таким образом, версия языка определяется
из объявления, и если объявление отсутствует, то принимается версия 1.0.

Кроме версии XML объявление может также содержать информацию о кодировке документа и
«оставаться ли документу со своим собственным DTD (DTD («document type definition») — позволяет
определить список разрешённых элементов для какой-то сущности в XML-файле.), или с
подключённым».

**Envelope («конверт»)**. Это корневой элемент. Определяет XML-документ как сообщение SOAP с
помощью пространства имён xmlns:soap=»<http://www.w3.org/2003/05/soap-envelope/»>. Если в
определении будет указан другой адрес, сервер вернёт ошибку.

**Header («заголовок»)**. Включает в себя атрибуты сообщения, связанные с конкретным приложением
(аутентификация, проведение платежей и так далее). В заголовке могут использоваться три
атрибута, которые указывают, как принимающая сторона должна обрабатывать сообщение, —
mustUnderstand, actor и encodingStyle. Значение mustUnderstand — 1 или 0 — говорит принимающему
приложению о том, следует ли распознавать заголовок в обязательном или опциональном порядке.
Атрибут actor задаёт конкретную конечную точку для сообщения. Атрибут encodingStyle
устанавливает специфическую кодировку для элемента. По умолчанию SOAP-сообщение не имеет
определённой кодировки.

**Body («тело»)**. Сообщение, которое передаёт веб-приложение. Может содержать запрос к серверу
или ответ от него

Пример запроса и ответа от сервиса Яндекс.Спеллер:

```xml
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
xmlns:spel="http://speller.yandex.net/services/spellservice">
<soap:Header/>
  <soap:Body>
    <spel:CheckTextRequest lang="ru" options="0" format="">
      <spel:text>кылбаса</spel:text>
    </spel:CheckTextRequest>
  </soap:Body>
</soap:Envelope>
```

Пример ответа:

```xml
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
  <soap:Body>
    <CheckTextResponse
    xmlns="http://speller.yandex.net/services/spellservice">
      <SpellResult>
        <error code="1" pos="0" row="0" col="0" len="7">
          <word>кылбаса</word>
          <s>колбаса</s>
        </error>
      </SpellResult>
    </CheckTextResponse>
  </soap:Body>
</soap:Envelope>
```

# Отличия SOAP от REST

SOAP — протокол, а REST — архитектурный стиль. К недостаткам SOAP можно отнести:

- объёмные сообщения;
- поддержка только одного формата — XML;
- схема работы по принципу «один запрос — один ответ»;
- смена описания веб-сервиса может нарушить работу клиента.

REST поддерживает несколько форматов помимо XML: JSON, TXT, CSV, HTML. Вместо создания
громоздкой структуры XML-запросов при использовании REST чаще всего можно передать нужный
URL. Эти особенности делают стиль REST простым и понятным, а приложения и веб-сервисы,
использующие его, отличаются высокой производительностью и легко масштабируются.

У REST есть ряд недостатков, которые отсутствуют у SOAP:

- при использовании REST сложнее обеспечить безопасность конфиденциальных данных;
- трудности с проведением операций, которым необходимо сохранение состояния. Как,
например, в случае с корзиной в онлайн-магазине, которая должна сохранять добавленные
товары до момента оплаты.

# В каких случаях используют SOAP

- Асинхронная обработка и последующий вызов. Стандарт SOAP 1.2 обеспечивает клиенту
гарантированный уровень надёжности и безопасности.
- Формальное средство коммуникации. Если клиент и сервер имеют соглашение о формате
обмена, то SOAP 1.2 предоставляет жёсткие спецификации для такого типа взаимодействия.
Пример — сайт онлайн-покупок, на котором пользователи добавляют товары в корзину перед
оплатой. Предположим, что есть веб-служба, которая выполняет окончательный платёж.
Может быть достигнуто соглашение, что веб-сервис будет принимать только название
товара, цену за единицу и количество. Если сценарий существует, лучше использовать
протокол SOAP.
- Операции с состоянием. Если приложение требует, чтобы состояние сохранялось от одного
запроса к другому, то стандарт SOAP 1.2 предоставляет структуру для поддержки таких
требований.

# Тестирование Soap

Для тестирования SOAP используется инструмент SOAP UI. Скачать этот инструмент можно с сайта
<https://soapui.ru/>, где необходимо выбрать версию Open Source.

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/3.jpg?raw=true">

Устанавливаем и запускаем.

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/4.jpg?raw=true">

Далее создаём новый проект, для этого нажмём на кнопку SOAP:

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/5.jpg?raw=true">

В поле Project Name необходимо ввести название проекта (можно указать любое название). Также в
поле Initial WSDL указать путь к файлу WSDL. Мы будем использовать WSDL от Яндекс.Спеллера.
Перейдём по ссылке, которая ведёт на документацию Яндекс.Спеллера <a href = "https://yandex.ru/dev/speller/doc/dg/concepts/api-overview.html">(Описание API — API.
Руководство разработчика):</a>

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/6.jpg?raw=true">

Скопируем и вставим ссылку в поле Initial WSDL:
<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/7.jpg?raw=true">

После того как подтвердим создание проекта, нажав на кнопку ОК, созданный проект появится
слева в меню:
<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/8.jpg?raw=true">

В проекте имеется два набора: SpellServiceSoap и SpellServiceSoap12 для версий 1.1 и 1.2
соответственно. Для примера мы будем использовать версию SpellServiceSoap12. Открываем запрос
checkText → Request1:
<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/9.jpg?raw=true">
Это практически готовый запрос. Нам надо внимательно изучить документацию на проект <a href = "https://yandex.ru/dev/speller/doc/dg/reference/checkText.html">«Метод
checkText — API. Руководство разработчика»</a> и заполнить запрос данными. Данные, необходимые
для заполнения, обозначены знаками вопроса:

```xml
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
xmlns:spel="http://speller.yandex.net/services/spellservice">
  <soap:Header/>
  <soap:Body>
    <spel:CheckTextRequest lang="?" options="0" format="">
      <spel:text>?</spel:text>
    </spel:CheckTextRequest>
  </soap:Body>
</soap:Envelope>
```

Это параметр lang и значение в теге spel:text. В параметре lang укажем язык ru. И слово с ошибкой,
например, «кылбаса». Получится следующий запрос:

```xml
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
xmlns:spel="http://speller.yandex.net/services/spellservice">
  <soap:Header/>
  <soap:Body>
    <spel:CheckTextRequest lang="ru" options="0" format="">
     <spel:text>кылбаса</spel:text>
    </spel:CheckTextRequest>
  </soap:Body>
</soap:Envelope>
```

Отправляем его, получаем ответ:

```xml
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
  <soap:Body>
    <CheckTextResponse
    xmlns="http://speller.yandex.net/services/spellservice">
      <SpellResult>
        <error code="1" pos="0" row="0" col="0" len="7">
          <word>кылбаса</word>
          <s>колбаса</s>
        </error>
      </SpellResult>
    </CheckTextResponse>
  </soap:Body>
</soap:Envelope>
```

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/10.jpg?raw=true">

В ответе мы видим следующие параметры, описание которых можно взять из документации:

- SpellResult — корневой элемент;
- error — информация об ошибке (может быть несколько или может отсутствовать);
- word — исходное слово;
- s — подсказка (может быть несколько или может отсутствовать).

Элемент \<error> содержит следующие атрибуты:

- code — код ошибки, см. <a href = "https://yandex.ru/dev/speller/doc/dg/reference/error-codes-docpage/">коды ошибок;</a>
- pos — позиция слова с ошибкой (отсчёт от 0);
- row — номер строки (отсчёт от 0);
- col — номер столбца (отсчёт от 0);
- len — длина слова с ошибкой.

Итак, мы отправили запрос, получили ответ. Это базовые возможности SoapUI. Но можно ли быть
уверенными, что ответ у нас пришёл верный? Нет. Необходимо написать тесты на проверку
результата ответа, другими словами, как это называется в SOAP — Assertion.

## Assertion

Первоначально нужно создать TestSuite (набор тестов), для этого откройте меню проекта и выберите
New TestSuite:
<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/11.jpg?raw=true">

Указываем название, можно оставить дефолтное и для подтверждения нажать необходимо ОК

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/12.jpg?raw=true">

В окне редактирования suite можно добавить тест-кейс, нажав на зелёную галочку:

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/13.jpg?raw=true">

Или добавить его через контекстное меню в левом списке:

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/14.jpg?raw=true">

Мы создали новый тест-кейс на проверку длины слова, поэтому так и укажем название кейса:

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/15.jpg?raw=true">

Создадим новый Request, выбрав Create a new SOAP Request TestStep:

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/16.jpg?raw=true">
<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/17.jpg?raw=true">

В окне New TestRequest выберем в выпадающем списке: SpellServiceSoap12, так как мы используем
вторую версию api:
<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/18.jpg?raw=true">

Далее можно добавить сразу пару проверок на то, что пришёл ответ SOAP и он соответствует WSDL, и
нажать ОК:
<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/19.jpg?raw=true">

Создадим следующий запрос:

```xml
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
xmlns:spel="http://speller.yandex.net/services/spellservice">
  <soap:Header/>
    <soap:Body>
      <spel:CheckTextRequest lang="ru" options="0" format="">
        <spel:text>кылбаса</spel:text>
      </spel:CheckTextRequest>
    </soap:Body>
</soap:Envelope>
```

Отправляем его, получаем ответ:

```xml
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
  <soap:Body>
    <CheckTextResponse
    xmlns="http://speller.yandex.net/services/spellservice">
      <SpellResult>
        <error code="1" pos="0" row="0" col="0" len="7">
          <word>кылбаса</word>
          <s>колбаса</s>
        </error>
      </SpellResult>
    </CheckTextResponse>
  </soap:Body>
</soap:Envelope>
```

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/20.jpg?raw=true">

Из ответа нас будет интересовать следующая строка:

```xml
<error code="1" pos="0" row="0" col="0" len="7">
```

А именно параметр len="7", его мы и проверим. Нажимаем внизу на кнопку Assertions:

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/21.jpg?raw=true">

В Assertions имеются две проверки, которые были добавлены автоматически при создании шага, и
они прошли успешно и обе зелёные. Теперь давайте добавим проверку на то, что в ответе, в len
приходит значение 7. Нажимаем Add an assertion to this item:

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/22.jpg?raw=true">

Далее выбираем Property Content → XPath match:

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/23.jpg?raw=true">
Откроется окно редактирования Assert, где необходимо нажать на кнопку Declare для добавления
namespace:
<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/24.jpg?raw=true">
Оставим только первый XPath Expression, а второй удалим. Затем добавим строку с XPath, при этом
дописывая к имени тега переменную namespace:
```xml
declare namespace ns1='http:/ speller.yandex.net/services/spellservice';
/ ns1:error/@len
```
<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/25.jpg?raw=true">
А в Expected Result добавим значение len, которое мы ожидаем получить, в этом случае это 7 и
сохраним нашу проверку:
<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/26.jpg?raw=true">
В результате наш составленный assert зелёный и в ответе мы получили ожидаемое значение (7):
<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/27.jpg?raw=true">
Предположим, что мы ожидали получить значение 6:
<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/28.jpg?raw=true">
В таком случае получим ошибку, что мы ожидали 6, а по факту получили 7:
<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/29.jpg?raw=true">

### Mock-сервер

В SOAP имеется возможность эмуляции сервера. Кликаем правой кнопкой по проекту YandexSpeller
и выбираем Create SOAP MockService, в открывшемся окне указываем название:
<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/30.jpg?raw=true">
<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/31.jpg?raw=true">
Откроем MockService Editor и зададим путь, порт, хост (можно оставить по умолчанию):
<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/32.jpg?raw=true">
Запустим MockService, нажав Starts this MockService on the specified port:
<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/33.jpg?raw=true">
MockService запущен на порту 8080:
<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/34.jpg?raw=true">
Нажимаем на Create a new Mock Operation:
<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/35.jpg?raw=true">
Выберем вторую версию api:
<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/36.jpg?raw=true">
Справа добавим предполагаемый ответ от сервера (мок) то, что мы ожидаем получить:
<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/37.jpg?raw=true">
Далее возвращаемся к запросу (который не в тестах), меняем адрес на <http://localhost:8080>,
отправляем запрос и получаем в качестве ответа нашу «заглушку»:
<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/38.jpg?raw=true">
Таким образом можно эмулировать ответы сервера на любой запрос.

### QUERY_MATCH

Также на сэмулированные ответы можно добавить проверки, это делается по аналогии с проверками
в Assertions в тестах. Для этого переходим в MockService Editor и через контекстное меню или по
двойному клику правой кнопки мыши переходим в редактирование созданной mock операции:
<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/39.jpg?raw=true">
В итоге откроется окно редактирования mock операции:
<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/40.jpg?raw=true">
Также в кейсе, когда в моке создано несколько заглушек ответов, может появится необходимость
выбора конкретного ответа к конкретному запросу. Чтобы реализовать такие “связи”, нужно в
селекте Dispatch выбрать QUERY_MATCH, после чего в нижней части открытого окна появятся поля
добавления соответствия запрос-ответ:
<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/41.jpg?raw=true">
Для добавления match’а кликаем на плюсик:
<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/42.jpg?raw=true">
Далее откроется стандартное окно ввода названия, указываем название соответствия и кликаем ОК.
В результате получим match, в который теперь нужно добавить xpath и expected value, по которому
как раз SOAP UI и будет связывать запрос и ответ:
<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/43.jpg?raw=true">
Теперь в xpath тут нужно добавить путь, но перед этим кликаем на Declare для добавления
namespace (аналогично добавлению проверок в тестах), добавится 2 строчки, из которых нужна
только 1 - для namespace spel. После прописываем путь до элемента(например, по тексту слова), на
который мы завязываемся для выбора ответа - в итоге получается выражение аналогичное тому, что
на скрине. Также в поле Expected Value прописываем значение для элемента, к которому строили
путь, и в Dispatch to указываем ответ, который хотим увидеть при совпадении запроса с нашим
ожидаемым значением:
<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/44.jpg?raw=true">
Для того, чтобы наглядно продемонстрировать работу QUERY_MATCH, создадим еще одну заглушку
ответа, заменим в ней вопросительные знаки на какие-то значения и выберем этот ответ ответом по
умолчанию:
<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/45.jpg?raw=true">
Возвращаемся в тестовый запрос, который смотрит на mock-сервер и смотрим, какой ответ он нам
отдает при совпадении значения с заданным и при несовпадении:
<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/Soap%20api/46.jpg?raw=true">
Отсюда видно, что запрос и ответ матчатся корректно - все работает!

Mock-сервер - это хороший вариант для тестирования, когда у нас уже есть готовый клиент, который
надо протестировать, но пока ещё отсутствует сервер
