const container = document.getElementById('container');
let counter = 0;

function newdiv() {
  const newDiv = document.createElement('div');
  newDiv.classList.add('div-container');
  newDiv.style.backgroundColor = colors[counter % colors.length];
  newDiv.textContent = `Div #${counter + 1}`;
  container.innerHTML = "";
  container.appendChild(newDiv);
}

setInterval(() => {
  createNewDiv();
  counter++;
}, 1000);
