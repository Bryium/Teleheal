let menubar = document.querySelector('#menubar');
let mynav = document.querySelector('.navbar');


menubar.onclick = () => {
    menubar.classList.toggle('fa-times')
    mynav.classList.toggle('active')

}

function toggleMenu() {
    const  menu = document.querySelector('.menu-links');
    const  icon = document.querySelector('.hamburger-icon');
    menu.classList.toggle('open');
    icon.classList.toggle('open');
}

