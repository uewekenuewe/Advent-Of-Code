import pygame, sys

class Player(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		super().__init__()
		self.attack_animation = False
		self.sprites = []
		self.sonars  = []
		self.sprites.append(pygame.image.load('uboot.png'))
		#self.uboot = pygame.image.load('uboot.png')
		#print(self.uboot.get_rect().center)
		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]

		self.rect = self.image.get_rect()
		self.rect.topleft = [pos_x,pos_y]



	def attack(self):
		self.attack_animation = True

	def sonar(self):
		print(self.rect.topleft)
		self.sonars.append([self.rect.topleft, 0 ])

	def move(self):
		self.rect.topleft = [self.rect.topleft[0]+20,self.rect.topleft[1]]

	def update(self,speed):
		if self.attack_animation == True:
			self.current_sprite += speed
			if int(self.current_sprite) >= len(self.sprites):
				self.current_sprite = 0
				self.attack_animation = False

		self.image = self.sprites[int(self.current_sprite)]

	
# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("advent of code")

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(100,100)
moving_sprites.add(player)

finish = False


while not finish:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			player.attack()
	#player.move()	

	pressed = pygame.key.get_pressed()
	if(pressed[pygame.K_s]):
		player.sonar()
	if(pressed[pygame.K_w]):
		player.move()		
	if(pressed[pygame.K_q]):
		pygame.quit()	
		sys.exit()
	# Drawing
	screen.fill((0,0,0))

	blockSize = 20 #Set the size of the grid block
	for x in range(0, screen_width, blockSize):
		for y in range(0, screen_height, blockSize):
			rect = pygame.Rect(x, y, blockSize, blockSize)
			pygame.draw.rect(screen, (200, 200, 200), rect, 1)	


	for ele in player.sonars:
		if(ele[1] >= 300):
			player.sonars.remove(ele)
		pygame.draw.circle(screen, (200,0,0,0.5), ele[0], ele[1],2)
		ele[1] += 3	

	moving_sprites.draw(screen)
	moving_sprites.update(0.25)

	

	pygame.display.flip()
	clock.tick(30)