var counterDisplay = document.getElementById("display");
let count = 0;
function increasecounter(){
    count++;
    counterDisplay.innerHTML=count;
};
function decreasecounter(){
    count--;
    counterDisplay.innerHTML=count;
};
function resetcounter(){
    count = 0;
    counterDisplay.innerHTML=count;
};