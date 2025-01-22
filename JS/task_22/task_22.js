// Получите ссылку на первый абзац из дива с id, равным block, выведите его в консоль
// Получите ссылку на первый абзац с классом www. и вывести его в консоль
// <p class="www">text 1</p>
// <p class="www">text 2</p>


const blockEl = document.querySelector('#block');
console.log(blockEl);

const siteEl = document.querySelectorAll('.www')[0];
console.log(siteEl);