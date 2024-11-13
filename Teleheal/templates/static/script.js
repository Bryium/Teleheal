// Function to toggle the menu open and close
function toggleMenu() {
    const menu = document.querySelector('.navbar');
    const icon = document.querySelector('#menubar');
    menu.classList.toggle('open');
    icon.classList.toggle('open');
}

// Smooth scrolling function for navigation links
document.querySelectorAll('.navbar a').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();

        const targetId = this.getAttribute('href').substring(1);
        const targetSection = document.getElementById(targetId);

        if (targetSection) {
            window.scrollTo({
                top: targetSection.offsetTop,
                behavior: 'smooth'
            });

            // Close menu after click (for mobile view)
            const menu = document.querySelector('.navbar');
            menu.classList.remove('open');
            const icon = document.querySelector('#menubar');
            icon.classList.remove('open');
        }
    });
});



