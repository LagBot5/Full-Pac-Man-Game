class Ghost extends Pacman {
	constructor(x, y, colour, algorithm, AIlevel) {
		super(x, y)
		this.Xspeed = 0
		this.Yspeed = 0
		this.speed = 1.5
		this.GridPos = 0
		this.Colour = colour
		this.Size = 27
		this.Algorithm = algorithm
		this.AlgStep = 0
		this.AIlevel = AIlevel
		this.GivenMove = false

	}

	PositionCheck() {
		super.PositionCheck()
	}

	MovementCheck() {
		super.MovementCheck()
	}

	Killmode() {
		let distance = p5.Vector.dist(this.Pos, pacman.Pos)
		fill(this.Colour)
		circle(this.Pos.x, this.Pos.y, this.Size)
		this.speed = 1.5
		if (distance <= this.Size / 2 + pacman.Diameter / 2) {
			print('kill')
			return "kill"
		} else {
			return "alive"
		}

	}
	Deathmode() {
		fill('rgb(0,52,255)')
		circle(this.Pos.x, this.Pos.y, this.Size)
		this.speed = 1
		let distance = p5.Vector.dist(this.Pos, pacman.Pos)
		if (distance <= this.Size + pacman.Diameter) {
			return "dead"
		} else {
			return "alive"
		}
	}

	draw() {
		if (pacman.KillMode == false) {
			this.Killmode()
		} else if (pacman.KillMode == true) {
			this.Deathmode()
		}

		this.Pos.x += this.Xspeed
		this.Pos.y += this.Yspeed

	}

	AlgorithmMovement() {
		let step
		let timer = 120
		let count = 0

		if (this.AlgStep < this.Algorithm.length && pacman.KillMode == false) {
			step = this.Algorithm[this.AlgStep]
			this.GivenMove = true
		}
		if (this.AlgStep >= this.Algorithm.length && pacman.KillMode == false) {

			if (this.AIlevel == 1) {


				if (this.GivenMove == false) {
					step = Math.round(random(0, 4))

				}
				count++
				if (this.Xspeed == 0 && this.Yspeed == 0 && count >= timer) {
					step = Math.round(random(0, 4))
				}

			}
			if (this.AIlevel == 2) {

			}
			if (this.AIlevel == 3) {
				print('level 3')

				let Distance = p5.Vector.dist(this.Pos, pacman.Pos)
				let possibleDistance
				let bestDistance = 0
				let bestChoice
				let North = GenerateList[this.GridPos - 21]
				let East = GenerateList[this.GridPos + 1]
				let South = GenerateList[this.GridPos + 21]
				let West = GenerateList[this.GridPos - 1]

				if (North.Collide == false) {
					possibleDistance = p5.Vector.dist(North.Pos, pacman.Pos)
					if (bestDistance == 0 || possibleDistance < bestDistance) {
						bestDistance = possibleDistance
						bestChoice = 1
					}
				}
				if (East.Collide == false) {
					possibleDistance = p5.Vector.dist(East.Pos, pacman.Pos)
					if (bestDistance == 0 || possibleDistance < bestDistance) {
						bestDistance = possibleDistance
						bestChoice = 2
					}
				}
				if (South.Collide == false) {
					possibleDistance = p5.Vector.dist(South.Pos, pacman.Pos)
					if (bestDistance == 0 || possibleDistance < bestDistance) {
						bestDistance = possibleDistance
						bestChoice = 3
					}
				}
				if (West.Collide == false) {
					possibleDistance = p5.Vector.dist(West.Pos, pacman.Pos)
					if (bestDistance == 0 || possibleDistance < bestDistance) {
						bestDistance = possibleDistance
						bestChoice = 4
					}
				}
				step = bestChoice
			}
		} else if (this.AlgStep >= this.Algorithm.length && pacman.KillMode == true) {
			let Distance = p5.Vector.dist(this.Pos, pacman.Pos)
			let possibleDistance
			let bestDistance = 0
			let bestChoice
			let North = GenerateList[this.GridPos - 21]
			let East = GenerateList[this.GridPos + 1]
			let South = GenerateList[this.GridPos + 21]
			let West = GenerateList[this.GridPos - 1]

			if (North.Collide == false) {
				possibleDistance = p5.Vector.dist(North.Pos, pacman.Pos)
				if (bestDistance == 0 || possibleDistance > bestDistance) {
					bestDistance = possibleDistance
					bestChoice = 1
				}
			}
			if (East.Collide == false) {
				possibleDistance = p5.Vector.dist(East.Pos, pacman.Pos)
				if (bestDistance == 0 || possibleDistance > bestDistance) {
					bestDistance = possibleDistance
					bestChoice = 2
				}
			}
			if (South.Collide == false) {
				possibleDistance = p5.Vector.dist(South.Pos, pacman.Pos)
				if (bestDistance == 0 || possibleDistance > bestDistance) {
					bestDistance = possibleDistance
					bestChoice = 3
				}
			}
			if (West.Collide == false) {
				possibleDistance = p5.Vector.dist(West.Pos, pacman.Pos)
				if (bestDistance == 0 || possibleDistance > bestDistance) {
					bestDistance = possibleDistance
					bestChoice = 4
				}
			}
			step = bestChoice
		}



		if (this.Pos.x == GenerateList[this.GridPos].Pos.x && this.Pos.y == GenerateList[this.GridPos].Pos.y) {


			if (step == 1) {
				if (GenerateList[this.GridPos - 21].Collide == false) {
					this.Yspeed = this.speed * -1
					this.Xspeed = 0
					// this.GivenMove = false
					this.AlgStep++
				}
			}
			if (step == 2) {
				if (GenerateList[this.GridPos + 1].Collide == false) {
					this.Xspeed = this.speed
					this.Yspeed = 0
					this.GivenMove = false
					this.AlgStep++
				}
			}
			if (step == 3) {
				if (GenerateList[this.GridPos + 21].Collide == false) {
					this.Yspeed = this.speed
					this.Xspeed = 0
					this.GivenMove = false
					this.AlgStep++
				}
			}
			if (step == 4) {
				if (GenerateList[this.GridPos - 1].Collide == false) {
					this.Xspeed = this.speed * -1
					this.Yspeed = 0
					this.GivenMove = false
					this.AlgStep++
				}
			}
			// print(this.GivenMove)
			// if (this.GivenMove == false){
			// 	print('hello')
			// 	this.AlgStep++

		}
	}
}
