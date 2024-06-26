# сниффинг трафика

**Сниффинг** — процесс мониторинга и перехвата всех пакетов, проходящих через сеть, с
помощью инструментов сниффинга (Charles Proxy).

## Как осуществляется проксирование трафика

Сниффер трафика — программа, которая устанавливается и запускается на компьютере в той
же локальной подсети, что и веб-, мобильное приложение или иное тестируемое приложение.
Снифферы трафика работают по принципу man in the middle. Имеется промежуточный сервер
(в данном случае наш ПК), через который проходят запросы и ответы.

Для выполнения проксирования HTTP-трафика, практически в любом инструменте
необходимо настроить Wi-Fi соединение. В настройках прокси или Wi-Fi мобильного
устройства в качестве прокси-сервера указывается IP-адрес компьютера и порт инструмента.

С HTTPS немного сложнее: нужно установить SSL-сертификат сниффера на устройство и
разрешить девайсу доверять сертификату, чтобы трафик расшифровывался

Но есть нюанс с SSL-пиннингом, то есть процессом сверки полученного сертификата со
вшитым в приложение. Если в вашем приложении есть SSL-пиннинг, для его отключения на
тестовой версии приложения придётся обратиться к разработчикам. Иначе подсмотреть
трафик приложения не получится.

# Инструменты прокси-трафика

<a href="https://www.telerik.com/fiddler/fiddler-classic">Fiddler Classic</a> — приложение прокси-сервера для отладки HTTP. Он позволяет пользователю
просматривать HTTP- и, HTTPS-трафик, доступ к которому осуществляется с локального
компьютера, на него или через него.

Платформы: Windows.

<a href="https://www.telerik.com/fiddler/fiddler-everywhere">Fiddler Everywhere</a> — кроссплатформенное приложение прокси-сервера для отладки HTTP
исходящего или входящего трафика.

Платформы: Windows, Mac OS, Linux

<a href="https://www.charlesproxy.com/">Charles Proxy</a> — кроссплатформенное приложение прокси-сервера для отладки HTTP,
написанное на Java. Он позволяет пользователю просматривать HTTP, HTTPS и
активированный трафик TCP-порта, доступ к которому осуществляется с локального
компьютера, на него или через него. Сюда входят запросы и ответы, включая HTTP-заголовки
и метаданные (например, файлы cookie, кеширование и кодирование информации), с
функциями, предназначенными для помощи разработчикам и тестировщикам в анализе
соединений и обмене сообщениями.

Платформы: Windows, Mac OS, Linux

<a href="https://mitmproxy.org/">Mitmproxy</a> — инструмент для перехвата, проверки, изменения и воспроизведения
веб-трафика, такого как HTTP/1, HTTP/2, WebSockets или любых других протоколов,
защищённых SSL/TLS. Также можно преобразовывать и декодировать различные типы
сообщений, от HTML до Protobuf, перехватывать определённые сообщения на лету, изменять
их до того, как они достигнут места назначения, и позже воспроизводить их на клиенте или
сервере.

Платформы: Mac OS

<a href="https://proxyman.io/">Proxyman</a> — это приложение для macOS, которое позволяет разработчикам с лёгкостью
захватывать, проверять и обрабатывать HTTP-запросы/ответы. Инструмент позволяет делать
Breakpoint (перехват запросов в определённый момент времени), Map Local (использование
локальных файлов в качестве ответа на запросы), выполнять отладку GraphQL, делать diff
запросов и ответов и многое другое.

Платформы: Mac OS

## Charles Proxy

Мы рассмотрим принцип работы и функциональность инструмента Charles Proxy

### Как установить Charles для Windows

Скачиваем дистрибутив для своей операционной системы и запускаем установщик. Никаких
особенных настроек в процессе установки делать не требуется, всё достаточно стандартно:

<img src="https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/1.jpg?raw=true">

Сразу после установки приложения можно приступить к работе.

#### Настройка Charles

Для работы с HTTPS-трафиком надо установить сертификаты прокси-сервера Charles в
браузер. В зависимости от браузера этот сценарий отличается.

##### Windows или Internet Explorer

Открываем меню Help и выбираем SSL Proxying — Install Charles Root Certificate.

<img src="https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/2.jpg?raw=true">

Появится окно для установки сертификата. Нажимаем кнопку «Установить сертификат»:

<img src="https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/3.jpg?raw=true">

Запустится мастер импорта сертификатов. На втором шаге выбираем «Поместить все
сертификаты в следующее хранилище» и нажимаем кнопку «Обзор...».

<img src="https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/4.jpg?raw=true">

