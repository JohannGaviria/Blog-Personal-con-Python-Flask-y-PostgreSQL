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