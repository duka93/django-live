//HEADER

//Dodao za smanjivanje i povecavanje elemenata na vrhu
let cover1 = document.getElementById('cover1');

const eventHandle2 = function(){
    cover1.style.display = 'inline-block';
    cover1.style.fontSize = '17px';
    cover1.style.transitionDuration = '0.5s'
    cover1.style.transitionDelay = '0.1s'
}
document.getElementById('cover2').addEventListener('mouseover',eventHandle2)



let cover3 = document.getElementById('cover3');

const eventHandle4 = function(){
    cover3.style.fontSize = '17px';
    cover3.style.display = 'inline-block';
    cover3.style.transitionDuration = '0.5s'
    cover3.style.transitionDelay = '0.1s'
}
document.getElementById('cover4').addEventListener('mouseover',eventHandle4)


let cover0 = document.getElementById('cover0');
let cover10 = document.getElementById('cover10')

const eventHandle6 = function(){
    cover0.innerHTML = '&nbsp; Naslovna ';
    cover0.style.fontSize = '17px';
    cover0.style.display = 'inline-block';
    cover0.style.transitionDuration = '0.5s'
    cover0.style.transitionDelay = '0.1s'
}
const eventHandle7 = function(){
    cover0.style.fontSize = '0px';
    cover0.style.transitionDuration = '0.5s'
}
cover10.addEventListener('mouseover',eventHandle6)
cover10.addEventListener('mouseout',eventHandle7)



let cover5 = document.getElementById('cover5');

const eventHandle8 = function(){
    cover5.innerHTML = 'Profil &nbsp;';
    cover5.style.fontSize = '17px';
    cover5.style.display = 'inline-block';
    cover5.style.transitionDuration = '0.5s'
    cover5.style.transitionDelay = '0.1s'
}
document.getElementById('cover6').addEventListener('mouseover',eventHandle8)



let cover7 = document.getElementById('cover7');

const eventHandle13 = function(){
    cover7.innerHTML = 'Uputstvo &nbsp;';
    cover7.style.fontSize = '17px';
    cover7.style.display = 'inline-block';
    cover7.style.transitionDuration = '0.5s'
    cover7.style.transitionDelay = '0.1s'
}
document.getElementById('cover8').addEventListener('mouseover',eventHandle13)



//Genijalna funkcija za vracanje svih elemenata headera u prvobitno stanje
let modifikovanjeElemenata = document.querySelectorAll('.modifikovanje-elemenata');
let modifikovanjeElemenata1 = document.querySelectorAll('.modifikovanje-elemenata1');

modifikovanjeElemenata1.forEach(element => {
    element.addEventListener('mouseout', ()=>{
      modifikovanjeElemenata.forEach(element2 => {
        element2.style.fontSize = '0px';
        element2.style.transitionDuration = '0.5s'
      })
    });
 });

//Funkcija koja vraca dimenziju svih tekstualnih elemenata headera na nulu
 modifikovanjeElemenata.forEach(element => {
    element.style.fontSize = '0px';
 })


//Da navbar elementi budu providni na pocetku
const navChange = document.getElementsByClassName('navbar')[0];
const homeChange = document.getElementsByClassName('vrh')[0];
const elementChange = document.querySelectorAll('.decor');

elementChange.forEach(element => {
    element.style.backgroundColor = 'transparent';
    element.style.borderStyle = 'none'
})
navChange.style.backgroundColor = 'transparent';
homeChange.style.backgroundColor = 'transparent';
homeChange.style.borderStyle = 'none';


window.addEventListener('scroll', () => {
    if (window.scrollY > 10) {
        navChange.style.backgroundColor = 'white';
        navChange.style.transitionDuration = '0.6s';
        elementChange.forEach(element => {
            element.style.backgroundColor = ' #77C3EC';
            element.style.transitionDuration = '0.6s';
        })
        homeChange.style.backgroundColor = ' #77C3EC';
        homeChange.style.transitionDuration = '0.6s';
    }
    else{
        elementChange.forEach(element => {
            element.style.backgroundColor = 'transparent';
            element.style.borderStyle = 'none'
        })
        navChange.style.backgroundColor = 'transparent';
        homeChange.style.backgroundColor = 'transparent';
        homeChange.style.borderStyle = 'none';
    }
})




//Za uvelicavanje KONCEPT sekcije
let enlarge = document.getElementsByClassName('koncept')[0];

window.addEventListener('scroll',() => {
   if(window.scrollY >= 50 && window.scrollY <= 400){
       enlarge.style.paddingTop = '40px';
       enlarge.style.paddingBottom = '40px'
       enlarge.style.transitionDuration = '1s';
       enlarge.style.backgroundColor = 'beige';
   }
   if(window.scrollY > 400 || window.scrollY < 50){
       enlarge.style.padding = '';
       enlarge.style.fontSize = '';
       enlarge.style.transitionDuration = '1s';
       enlarge.style.backgroundColor = '';
   }
})



//Animacija oko ZABLUDA
const enlarge1 = document.querySelectorAll('.block');
const zabludeHeader = document.getElementById('zablude-h1')


window.addEventListener('scroll',() => {
     if(window.scrollY >=200){
        zabludeHeader.style.color = 'white';
        zabludeHeader.style.transitionDuration = '4s';
     }
})

window.addEventListener('scroll',() => {
    if(window.scrollY >= 700 && window.scrollY <= 1100){
        enlarge1.forEach(element => {
            element.style.padding = '10px';
            element.style.transitionDuration = '1.2s';
            element.style.backgroundColor = '#77C3EC';
        });
        document.getElementById('zablude').style.background='white';
        document.getElementById('zablude').style.transitionDuration='4s';
        document.getElementsByClassName('slike-za-fleks')[0].style.background='white';
        document.getElementsByClassName('slike-za-fleks')[0].style.transitionDuration='4s';
        };

    if(window.scrollY > 1350 || window.scrollY <700){
      enlarge1.forEach(element => {
        element.style.padding = '';
        element.style.transitionDuration = '0.6';
        element.style.backgroundColor = '';
    });
    document.getElementById('zablude').background = 'linear-gradient(#77C3EC, #89CFF0, #9DD9F3, #B8E2F2)';
    document.getElementById('zablude').style.transitionDuration='1s';
    document.getElementsByClassName('slike-za-fleks')[0].style.backgroundColor = '#B8E2F2';
    document.getElementsByClassName('slike-za-fleks')[0].style.transitionDuration='1s';
    };
});



//Za pojavljivanje FOOTER sekcije
const footerr = document.getElementById('footer');
footer.style.opacity = '0';


window.addEventListener('scroll', () => {
    if (window.scrollY > 2000){
        footer.style.opacity = '1';
        footer.style.transitionDuration = '3s';
        footer.style.transitionTimingFunction = 'ease-in-out';
    }
})

// ZA QA SAMO
/* <ul id='groceries'>
  <li id='must-have'>Toilet Paper</li>
  <li>Apples</li>
  <li>Chocolate</li>
  <li>Dumplings</li>
</ul>
let parentElement = document.getElementById('must-have').parentNode; // returns <ul> element
let childElements = document.getElementById('groceries').children; // returns an array of <li> elements */











