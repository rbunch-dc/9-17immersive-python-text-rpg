class Hero(object):
	def __init__(self, name = "Incognito"):
		# set up the object to remember it's name
		self.name = name
		self.health = 10
		self.power = 5
	def take_damage(self,amount_of_damage):
		self.health -= amount_of_damage
	def cheer_for_hero(self):
		print "Fight hard, valiant %s" % self.name
	def is_alive(self):
		return self.health > 0
