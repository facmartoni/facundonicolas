const $footerCTA = document.getElementById("footer-cta");

const mediumScreenSize = window.matchMedia("(min-width: 768px)");

const ScreenSizeFuntion = size => {
  if (size.matches) {
    $footerCTA.innerHTML =
      "¿Te aviso cada vez que escribo? ¡Suscríbete a mi blog!";
  }
};

ScreenSizeFuntion(mediumScreenSize);
mediumScreenSize.addListener(ScreenSizeFuntion);
