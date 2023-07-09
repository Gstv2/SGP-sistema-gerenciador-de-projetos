var editProfileButton = document.getElementById('edit-profile-button');
var saveProfileButton = document.getElementById('save-profile-button');
var cancelProfileButton = document.getElementById('cancel-profile-button');
var profileContainer = document.querySelector('.profile-container');
var idadeElement = document.getElementById('idade');
var cargoElement = document.getElementById('cargo');
var bioElement = document.getElementById('bio');
var websiteElement = document.getElementById('website');
var changePictureButton = document.getElementById('change-picture-button');
var toggleThemeButton = document.getElementById('toggle-theme-button');

editProfileButton.addEventListener('click', function() {
  profileContainer.classList.add('edit-mode');
});

cancelProfileButton.addEventListener('click', function() {
  profileContainer.classList.remove('edit-mode');
});

saveProfileButton.addEventListener('click', function() {
  var idade = idadeElement.innerText;
  var cargo = cargoElement.innerText;
  var bio = bioElement.value;
  var website = websiteElement.innerText;
  
  // Salvar as alterações do perfil
  // Seu código para salvar as alterações vai aqui
  
  profileContainer.classList.remove('edit-mode');
});

changePictureButton.addEventListener('click', function() {
  // Abrir o seletor de arquivos ou executar qualquer outra ação para alterar a imagem do perfil
  // Seu código para alterar a imagem do perfil vai aqui
});

toggleThemeButton.addEventListener('click', function() {
  profileContainer.classList.toggle('dark-theme');
});
