function editProfile() {
    let newName = prompt("Enter your name:", document.getElementById("owner-name").innerText);
    let newEmail = prompt("Enter your email:", document.getElementById("email").innerText);
    let newPhone = prompt("Enter your phone:", document.getElementById("phone").innerText);
    let newPetName = prompt("Enter your pet's name:", document.getElementById("pet-name").innerText);
    let newPetBreed = prompt("Enter your pet's breed:", document.getElementById("pet-breed").innerText);
    let newPetAge = prompt("Enter your pet's age:", document.getElementById("pet-age").innerText);

    document.getElementById("owner-name").innerText = newName;
    document.getElementById("email").innerText = newEmail;
    document.getElementById("phone").innerText = newPhone;
    document.getElementById("pet-name").innerText = newPetName;
    document.getElementById("pet-breed").innerText = newPetBreed;
    document.getElementById("pet-age").innerText = newPetAge;
}
