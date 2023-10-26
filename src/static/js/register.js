function displayPhoto(event) {
    const preview = document.getElementById('photo-preview');
    const file = event.target.files[0];
    const reader = new FileReader();

    reader.onload = function (e) {
        preview.setAttribute('src', e.target.result);
        preview.style.display = 'block';
    };

    reader.readAsDataURL(file);
}
function openFileExplorer() {
    document.getElementById('photo').click();
}