const btnPosts = document.getElementById('btn-posts');
const btnPeople = document.getElementById('btn-people');
const viewPost = document.getElementById('search-post-content');
const viewPeople = document.getElementById('search-people-content');

btnPosts.addEventListener('click', () => {
    viewPost.style.display = 'block';
    viewPeople.style.display = 'none';
});

btnPeople.addEventListener('click', () => {
    viewPeople.style.display = 'block';
    viewPost.style.display = 'none';
});