В списке хранилищ выбираем «Доверенные корневые центры сертификации»:

<img src="https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/5.jpg?raw=true">

Нажимаем «Далее», «Готово»:

<img src="https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/6.jpg?raw=true">

Для надёжности перезапустим Internet Explorer.

##### Mozilla Firefox

Для начала надо убедиться, что в Firefox настроен прокси и браузер работает через Charles.
Открываем «Настройки» → «Основные» → «Параметры сети» и нажимаем кнопку «Настроить»:

<img src="https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/7.jpg?raw=true">

Далее в Charles Proxy переходим на вкладку Help → Local iP Address.

<img src="https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/8.jpg?raw=true">

Смотрим свой IP-адрес. В нашем примере это 192.168.31.199.

<img src="https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/9.jpg?raw=true">

Включаем «Ручная настройка прокси» в Firefox. Указываем IP-адрес 192.168.31.199 и порт
8888, а также включаем «Использовать для FTP и HTTPS».

<img src="https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/10.jpg?raw=true">

После настройки прокси открываем адрес <https://chls.pro/ssl> в Firefox. В открывшемся окне
включаем Trust this CA to identify websites и завершаем импорт.
Если окно не открылось, а появляется окно сохранения pem-файла, то сохраняем файл и
добавляем сертификат вручную. Открываем «Настройки» → «Приватность и защита» →
«Просмотр сертификатов»:

<img src="https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/11.jpg?raw=true">

Далее переходим в раздел «Центры сертификации» и нажимаем «Импортировать»:

<img src="https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/12.jpg?raw=true">

Выбираем сохранённый файл с сертификатом. Откроется окно импорта. Включаем «Доверять
при идентификации веб-сайтов» и нажимаем ОК. Сертификат установлен.

<img src="https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/13.jpg?raw=true">

Далее рекомендуется перезапустить Firefox и Charles.

### Возможности Charles Proxy

1. Подмена данных

Представим, что нам надо протестировать на клиенте вёрстку. Нужно проверить, как будет
отображаться множество бонусов у пользователя. Один из вариантов, который многие
предложат: изменить в БД количество бонусов и проверить на клиенте. Да, вы будете правы!
Однако на сервере может быть кеш, и необходимо подождать какое-то время, пока
количество бонусов не обновится, либо просто подключиться к самой базе и выполнить
запрос — это занимает определённое время. Есть вариант проще: изменить ответ от сервера!
В Charles Proxy есть три способа подмены данных:

- breakpoint
- rewrite
- map local

#### 1.1 Breakpoint

Breakpoint — это некая точка остановки запроса. Когда обнаруживается запрос из заданного
списка, для дальнейшего ручного взаимодействия с параметрами запроса открывается
отдельное окно. В нём перейдите к ручному изменению запросов и ответов. Удобно
использовать эту функцию, когда тестируете API или разные ответы сервера.

У нас есть профиль пользователя, у которого сейчас не указан email (либо значение ещё не
отдаётся сервером и нам надо проверить вёрстку на клиенте, пока ждём реализацию на
бэке):

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/30.jpg?raw=true">

Запрос, в котором приходит email: <https://api.youla.io/api/v1/user/6091ceee58e49e3b153ad65a>

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/31.jpg?raw=true">

Чтобы «повесить» Breakpoint на запрос, перейдите в раздел Proxy → Breakpoint Settings. Далее
поставьте галочку Enable Breakpoints → Add и в открывшемся диалоговом окне Edit Breakpoint
вставьте URL запроса, как показано на скриншоте:

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/32.jpg?raw=true">

Для примера поставьте две галочки: Request и Response. Нажмите OK, затем ещё раз OK в окне
Breakpoint Settings. Теперь ещё раз выполните запрос — просто обновите вкладку с
профилем.

В Charles Proxy мы видим, что выполнение запроса ставится на паузу:

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/33.jpg?raw=true">

Здесь можно изменить параметры запроса. Но сейчас это делать не нужно, нажмите Execute.
Следом у нас ставится на паузу уже пришедший ответ от сервера. И тут как раз мы должны
отредактировать Response. Найдите нужный параметр — "email": null.

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/34.jpg?raw=true">

Далее измените значение параметра "email", например, на <my@mail.ru> бонусов, и нажмите
Execute.

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/35.jpg?raw=true">

На клиенте отобразится email клиента:

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/36.jpg?raw=true">

#### 1.2 Rewrite

Rewrite — это инструмент, позволяющий создавать правила, которые изменяют запросы и
ответы, когда те проходят через Charles Proxy. Например, можно добавлять и изменять
заголовок, искать и заменять текст в теле ответа или запроса и т. д.

