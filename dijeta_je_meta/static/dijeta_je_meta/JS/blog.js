let cover0 = document.getElementById('cover0');
let cover10 = document.getElementById('cover10');

cover0.style.fontSize = '0px';

const eventHandle6 = function(){
    cover0.innerHTML = 'Naslovna &nbsp;';
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
let cover6 = document.getElementById('cover6');

cover5.style.fontSize = '0px';

const eventHandle8 = function(){
    cover5.innerHTML = 'Socials &nbsp;';
    cover5.style.fontSize = '17px';
    cover5.style.display = 'inline-block';
    cover5.style.transitionDuration = '0.5s'
    cover5.style.transitionDelay = '0.1s'
}
const eventHandle9 = function(){
    cover5.style.fontSize = '0px';
    cover5.style.transitionDuration = '0.5s'
}

cover6.addEventListener('mouseover',eventHandle8)
cover6.addEventListener('mouseout',eventHandle9)









//za svaki kliknuti lajk menja se boja

const elements = document.querySelectorAll('.button');

elements.forEach(element => {
    element.addEventListener('click', (e)=>{
      e.target.style.color = 'green';
    });
 });

