function showSignIn() {
    document.getElementById("selectionPage").style.display = "none";
    document.getElementById("signUpPage").style.display = "none";
    document.getElementById("signInPage").style.display = "block";
}

function showSignUp() {
    document.getElementById("selectionPage").style.display = "none";
    document.getElementById("signInPage").style.display = "none";
    document.getElementById("signUpPage").style.display = "block";
}

function redirectToForm() {
    window.location.href = "form.html"; // Redirects to form.html
}


