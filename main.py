let North = 270
let East = 0
let South = 90
let West = 180
let gameWidth = 630
let gameHeight = 650

let pacman
let Ghosts = []


function setup() {
	createCanvas(gameWidth, gameHeight);
	background("black");
	angleMode(DEGREES)
	Generate()
}

function draw() {
	clear()
	for (o = 0; o < GenerateList.length; o++){
		GenerateList[o].draw()
	}
	if (pacman){
		pacman.draw()
		pacman.PositionCheck()
		pacman.MovementCheck()
	}
	points(0)
	Ghosts.forEach(Ghost => {
		Ghost.draw()
		Ghost.PositionCheck()
		Ghost.MovementCheck()
		Ghost.AlgorithmMovement()
	})	
}
