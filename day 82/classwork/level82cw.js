function RandomDisplay() {
    let mode = "number";
    let value = "";
    let running = false;
  
    const numbers = Array.from({ length: 100 }, i + 1);
    const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  
    function updateDisplay() {
      if (!running) return;
      if (mode === "number") {
        value = numbers[Math.floor(Math.random() * numbers.length)];
      } else {
        value = letters[Math.floor(Math.random() * letters.length)];
      }
      document.getElementById("display").Text = value;
      setTimeout(updateDisplay, 1000);
    }
  
    function start() {
      if (!running) {
        running = true;
        updateDisplay();
      }
    }
  
    function stop() {
      running = false;
    }
  
    return (
      <div>
        <label>
          <input type="radio" name="mode" onclick={(mode = "number")} /> 
        </label>
        <label>
          <input type="radio" name="mode" onclick={(mode = "letter")} /> 
        </label>
        <div id="display"></div>
        <button onclick={start}>Start</button>
        <button onclick={stop}>Stop</button>
      </div>
    );
  }