const $menuButton = document.getElementById("menu_button");
const $lines = document.getElementsByClassName("line");
const $nav = document.getElementById("nav");

$menuButton.addEventListener("click", () => {
  for (i = 0; i < $lines.length; i++) {
    $lines[i].classList.toggle("lines-separated");
  }

  $nav.classList.toggle("nav-appears");
});