Попробуем с помощью Rewrite изменить email пользователя. Для этого откройте Tools →
Rewrite → галочка Enable Rewrite → Add. В поле Name можно ввести любое название подмены,
например, email, либо оставить по умолчанию Untitled Set.

На следующем шаге необходимо добавить в Location путь запроса. Для этого в разделе
Location → Add заполните следующие поля и сохраните:

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/37.jpg?raw=true">

После того как вы добавили путь запроса, необходимо изменить сам параметр и его значение.
Для этого нужно создать Rewrite Rule:

- Type: Body, потому что параметр находится в теле.
- Where: Response, потому что параметр находится в ответе от сервера.
- Раздел Match: в Value укажите значение и параметр, возвращаемый сервером.
- Раздел Replace: в Value укажите значение и параметр, который хотите увидеть на
клиенте.

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/38.jpg?raw=true">

Далее сохраните «Rewrite Rule» и нажмите ОК на вкладке Rewrite Settings. На клиенте
перезапросите ещё раз профиль пользователя. У вас автоматически подменился email:

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/39.jpg?raw=true">

#### 1.3 Map Local

Map Local — инструмент, который позволяет использовать локальные файлы, словно они
являются частью сервера.

Перейдите в Tools → Map Local.
<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/40.jpg?raw=true">

Далее в окошке Map Local Settings нажмите Add → Хост:
<https://api.youla.io/api/v1/user/6091ceee58e49e3b153ad65a> → Local path: путь на компьютере
до файла. Можете использовать готовые медиафайлы, HTML, CSS, JSON, XML. Больше
подходит, конечно, разработчикам, чтобы не загружать данные на сервер для его
последующего тестирования, но и тестировщик может найти грамотное применение. Мы
заранее подготовили ответ, который нам будет нужен, и сохранили в файл email.json:

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/41.jpg?raw=true">

Сохраните введённые значения на вкладке Edit Mapping и на вкладке Map Local Settings.

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/42.jpg?raw=true">

На клиенте перезапросите ещё раз профиль пользователя. У вас автоматически подменяется
email.

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/43.jpg?raw=true">

Рассмотрим другие возможности инструмента Charles Proxy. И начнём с самого начала: со
вкладки Proxy.

#### 2.1 Throttle Settings

Throttle Settings — функция, позволяющая задавать разные параметры скорости соединения с
выбранным доменом.

Функция для тех, кто любит тестировать в лифте, в метро, в подземном переходе. Перейдём в
Proxy → Throttle Settings → галочка Enable Throttling. Если не разбираетесь во всех
перечисленных пунктах, то можете использовать Throttle preset и там выбрать подходящую
для теста скорость, а система автоматически заполнит остальные поля.

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/44.jpg?raw=true">

Если выбрать Only for selected hosts, то можно задать определённый хост, к которому будут
применяться ваши настройки. Здесь можно использовать готовые пресеты с настройками для
различных типов (4G, 3G и т. д.).Также можно задать разные параметры. Коротко перечислю
некоторые из них:

- Bandwidth — максимальный объём данных, который может быть передан с течением
времени.
- Utilisation — доля общей пропускной способности, которая может быть предоставлена
пользователю в любое время.
- Latency — задержка в миллисекундах по запросу firts между клиентом и удалённым
сервером.
- MTU — максимальное передающее устройство для текущего пресета.
- Reliability — мера вероятности, что соединение не удастся. Используется для имитации
ненадёжных сетевых условий.
- Stability — мера вероятности, что соединение будет нестабильным и, следовательно,
снизится качество. Полезно для моделирования сетей, в которых периодических
падает качество связи, например, мобильных.

#### 2.2 Reverse Proxies

Reverse proxy — обратный прокси-сервер. Обычно используется для того, чтобы принимать
запросы из интернета и перенаправлять их на один из веб-серверов.

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/45.jpg?raw=true">

#### 2.3 Port Forwarding

Port Forwarding — проброс портов, который иногда называют перенаправлением портов, или
туннелированием — процесс пересылки трафика, адресованного конкретному сетевому порту,
с одного сетевого узла на другой. Этот метод позволяет внешнему пользователю достичь
порта внутри локальной сети.

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/46.jpg?raw=true">

#### 2.4 MacOS Proxy/Windows Proxy

MacOS Proxy или Windows Proxy (в зависимости от вашей ОС) — проксирование трафика с
вашего веб-браузера.

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/47.jpg?raw=true">

