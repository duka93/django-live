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
    cover5.innerHTML = 'Profile &nbsp;';
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






