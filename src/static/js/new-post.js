// const hashtagInput = document.getElementById('hashtag');
// const hashtagList = document.querySelector('.hashtag-list');
// const hashtagResult = document.querySelector('.hashtag-result');
// const result = document.getElementById('result');
// const maxHashtags = 5;

// hashtagInput.addEventListener('input', (e) => {
//     const inputValue = e.target.value.trim();

//     if (inputValue !== '') {
//         hashtagResult.style.display = 'block';
//         result.textContent = `#${inputValue}`;
//     } else {
//         hashtagResult.style.display = 'none';
//         result.textContent = '';
//     }
// });

// function addHashtagToList(inputValue) {
//     if (inputValue !== '') {
//         if (hashtagList.querySelectorAll('li').length >= maxHashtags) {
//             alert('No puedes agregar más de 5 hashtags.');
//         } else {
//             const listItem = document.createElement('li');
//             const hashtagText = document.createElement('span');
//             hashtagText.textContent = `#${inputValue}`;

//             const closeIcon = document.createElement('i');
//             closeIcon.classList.add('fas', 'fa-times');

//             listItem.appendChild(hashtagText);
//             listItem.appendChild(closeIcon);

//             hashtagList.appendChild(listItem);

//             hashtagInput.value = '';
//             result.textContent = '';
//             hashtagResult.style.display = 'none';

//             closeIcon.addEventListener('click', () => {
//                 listItem.remove();
//             });
//         }
//     }
// }

// hashtagInput.addEventListener('keydown', (e) => {
//     if (e.key === 'Enter') {
//         e.preventDefault();
//         const inputValue = hashtagInput.value.trim();
//         addHashtagToList(inputValue);
//     }
// });

// hashtagResult.addEventListener('click', () => {
//     const inputValue = result.textContent.trim();
//     if (inputValue) {
//         addHashtagToList(inputValue.slice(1));
//     }
// });

//-------------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------------

function insertMarkdown(openTag, closeTag) {
    const contentTextarea = document.getElementById('content');
    const selectionStart = contentTextarea.selectionStart;
    const selectionEnd = contentTextarea.selectionEnd;
    const currentText = contentTextarea.value;

    const selectedText = currentText.substring(selectionStart, selectionEnd);
    const newText = currentText.substring(0, selectionStart) + openTag + selectedText + closeTag + currentText.substring(selectionEnd);

    contentTextarea.value = newText;
}

//-------------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------------

function displayImage(event) {
    const preview = document.getElementById('image-preview');
    const btnDelete = document.getElementById('btn-delete');
    const btnChange = document.getElementById('btn-change');
    const formPostImage = document.getElementById('form-post-image');
    const imageInput = document.getElementById('image-input');
    const file = event.target.files[0];
    const reader = new FileReader();

    var viewImage = document.getElementById('view-image');

    reader.onload = function (e) {
        preview.setAttribute('src', e.target.result);
        preview.style.display = 'block';
        btnDelete.style.display = 'block';
        btnChange.style.display = 'block';
        formPostImage.style.display = 'none';
    };

    reader.readAsDataURL(file);

    btnDelete.addEventListener('click', function () {
        preview.setAttribute('src', '');
        preview.style.display = 'none';
        btnDelete.style.display = 'none';
        btnChange.style.display = 'none';
        formPostImage.style.display = 'block';

        viewImage.setAttribute('src', '');

        imageInput.value = "";
    });
}

//-------------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------------

document.addEventListener('input', function (e) {
    if (e.target.classList.contains('auto-resize') && e.target.tagName.toLowerCase() === 'textarea') {
        e.target.style.height = 'auto';
        e.target.style.height = (e.target.scrollHeight) + 'px';
    }
});

//-------------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------------

document.getElementById("btn-edit").addEventListener("click", function () {
    document.getElementById("edit-post-container").style.display = "block";
    document.getElementById("view-post-container").style.display = "none";
});

document.getElementById("btn-view").addEventListener("click", function () {
    document.getElementById("view-post-container").style.display = "block";
    document.getElementById("edit-post-container").style.display = "none";

    const imageInput = document.getElementById('image-input');
    const viewImage = document.getElementById('view-image');
    const titlePost = document.getElementById('title').value;
    
    if (imageInput.files && imageInput.files[0]) {
        const reader = new FileReader();
        
        reader.onload = function (e) {
            viewImage.src = e.target.result;
            viewImage.style.display = 'block';
        };
        
        reader.readAsDataURL(imageInput.files[0]);
    }
    
    document.getElementById('view-title').innerText = titlePost;
    
    const contentPost = document.getElementById('content').value;
    var converter = new showdown.Converter();
    var md = contentPost;
    var html = converter.makeHtml(md);
    
    document.getElementById('content-post').innerHTML = html;

});

//-------------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------------

function openModal() {
    const modal = document.getElementById('cancellation-warning');
    modal.style.display = 'block';
    document.body.style.overflow = 'hidden';
}

function closeModal() {
    const modal = document.getElementById('cancellation-warning');
    modal.style.display = 'none';
    document.body.style.overflow = 'auto';
}

document.getElementById('post-cancel').addEventListener('click', openModal);
document.getElementById('close-modal').addEventListener('click', closeModal);
document.getElementById('continue-editing-button').addEventListener('click', closeModal);

//-------------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------------

document.addEventListener("DOMContentLoaded", function () {
    const formPost = document.getElementById("form-post");
    const revertChange = document.getElementById("revert-change");
    const preview = document.getElementById('image-preview');
    const btnDelete = document.getElementById('btn-delete');
    const btnChange = document.getElementById('btn-change');
    const formPostImage = document.getElementById('form-post-image');

    revertChange.addEventListener("click", function () {
        preview.setAttribute('src', '');
        preview.style.display = 'none';
        btnDelete.style.display = 'none';
        btnChange.style.display = 'none';
        formPostImage.style.display = 'block';
        formPost.reset();
    });
});
