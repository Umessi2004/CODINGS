var counterDisplay = document.getElementById("display");
let count = 0;
function increasecounter() {
    // var increaseButton = document.getElementById("increase");
    if (count >= 20) {
        alert("Counter cannot exceed 20!");
        return;
    }
    counterDisplay.textContent = ++count;
};
function decreasecounter() {
    // var decreaseButton = document.getElementById("decrease");
    if (count <= 0) {
        alert("Counter cannot go below zero!");
        return;
    }
    counterDisplay.textContent = --count;
};
function resetcounter() {
    // var resetButton = document.getElementById("reset");
    if (count !== 0) {
        count = 0;
        counterDisplay.textContent = count;
    }
    else {
        alert("Counter is already at zero!");
    }
};
document.addEventListener("keydown", function(event) {
    if (event.key === "Enter"){
        alert("You pressed Enter! Use the buttons to change the counter.");
    }
});