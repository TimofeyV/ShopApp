/* =====typed js====== */
var typed = new Typed('#element', {
    strings: ['Junior Backend Developer',
                'Студент университета',
                'Любитель головоломок'],
      typeSpeed: 100,
      backSpeed: 100,
      backDelay: 3000,
      loop: true
  });

/* =====toggle icon navbar====== */
let menuIcon = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');

menuIcon.onclick = () => {
  menuIcon.classList.toggle('bx-menu-alt-right');
  navbar.classList.toggle('active');
};

/* =====remove navbar when click====== */

  menuIcon.classList.remove('bx-menu-alt-right');
  navbar.classList.remove('active');


/* scroll */

  let sections = document.querySelectorAll('section');
  let navLinks = document.querySelectorAll('header nav a');

window.onscroll = () => {
  sections.forEach(sec => {
      let top = window.scrolly;
      let offset = sec.offsetTop - 150;
      let height = sec.offsetHeight;
      let id = sec.getAttribute('id');

      if(top >= offset && top < offset + height){
          navLinks.forEach(links =>{
              links.classList.remove('active');
              document.querySelector('header nav a[href* = ' + id + ']').classList.add('active');
          });
      };
  });

  let header = document.querySelector('header');

  header.classList.toggle('sticky', window.scrolly > 100);

  menuIcon.classList.remove('bx-menu-alt-right');
  navbar.classList.remove('active');
};