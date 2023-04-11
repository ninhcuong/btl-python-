
	def gameover(self, player):
		if self.mode == self.c.SINGLE:
			print ('gameover - lost all lives | or time ran out')
			self.highscores.addScore(player.score)
			self.gameIsActive = False
			self.exitGame = True