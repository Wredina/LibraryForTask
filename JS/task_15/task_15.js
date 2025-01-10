// const obj = { 
    // key1: { 
        // key1: 1, 
        // key2: 2, 
        // key3: 3,
    // }, 

    // key2: { 
        // key1: 4, 
        // key2: 5, 
        // key3: 6, 
    // }, 

    // key3: {
        // key1: 7, 
        // key2: 8, 
        // key3: 9,
    //  }, 
//  } 
// 
// Найдите сумму элементов приведенного объекта.


const obj = { 
    key1: { 
        key1: 1, 
        key2: 2, 
        key3: 3,
    }, 

    key2: { 
        key1: 4, 
        key2: 5, 
        key3: 6, 
    }, 

    key3: {
        key1: 7, 
        key2: 8, 
        key3: 9,
     }, 
 } 

let total = 0;

for (const key in obj){
    total += Object.values(obj[key]).reduce((a,b) => a + b);
}

console.log(total);



// function allNumValueObject(obj){
//     let sum = 0;

//     for (const key in obj) {
//         if (typeof obj[key] === 'number'){
//             sum += obj[key];
//         } else {
//             sum += allNumValueObject(obj[key]);
//         }
//     }
//     return sum;
// }


// console.log(allNumValueObject(obj));

