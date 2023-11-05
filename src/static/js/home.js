const recentButton = document.getElementById('filter-recent');
const relevantButton = document.getElementById('filter-relevant');
const closeIcon = document.getElementById('close-icon');

recentButton.addEventListener('click', () => {
    relevantButton.classList.remove('select-filter');
    recentButton.classList.add('select-filter');
    closeIcon.style.display = 'block';
});

relevantButton.addEventListener('click', () => {
    recentButton.classList.remove('select-filter');
    relevantButton.classList.add('select-filter');
    closeIcon.style.display = 'block';
});


closeIcon.addEventListener('click', () => {
    recentButton.classList.remove('select-filter');
    relevantButton.classList.remove('select-filter');
    closeIcon.style.display = 'none';
});

//-------------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------------

const buttonCreate = document.querySelector('.button-create');
const buttonCreatePosition = buttonCreate.getBoundingClientRect().top;
const buttonFixed = document.getElementById('buttonFixed');

window.addEventListener('scroll', () => {
    if (window.scrollY >= buttonCreatePosition) {
        buttonFixed.style.display = 'block';
    } else {
        buttonFixed.style.display = 'none';
    }
});

//-------------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------------

var elemento = document.getElementById('author-details-hidden');
var boton = document.getElementById('button-author-name');

boton.addEventListener('click', function () {
    elemento.style.display = 'block';
});