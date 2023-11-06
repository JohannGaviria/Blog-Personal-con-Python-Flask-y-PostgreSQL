const hashtagInput = document.getElementById('hashtag');
const hashtagList = document.querySelector('.hashtag-list');
const hashtagResult = document.querySelector('.hashtag-result');
const result = document.getElementById('result');
const maxHashtags = 5;

hashtagInput.addEventListener('input', (e) => {
    const inputValue = e.target.value.trim();

    if (inputValue !== '') {
        hashtagResult.style.display = 'block';
        result.textContent = `#${inputValue}`;
    } else {
        hashtagResult.style.display = 'none';
        result.textContent = '';
    }
});

function addHashtagToList(inputValue) {
    if (inputValue !== '') {
        if (hashtagList.querySelectorAll('li').length >= maxHashtags) {
            alert('No puedes agregar más de 5 hashtags.');
        } else {
            const listItem = document.createElement('li');
            listItem.textContent = `#${inputValue}`;

            hashtagList.appendChild(listItem);

            hashtagInput.value = '';
            result.textContent = '';
            hashtagResult.style.display = 'none';
        }
    }
}

hashtagInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
        e.preventDefault();
        const inputValue = hashtagInput.value.trim();
        addHashtagToList(inputValue);
    }
});

hashtagResult.addEventListener('click', () => {
    const inputValue = result.textContent.trim();
    if (inputValue) {
        addHashtagToList(inputValue.slice(1));
    }
});

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
    const file = event.target.files[0];
    const reader = new FileReader();

    reader.onload = function (e) {
        preview.setAttribute('src', e.target.result);
        preview.style.display = 'block';
        btnDelete.style.display = 'block';
        btnChange.style.display = 'block';
        formPostImage.style.display = 'none';
    };

    reader.readAsDataURL(file);
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