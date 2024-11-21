class Path {
	constructor(x, y, Collidable) {
		this.Pos = createVector(x, y)
		this.size = 30
		this.Collide = Collidable
	}

	draw() {
		fill("black")
		circle(this.Pos.x, this.Pos.y, 3)
	}

	PositionCheck() {
		let GridPos = (Math.floor(this.Pos.x / 30)) + (Math.floor(this.Pos.y / 30) * 21)
		// print (GridPos)
	}
}

class Wall extends Path {


	draw() {
		fill("rgb(0,0,89)")
		rect(this.Pos.x, this.Pos.y, this.size)
	}


}


class Pellet extends Path {
	constructor(x, y, diameter, Collidable, score) {
		super(x, y, Collidable)
		this.Diameter = diameter
		this.Score = score
		this.Collected = false
		this.Mode = false

	}
	draw() {
		if (this.Collected == false) {
			fill("white")
			circle(this.Pos.x, this.Pos.y, this.Diameter)
		}
		this.CollectSystem()
	}

	CollectSystem() {
		let distance = p5.Vector.dist(this.Pos, pacman.Pos)
		if (distance == 0 && this.Collected == false) {
			this.Collected = true
			points(this.Score)
		}
	}
}


class PowerPellet extends Pellet {
	constructor(x, y, diameter, Collidable, score) {
		super(x, y, diameter, Collidable, score)
		this.Collected = false
		this.Timer = 6 * 60
		this.Count = 0
	}

	draw() {
		super.draw()
	}
	CollectSystem() {

		let distance = p5.Vector.dist(this.Pos, pacman.Pos)
		if (distance == 0 && this.Collected == false) {
			this.Collected = true
			this.Mode = true
			points(this.Score)
		}
		if (this.Collected == true && this.Mode == true) {
			pacman.KillMode = true
			this.Count++
		}
		if (this.Count >= this.Timer) {
			pacman.KillMode = false
			this.Count = 0
			this.Mode = false
		}
	}
}
