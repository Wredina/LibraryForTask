// const slider = document.querySelector('.item__info__slider');
// const back_page = document.querySelector('.item__info__slider__back-page');
// const next_page = document.querySelector('.item__info__slider__next-page');
// const pages = document.querySelector('.main-container');
// const slide_count = ['page_02.html', 'page_03.html', 'page_04.html'];
// let slide_index = 0;

// back_page.addEventListener('click', showPreviousSlide);
// next_page.addEventListener('click', showNextSlide);

// function showPreviousSlide(){
//     slide_index = (slide_index - 1 + slide_count) % slide_count;
//     updateSlider();
// }

// function showNextSlide() {
//     slide_index = (slide_index + 1) % slide_count;
//     updateSlider();
//   }

//   function updateSlider() {
//     pages.forEach((slide, index) => {
//       if (index === slide_index) {
//         slide.style.display = 'block';
//       } else {
//         slide.style.display = 'none';
//       }
//     });
//   }
  
//   // Инициализация слайдера
//   updateSlider();


const pages = document.querySelector('.main-container');
const back_page = document.querySelector('.item__info__slider__back-page');
const next_page = document.querySelector('.item__info__slider__next-page');
const slide_count = ['page_02.html', 'page_03.html', 'page_04.html'];
let slide_index = 0;

next_page.addEventListener('click', show_next_page);
back_page.addEventListener('click', show_back_page);

function show_next_page(){
  if (slide_index === slide_count.length){
    slide_count[0]
  } else {
    slide_count[slide_index + 1]
  }

}

function show_back_page(){
  slide_count[slide_index - 1]
}