'use strict';


const linkEl = document.querySelector('.card-link');
linkEl.textContent = 'link text js';
linkEl.href = 'https://mail.ru/';

const imgEl = document.querySelector('.photo');
imgEl.src = 'https://yt3.ggpht.com/yti/ANjgQV-1muelk5qXaX2vbaEPZ9uHOkaW6eupC2kwhOzsD8DsaA=s88-c-k-c0x00ffffff-no-rj';

const divEl = document.querySelector('.card');
const newEl = document.createElement('p');
newEl.textContent = 'Новый текстовый элемент';
divEl.appendChild(newEl);

newEl.remove();


const btnEl = document.querySelector('.btn');
btnEl.onclick = function(){
    console.log('clic');
}

const newBtn = document.createElement('button');
newBtn.textContent = 'Отправить';
divEl.appendChild(newBtn);
newBtn.onclick = function(){
    newBtn.textContent = 'Текст отправлен'
}