Разобравшись с разделом Proxy, перейдём к разделу Tools.

#### 3.1 No Caching

Инструмент No Caching предотвращает кеширование, манипулируя заголовками HTTP,
которые управляют кешированием ответов. Заголовки If-Modified-Since и If-None-Match
удаляются из запросов, добавляются Pragma: no-cache и Cache-control: no-cache. Заголовки
Expires, Last-Modified и ETag удаляются из ответов и добавляются Expires: 0 и Cache-Control:
no-cache.

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/48.jpg?raw=true">

#### 3.2 Block Cookies

Block Cookies — заголовок файла Cookie удаляется из запросов, предотвращая отправку
значений файла из клиентского приложения, например, веб-браузера, на удалённый сервер. А
также из ответов удаляется заголовок Set-Cookie, предотвращая получение клиентским
приложением запросов на установку файлов cookie с удалённого сервера. В настройках
можно включить удаление Cookie как для всех хостов, так и для выбранных. В примере ниже
включено удаление Cookie для всех запросов.

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/49.jpg?raw=true">

#### 3.3 Map Remote

Map Remote — позволяет переадресовать запросы с одного URL Map From на другой Map To.
Подменяет хост, путь целиком или только параметры — в зависимости от вашей задачи. В
примере ниже подменён запрос с prod-сервера на dev-сервер.

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/50.jpg?raw=true">

#### 3.4 Block List

Block List — позволяет блокировать определённые доменные имена. Когда веб-браузер
попытается запросить любую страницу из заблокированного доменного имени, она
заблокируется. Можно выбрать либо Drop connection, либо возврат ошибки 403.

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/51.jpg?raw=true">

#### 3.5 DNS Spoofing

Виртуальный хостинг — это когда у вас есть несколько сайтов на одном IP-адресе, и
веб-сервер определяет, какой сайт вы запрашиваете, основываясь на имени, введённом в
браузере. Точнее, сервер смотрит на заголовок хоста, отправленный в запросе. Например,
когда нужно подменить хосты, чтобы при вводе какого-либо адреса в браузере (скажем,
api.youla.ru) запросы уходили по другому адресу (допустим, на тестовую площадку). DNS
Spoofing — перенаправляет доменное имя на определённый IP-адрес.

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/52.jpg?raw=true">

#### 3.6 Mirror

Mirror — эта функция позволяет автоматически сохранять все ответы, возвращаемые в Charles
Proxy. Они раскладываются локально в такой же иерархии, как на сервере. Если внезапно
случился даунтайм на бэкенде, отвалилась тестовая среда и т. д., у вас уже есть готовые моки
для Map Local. Активировать функцию можно так: Tools → Mirror или Tools → Auto Save

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/53.jpg?raw=true">

#### 3.7 Compose

Compose — функция редактирования запросов, которые вы поймали

Например, вы добавляете в «Избранное» какой-то товар, но почему-то он не добавляется. Вы
можете отредактировать уже отправленный запрос и отправить его ещё раз. Для этого
необходимо выбрать нужный запрос из списка, нажать на нём правой кнопкой и выбрать
Compose. Иконка у запроса поменяется — теперь можно смело его редактировать.

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/54.jpg?raw=true">

После того как вы изменили нужные значения в запросе, нажмите внизу Execute, чтобы
отправить запрос на сервер.

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/54.jpg?raw=true">

### 2. Recording Settings

Recording Settings — настройки отображения списков разрешённых и запрещённых доменов

Во вкладке Options можно настроить лимит, то есть количество запросов, которое Charles
Proxy должен записать.

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/55.jpg?raw=true">

Во вкладке Include можно выбрать конкретный домен для отображения пакетов

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/56.jpg?raw=true">

Во вкладке Exclude можем выбрать те домены, которые необходимо спрятать при сниффинге

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/57.jpg?raw=true">

### 3. Focus

Focus — функция, которая перемещает домен на первые позиции в списке.

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/58.jpg?raw=true">

### 4. Repeat

Repeat — отправляет на сервер запрос, идентичный выбранному.

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/59.jpg?raw=true">

### 5. Repeat Advanced

Repeat Advanced — идентично Repeat, только можно выбрать количество отправляемых
запросов и задержку между ними. Эта функция пригодится при проверке реакции сервера на
флуд.

Здесь Concurrency — количество пользователей, а Iterations — количество повторений каждого
запроса. Также можно поставить галочку Show results in new Session — откроется новое окно,
где будут выполняться запросы.

<img src = "https://github.com/Wredina/LibraryForTask/blob/main/Tester/img/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B0/60.jpg?raw=true">
