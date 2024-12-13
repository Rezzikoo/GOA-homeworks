
const incrementButton = document.getElementById("incrementButton");
const decrementButton = document.getElementById("decrementButton");
const resetButton = document.getElementById("resetButton");
const counter = document.getElementById("counter");


let count = 0;


function updateCounterColor() {
    if (count < 0) {
        counter.style.color = "red";
    } else if (count > 0) {
        counter.style.color = "green"; 
    }
}
    
    


function increment() {
    count++;
    counter.innerText = count;
    updateCounterColor(); 
}


function decrement() {
    count--;
    counter.innerText = count;
    updateCounterColor(); 
}


function reset() {
    count = 0;
    counter.innerText = count;
    updateCounterColor(); 
}


incrementButton.onclick = increment;
decrementButton.onclick = decrement;
resetButton.onclick = reset;


