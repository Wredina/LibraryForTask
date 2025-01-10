"use strict";

/*
Дан объект numbers. 
Необходимо в консоль вывести все значения объекта, которые больше или равны 3.
*/

const numbers = {
  key1: 12,
  key2: 2,
  key3: 4,
  key4: 1,
  key5: -244,
  key6: 0,
  key7: 7,
};

// Здесь пишем решение, данный комментарий необходимо стереть.

const arr = Object.values(numbers);

const arrNum = arr.filter(el => el >= 3);
console.log(arrNum);