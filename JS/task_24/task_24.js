"use strict";

// []()
// []()
// 1. Найти по id, используя getElementById, элемент с id равным "super_link" и вывести этот элемент в консоль.
// []()
// 2. Внутри всех элементов на странице, которые имеют класс "card-link", поменяйте текст внутри элемента на "ссылка".
// []()
// 3. Найти все элементы на странице с классом "card-link", которые лежат в элементе с классом "card-body" и вывести полученную коллекцию в консоль.
// []()
// 4. Найти первый попавшийся элемент на странице у которого есть атрибут data-number со значением 50 и вывести его в консоль.
// []()
// 5. Выведите содержимое тега title в консоль.
// []()
// 6. Получите элемент с классом "card-title" и выведите его родительский узел в консоль.
// []()
// 7. Создайте тегp`, запишите внутри него текст "Привет" и добавьте созданный тег в начало элемента, который имеет класс "card".

// 8. Удалите тег h6 на странице.



// const linkEl = document.getElementById('super_link');
// console.log(linkEl);

// const linkEls = document.querySelectorAll('.card-link');
// linkEls.forEach(el => {
//     el.textContent = 'ссылка';
// });

// const divEl = document.querySelector('.card-body');
// const linlEls = divEl.querySelectorAll('.card-link');
// console.log(linlEls)

// const atr = document.querySelector('[data-number = "50"]');
// console.log(atr);

// const textEl = document.querySelector('title');
// console.log(textEl.textContent);

// const getEl = document.querySelector('.card-title');
// console.log(getEl.parentNode)

// const newEl = document.createElement('p');
// newEl.textContent = 'Приввет';
// const divEl = document.querySelector('.card');
// divEl.prepend(newEl);

// const delEl = document.querySelector('h6');
// delEl.remove();