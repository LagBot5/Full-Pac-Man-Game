function keyPressed(){
	// let distance = p5.Vector.dist( pacman.Pos, GenerateList[pacman.GridPos].Pos)
	// d
	if (keyCode === 68 || keyCode === RIGHT_ARROW){
		if (GenerateList[pacman.GridPos + 1].Collide == false ){
			pacman.Pos.x = GenerateList[pacman.GridPos].Pos.x
			pacman.Pos.y = GenerateList[pacman.GridPos].Pos.y
			pacman.Xspeed = pacman.Speed
			pacman.Yspeed = 0
			pacman.AngleA = East
			pacman.AngleB = East + 360
			pacman.Direction = East
		}
	}
	// a
	else if (keyCode === 65 || keyCode === LEFT_ARROW){
		if (GenerateList[pacman.GridPos - 1].Collide == false){
			pacman.Pos.x = GenerateList[pacman.GridPos].Pos.x
			pacman.Pos.y = GenerateList[pacman.GridPos].Pos.y
			pacman.Xspeed = pacman.Speed*-1
			pacman.Yspeed = 0
			pacman.AngleA = West
			pacman.AngleB = West + 360
			pacman.Direction = West
		}
	}
	// s
	else if (keyCode === 83 || keyCode === DOWN_ARROW){
		if (GenerateList[pacman.GridPos + 21].Collide == false){
			pacman.Pos.x = GenerateList[pacman.GridPos].Pos.x
			pacman.Pos.y = GenerateList[pacman.GridPos].Pos.y
			pacman.Xspeed = 0
			pacman.Yspeed = pacman.Speed
			pacman.AngleA = South
			pacman.AngleB = South + 360
			pacman.Direction = South
		}
	}
	// w
	else if (keyCode === 87 || keyCode === UP_ARROW){
		if (GenerateList[pacman.GridPos - 21].Collide == false){
			pacman.Pos.x = GenerateList[pacman.GridPos].Pos.x
			pacman.Pos.y = GenerateList[pacman.GridPos].Pos.y
			pacman.Xspeed = 0
			pacman.Yspeed = pacman.Speed*-1
			pacman.AngleA = North
			pacman.AngleB = North + 360
			pacman.Direction = North
		}
	}
	else if (keyCode === 70){
		pacman.Xspeed = 0
		pacman.Yspeed = 0
	}
	if (keyIsDown(80)){
		points(50)
	}
	if (keyIsDown(79)){
		points(200)
	}
}
