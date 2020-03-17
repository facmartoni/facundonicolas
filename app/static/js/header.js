const $menuButton = document.getElementById("menu_button");
const $lines = document.getElementsByClassName("line");
const $nav = document.getElementById("nav");
const $body = document.getElementsByTagName("body")[0];

$menuButton.addEventListener("click", () => {
  for (i = 0; i < $lines.length; i++) {
    $lines[i].classList.toggle("lines-separated");
  }

  $nav.classList.toggle("nav-appears");
  $body.classList.toggle("overflow-hidden");
});
