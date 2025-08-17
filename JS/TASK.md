HTML узлы

- Element node - элемент как он есть
- Root node - верхний узел в древе
- child note - узел ребёнок. находится внутри другого узла
- Ancestor node (узел прародитель) - один из родительских узлов текущего узла
- Parent node (узел родитель) - узел, в которы входит текущий узел
- silling node (родственный узел) - узлы лежащие на одном уровне
- text node (тектовый узел) - узел содержащий текстовую строку

Поиск элементов

```js
// - по классу
document.querySelector('.card');

// - по id
document.querySelector('#card');

// - по тегу
document.querySelector('card');

// - по атрибуту
document.querySelector('[atribute = "value"]');

// - вывести все элементы в массиве
document.querySelectorAll('.card');


// Старые методы

// - по классу
document.getElementByClassName('card');

// - по id
document.getElementByID('card');

// - по тегу
document.getElementByTagName('card');


// Другие поиски

// - найти все элементы внутри другого
1. найти родительский элемент
const divEl = document.querySelector('.card-body');
2. найти все нужные элементы внутри
const linlEls = divEl.querySelectorAll('.card-list');
```

Получение данных
```js 
// - вывести содержимое тега
1. ищем нужный эл.
const textEl = document.querySelector('title');
2. выводим в консоль
console.log(textEl.textContent);

// - изменить текст внутри всех элементов
1. поиск всех эл-тов и создание из них массива
const linkEls = document.querySelectorAll('.card-link');
2. проходимся по ним
linkEls.forEach(el => {
    el.textContent = 'ссылка';
});

// - вывести родительский узел
1. получаем дочерний элемент
const getEl = document.querySelector('.card-title');
2. обращаемся через него к родительскому
console.log(getEl.parentNode)

// - изменения данных в атрибуте (изменение ссылки. В изображениях так можно менять путь картинки через src)
const linkEl = document.querySelector('.card-link');
linkEl.href = 'https://mail.ru/';
// либо
linkEl.setAttribute('href', 'https://mail.ru/');
```

Создание, удаление и клонирование
```js 
// - создание
const newEl = document.createElement('p')

// - удаление
el.remove()

// - создание и добавление внутри текста
const newEl = document.createElement('p');
newEl.textContent = 'Привет';

// - создание текстового тега с текстом и добавление его в див в начало
const newEl = document.createElement('p');
newEl.textContent = 'Привет';
const divEl = document.querySelector('.card');
divEl.prepend(newEl);

// - создание текстового тега с текстом и добавление его в див в конец
const newEl = document.createElement('p');
newEl.textContent = 'Привет';
const divEl = document.querySelector('.card');
divEl.appendChild(newEl);

// - клонирование
divEl.cloneNode(newEl);

// - замена одного на другой
divEl.replaceWith(newEl);
```

Управление стилями
```js
// - при прописывании стилей нельзя пользоваться дефисами и т.д. 
// Используется верблюжий стиль и всегда в нижнем регистре.
1.вариант
newEl.style.color = 'white';
newEl.style.textAlight = 'center';
newEl.style.backgroundColor = 'black';

2.вариант
// прописывается в HTML документе в теге head 
<style>
    .paragraph{
        color: white;
        text-alight: center;
        background-color: black;
    }
<style>

// в js файле
newEl.setAttribute('class', 'paragraph');
```