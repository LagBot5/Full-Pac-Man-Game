let score = 0

function points(NumberAdd) {
	score += NumberAdd
	fill("white")
	textSize(20)
	text("Score: " + score, 20, 30)
	return score
}
