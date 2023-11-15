const header = document.querySelector("header");
window.addEventListener ("scroll", function() {
	header.classList.toggle ("sticky", window.scrollY > 100);
});

let menu = document.querySelector('#menu-icon');
let navlist = document.querySelector('.navlist');

menu.onclick = () => {
	menu.classList.toggle('bx-x');
	navlist.classList.toggle('open');
};

window.onscroll = () => {
	menu.classList.remove('bx-x');
	navlist.classList.remove('open');
};

const sr= ScrollReveal({
	distance: '60px',
	duration: 2500,
	reset: true
})
sr.reveal('.home-text',{delay:200, origin:'left'})
sr.reveal('.home-img',{delay:400, origin:'right'})
sr.reveal('.about-img',{delay:400, origin:'left'})
sr.reveal('.about-text',{delay:400, origin:'right'})
sr.reveal('.contact-text',{delay:400, origin:'left'})
sr.reveal('.contact-icon',{delay:400, origin:'left'})
sr.reveal('.contact-form',{delay:400, origin:'right'})
sr.reveal('.hobbies, .interest, .gallery',{delay:200, origin:'top'})

const announcements = document.querySelector('.announcements');
const announcementItems = document.querySelectorAll('.announcements span');

let currentSlide = 1;

function slideTo(index) {
  if (index < 1) {
    currentSlide = announcementItems.length;
  } else if (index > announcementItems.length) {
    currentSlide = 1;
  }

  const translateX = -100 * (currentSlide - 1);
  announcements.style.transform = `translateX(${translateX}%)`;
}

function autoSlide() {
  currentSlide++;
  slideTo(currentSlide);
}

setInterval(autoSlide, 3000); // Change slide every 3 seconds

