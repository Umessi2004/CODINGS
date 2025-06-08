function clock() {
    const date = new Date();
    let hours = date.getHours().toString().padStart(2, '0');
    let minutes = date.getMinutes().toString().padStart(2, '0');
    let seconds = date.getSeconds().toString().padStart(2, '0');
    document.getElementById("clock_display").textContent = `${hours}:${minutes}:${seconds}`;
};

setInterval(clock, 1000); 
clock(); // Initial call to display the clock immediately