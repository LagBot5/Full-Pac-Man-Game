class Pacman {
	constructor(x, y) {
		this.Pos = createVector(x, y)
		this.GridPos = 0
		this.Colour = "yellow"
		this.Diameter = 25
		this.AngleA = 0
		this.AngleB = 360
		this.Xspeed = 0
		this.Yspeed = 0
		this.MouthSpeed = 5
		this.Direction = 0
		this.Speed = 1.5
		this.KillMode = false
	}

	PositionCheck() {
		this.GridPos = (Math.floor(this.Pos.x / 30)) + (Math.floor(this.Pos.y / 30) * 21)
	}
	MovementCheck() {
		let North = this.GridPos - 21
		let East = this.GridPos + 1
		let South = this.GridPos + 21
		let West = this.GridPos - 1

		if (this.Pos.x == GenerateList[this.GridPos].Pos.x && this.Pos.y == GenerateList[this.GridPos].Pos.y) {

			if (this.Xspeed < 0) {
				if (GenerateList[West].Collide == true) {
					this.Xspeed = 0
					this.Yspeed = 0
				}
			}

			if (this.Xspeed > 0) {
				if (GenerateList[East].Collide == true) {
					this.Xspeed = 0
					this.Yspeed = 0
				}
			}

			if (this.Yspeed < 0) {
				if (GenerateList[North].Collide == true) {
					this.Yspeed = 0
					this.Xspeed = 0
				}
			}

			if (this.Yspeed > 0) {
				if (GenerateList[South].Collide == true) {
					this.Yspeed = 0
					this.Xspeed = 0
				}
			}
		}
	}

	draw() {
		fill('yellow')

		// this code opens and closes the mouth
		if (this.Xspeed == 0 && this.Yspeed == 0) {
			this.MouthSpeed = 0
		} else {

			if (this.AngleA >= this.Direction + 55) {
				this.MouthSpeed = -5
			} else if (this.AngleA <= this.Direction) {
				this.MouthSpeed = 5
			}
		}

		// this code moves pacman's mouth, body, and draws him
		arc(this.Pos.x, this.Pos.y, this.Diameter, this.Diameter, this.AngleA, this.AngleB)
		this.Pos.x += this.Xspeed
		this.Pos.y += this.Yspeed
		this.AngleA += this.MouthSpeed
		this.AngleB -= this.MouthSpeed
	}
}
