const btnPublication = document.getElementById('btn-publication');
const btnComment = document.getElementById('btn-comment');
const btnFavorite = document.getElementById('btn-favorite');
const postPublications = document.getElementById('post-publication');
const postComments = document.getElementById('post-comment');
const favorite = document.getElementById('favorite');

btnComment.addEventListener('click', () => {
    postComments.style.display = 'block';
    postPublications.style.display = 'none';
    favorite.style.display = 'none';
});

btnPublication.addEventListener('click', () => {
    postPublications.style.display = 'block';
    postComments.style.display = 'none';
    favorite.style.display = 'none';
});

btnFavorite.addEventListener('click', () => {
    favorite.style.display = 'block';
    postPublications.style.display = 'none';
    postComments.style.display = 'none';
});