const btnPublication = document.getElementById('btn-publication');
const btnComment = document.getElementById('btn-comment');
const postPublications = document.getElementById('post-publication');
const postComments = document.getElementById('post-comment');

btnComment.addEventListener('click', () => {
    postComments.style.display = 'block';
    postPublications.style.display = 'none';
});

btnPublication.addEventListener('click', () => {
    postPublications.style.display = 'block';
    postComments.style.display = 'none';
});