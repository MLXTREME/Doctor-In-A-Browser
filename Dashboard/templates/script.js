/*Menu*/
const menu = document.querySelector('.menu')
const dashEm = document.querySelector('.menu_btn')
const content = document.querySelector('.content')
const demo = document.querySelector('.demo')



dashEm.addEventListener('click', () => {
    console.log('Menu');
    menu.classList.add('open');
})

menu.addEventListener('click', (e) => {
    if (e.target.classList.contains('menu')) {
        menu.classList.remove('open');
    }
})


/* Stage*/

const X1 = document.querySelector('.X-1')
const model_1 = document.querySelector('.model-1-tab')
X1.addEventListener('click', () => {
    console.log('X-1');
    model_1.classList.add('open');

})

const X2 = document.querySelector('.X-2')
const model_2 = document.querySelector('.model-2-tab')
X2.addEventListener('click', () => {
    console.log('X-2');
    model_2.classList.add('open');

})

const X3 = document.querySelector('.X-3')
const model_3 = document.querySelector('.model-3-tab')
X3.addEventListener('click', () => {
    console.log('X-3');
    model_3.classList.add('open');

})

const X4 = document.querySelector('.X-4')
const model_4 = document.querySelector('.model-4-tab')
X4.addEventListener('click', () => {
    console.log('X-4');
    model_4.classList.add('open');

})

/*Upload*/

const choose_file = document.querySelector('#choose_file');
const default_button = document.querySelector('#default-button');
const img = document.querySelector("img");
const wrapper = document.querySelector(".wrapper");
const cancel = document.querySelector("#cancel");


function defaultBtnActive() {
    default_button.click();
}

default_button.addEventListener('change', function () {
    const file = this.files[0];

    if (file) {
        const reader = new FileReader;
        reader.addEventListener('load', function () {
            img.src = reader.result;
            wrapper.classList.add("active");
        });
        cancel.addEventListener("click", function () {
            img.src = "";
            wrapper.classList.remove("active");
        })

        reader.readAsDataURL(file);
    }
})


const use=document.querySelector('use');
use.addEventListener('click',()=>{
    console.log("Laure");
})