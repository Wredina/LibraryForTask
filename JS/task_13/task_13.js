// 1. Создайте объект с ключами от 1 до 7, в качестве значений содержащий имена дней недели. Выведите на экран “Вторник” 
// 2. Создайте объект user с ключами 'name', 'surname', ‘age’. Выведите на экран фамилию, имя и возраст через дефис. 
// 3. Добавьте в объект user свойство отчество, которое пользователь должен ввести с клавиатуры 
// 4. Удалите свойство surname


const obj = {};
const arr = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресение'];

for(i = 0; i < 7; i++){
    obj[i + 1] = arr[i];
}

console.log(obj[2]);

const user = {
    name: 'Sandra',
    surname: 'Socolova',
    age: 26
}

console.log(`${user.name} - ${user.surname} - ${user.age}`);

user.patronymic = prompt('введите отчество');
console.log(user);

delete user.surname;
console.log(user);


