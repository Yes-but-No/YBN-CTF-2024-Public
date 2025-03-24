// Select the canvas and set up the context
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
const launch = document.getElementById("launch");
// Define grid size
const gridSize = 21;
const cellSize = canvas.width / gridSize; 
var curIntensity = 5;
var nukes = []
var heatMap = []



function getRedShade(intensity) {
    // Define the color for regular red (e.g., #FF0000) and white
    const regularRed = { r: 255, g: 0, b: 0 };
    const white = { r: 255, g: 255, b: 255 };

    // Scale intensity to make 5 result in regular red, clamping values for smooth blending
    const factor = Math.min(intensity / 5, 1);

    // Blend between white and regular red based on the scaled intensity factor
    const r = Math.round(white.r + (regularRed.r - white.r) * factor);
    const g = Math.round(white.g + (regularRed.g - white.g) * factor);
    const b = Math.round(white.b + (regularRed.b - white.b) * factor);

    // Convert RGB to hex
    const hex = `#${((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1)}`;
    
    return hex;
}
// Function to draw the grid
function drawGrid(clear) {
    if (clear) ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear any previous drawings
    
    // Loop to draw vertical and horizontal lines
    for (let i = 0; i <= gridSize; i++) {
        // Draw vertical lines
        ctx.beginPath();
        ctx.moveTo(i * cellSize, 0);
        ctx.lineTo(i * cellSize, canvas.height);
        ctx.stroke();

        // Draw horizontal lines
        ctx.beginPath();
        ctx.moveTo(0, i * cellSize);
        ctx.lineTo(canvas.width, i * cellSize);
        ctx.stroke();
    }
}




// Function to load an image and draw it onto the grid at specified grid coordinates
function drawImageOnGrid(imageSrc, gridX, gridY) {
  // Load the image
  const image = new Image();
  image.src = imageSrc;
  
  // Draw the image when it loads
  image.onload = function () {
      // Calculate the pixel coordinates for the image based on the grid cell size
      const pixelX = gridX * cellSize;
      const pixelY = gridY * cellSize;
      
      // Draw the image onto the canvas at the calculated coordinates
      ctx.drawImage(image, pixelX, pixelY, cellSize, cellSize);
  };
}

function recalculateHeatMap(){
  for (let i = 0; i < gridSize; i++) {
    for (let j = 0; j < gridSize; j++) {
      heatMap[i][j] = 0
    }
  }
  for (let coords of nukes){
    for (let i = -curIntensity; i <= curIntensity; i++) {
      for (let j = -curIntensity; j <= curIntensity; j++) {
        if (coords[1] + i >= 0 && coords[1] + i < gridSize && coords[0] + j >= 0 && coords[0] + j < gridSize) {
          const distance = Math.max(Math.abs(i), Math.abs(j));
          heatMap[coords[1] + i][coords[0] + j] += Math.max(0, curIntensity - distance);
        }
      }
    }
  }
}
function drawNuke(gridX,gridY){
  nukes.push([gridX,gridY])
  recalculateHeatMap()
  drawAllNukes()
}

function removeNuke(gridX,gridY){
  nukes = nukes.filter(coords => coords[0] !== gridX || coords[1] !== gridY)
  recalculateHeatMap()
  drawAllNukes()
}
function drawAllNukes(){
  for (let i = 0; i < gridSize; i++) {
    for (let j = 0; j < gridSize; j++) {
      ctx.fillStyle = getRedShade(heatMap[i][j]);
      ctx.fillRect(j * cellSize, i * cellSize, cellSize, cellSize);
      
    }
  }
  for (let coords of nukes){
    drawImageOnGrid("images/nuke.png",coords[0],coords[1])
  }
  drawBaba()
  drawGrid(false)
}
function drawBaba(){
  drawImageOnGrid("images/baba.webp",10,10)
}

function handleOnClick(event) {
  // Calculate the grid coordinates based on the mouse click position
  const gridX = Math.floor(event.offsetX / cellSize);
  const gridY = Math.floor(event.offsetY / cellSize);
  // check if the click is on a nuke
  for (let coords of nukes){
    if (coords[0] === gridX && coords[1] === gridY){
      removeNuke(gridX,gridY)
      return
    }
  }
  // Draw the image on the grid at the calculated coordinates
  drawNuke(gridX,gridY)
}

function submitNukes(){
  fetch("/nuke", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({nukes:nukes,baba:[10,10]}),
  })
  .then((response) => response.json())
  .then((data) => {
    alert(data.result?data.result:data.error);
  })
}

function init(){
  // Initialize the grid drawing
  drawGrid(true);
  for (let i = 0; i < gridSize; i++) {
    heatMap.push(new Array(gridSize).fill(0));
  }
  drawNuke(6,10)
  drawNuke(14,10)
  drawNuke(10,6)
  drawNuke(10,14)
  canvas.addEventListener("click", handleOnClick);
  launch.addEventListener("click", submitNukes);
}

init()