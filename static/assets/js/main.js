const video = document.getElementById("fitnessVideo");
const title = document.getElementById("videoTitle");

video.addEventListener("mouseenter", () => {
  video.play();
  title.style.opacity = "0";
});

video.addEventListener("mouseleave", () => {
  video.pause();
  title.style.opacity = "1";
});
