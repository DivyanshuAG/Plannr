const navSlideIn = () => {
    const menu = document.querySelector('.menu');
    const nav = document.querySelector('.nav-links');
    const nav_links = document.querySelectorAll('.nav-links li')

    menu.addEventListener('click', () => {
        nav.classList.toggle('nav-active');

        nav_links.forEach((link, index) => {
            if (link.style.animation) {
                link.style.animation = '';
            }
        else {
                link.style.animation = `navLinks 0.5s ease forwards ${index / 5 + 0.5}s`;
            }
        })
        menu.classList.toggle('toggle');
    })

}
navSlideIn();