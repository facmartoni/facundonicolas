const $featuredArticleContainer = document.getElementById(
  "featured_article_preview__container"
);

const $featuredArticleOverlay = document.getElementById(
  "featured_article_preview__overlay"
);

const $featuredArticleBody = document.getElementById(
  "featured_article_preview__body"
);

$featuredArticleContainer.addEventListener("mouseover", () => {
  $featuredArticleOverlay.classList.add(
    "featured_article_preview__big-overlay"
  );
  $featuredArticleBody.classList.add("featured_article_preview__big-text");
});

$featuredArticleContainer.addEventListener("mouseout", () => {
  $featuredArticleOverlay.classList.remove(
    "featured_article_preview__big-overlay"
  );
  $featuredArticleBody.classList.remove("featured_article_preview__big-text");
});
