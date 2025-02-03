// 21x21
let GenerateList = []
let Ghost1Alg = [1, 2, 1, 2, 1, 2]
let Ghost2Alg = [2, 1, 4, 3, 2, 3]
let Ghost3Alg = [1, 4, 3, 4, 1, 4]
let Ghost4Alg = [4, 1, 2, 3, 4, 3]

function Generate() {
	let posX;
	let posY;

	const MapGenerate = [
		0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
		0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0,
		0, 1, 3, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 3, 1, 0,
		0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0,
		0, 1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 0,
		0, 1, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 1, 0,
		0, 1, 1, 1, 1, 2, 1, 1, 1, 0, 1, 0, 1, 1, 1, 2, 1, 1, 1, 1, 0,
		0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0,
		1, 1, 1, 1, 1, 2, 1, 0, 1, 1, 5, 1, 1, 0, 1, 2, 1, 1, 1, 1, 1,
		0, 0, 0, 0, 0, 2, 0, 0, 1, 6, 7, 8, 1, 0, 0, 2, 0, 0, 0, 0, 0,
		1, 1, 1, 1, 1, 2, 1, 0, 1, 1, 1, 1, 1, 0, 1, 2, 1, 1, 1, 1, 1,
		0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0,
		0, 1, 1, 1, 1, 2, 1, 0, 1, 1, 1, 1, 1, 0, 1, 2, 1, 1, 1, 1, 0,
		0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0,
		0, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1, 0,
		0, 1, 3, 2, 1, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 2, 1, 2, 3, 1, 0,
		0, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 0,
		0, 1, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 1, 0,
		0, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 0,
		0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0,
		0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0
	]

	// Empty = 0
	// Wall = 1
	// Pellet = 2
	// PowerPoint = 3
	// PacMan = 4
	// Ghost = 5

	let h = 0
	let length = 21
	let n = MapGenerate.length

	for (let i = 0; i < n; i++) {
		let row = Math.floor(i / length)
		let col = i % length
		let posx = col * 30
		let posy = row * 30

		if (MapGenerate[i] == 0) {
			GenerateList.push(new Path(posx + 15, posy + 15, false))
		}
		if (MapGenerate[i] == 1) {
			GenerateList.push(new Wall(posx, posy, true))
		}

		if (MapGenerate[i] == 2) {
			GenerateList.push(new Pellet(posx + 15, posy + 15, 10, false, 20))
		}

		if (MapGenerate[i] == 3) {
			GenerateList.push(new PowerPellet(posx + 15, posy + 15, 20, false, 100))
		}

		if (MapGenerate[i] == 4) {
			pacman = new Pacman(posx + 15, posy + 15)
			GenerateList.push(new Path(posx + 15, posy + 15, false))
		}
		if (MapGenerate[i] == 5) {
			Ghosts.push(new Ghost(posx + 15, posy + 15, 'red', Ghost1Alg, 1))
			GenerateList.push(new Path(posx + 15, posy + 15, false))
		}
		if (MapGenerate[i] == 6) {
			Ghosts.push(new Ghost(posx + 15, posy + 15, 'rgb(77,242,254)', Ghost2Alg, 1))
			GenerateList.push(new Path(posx + 15, posy + 15, false))
		}
		if (MapGenerate[i] == 7) {
			Ghosts.push(new Ghost(posx + 15, posy + 15, 'pink', Ghost3Alg, 3))
			GenerateList.push(new Path(posx + 15, posy + 15, false))
		}
		if (MapGenerate[i] == 8) {
			Ghosts.push(new Ghost(posx + 15, posy + 15, 'yellow', Ghost4Alg, 3))
			GenerateList.push(new Path(posx + 15, posy + 15, false))
		}
	}
}
