// 1. Создайте объект riddles 
// 2. Добавьте свойства question, answer 
// 3. создайте метод askQuestion который спрашивает у пользователя вопрос question и сравнивает ответ с answer 
// 4. Если ответил неверно, то в консоль выводится текст: “вы проиграли” 
// 5. * По желанию, создать 2 подсказки, если пользователь ответил неверно

const riddles = {
    question: 'зимой и летом',
    answer: ['елка', 'ёлка', 'ель'],
    help: ['растёт в лесу', 'нг'],
    askQuestion: function(){
        let count = 0;
        let countEndGame = 3;
        while(count < countEndGame){
            let userAnswer = prompt(this.question);
            if (this.answer.find((ans) => userAnswer === ans)){
                console.log('YES');
                count = countEndGame;
            } else if (count < countEndGame - 1) {
                console.log(`NO\nhelp: ${this.help[count]}`);
                count++;
            } else {
                console.log('sorry, but no, вы проиграли');
                count++;
            }
        }
    },
}

riddles.askQuestion();