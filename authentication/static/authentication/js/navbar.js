const navToggle = document.querySelector(".navbar_toggle");
const link = document.querySelector(".main_nav");

navToggle.addEventListener('click', function () {
    link.classList.toggle("show_nav");
})