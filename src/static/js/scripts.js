// Mostrar y ocultar contraseña
function togglePasswordVisibility() {
    var passwordInput = document.getElementById("password");
    var icon = document.getElementById("togglePassword");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        icon.classList.remove("fa-lock");
        icon.classList.add("fa-unlock");
    } else {
        passwordInput.type = "password";
        icon.classList.remove("fa-unlock");
        icon.classList.add("fa-lock");
    }
}

//-------------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------------

function openFileExplorer(name) {
    document.getElementById(name).click();
}