import pygame, sys


move_distance = 10


class Player(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		super().__init__()
		self.attack_animation = False
		self.sprites = []
		self.sonars  = []
		self.sprites.append(pygame.image.load('./img/uboot.png'))
		self.uboot = pygame.image.load('./img/uboot.png')
		#print(self.uboot.get_rect().center)
		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]

		self.rect = self.image.get_rect()
		self.rect.topleft = [pos_x,pos_y]



	def attack(self):
		self.attack_animation = True

	def sonar(self):
		self.sonars.append([(self.rect.topleft[0]+self.uboot.get_rect().center[0],self.rect.topleft[1]+self.uboot.get_rect().center[1]), 0 ])
		pygame.mixer.Sound.play(sonarping)


	def moveRight(self):
		self.rect.topleft = [self.rect.topleft[0]+move_distance,self.rect.topleft[1]]

	def moveUp(self,units):
		self.rect.topleft = [self.rect.topleft[0],self.rect.topleft[1]-units]  

	def moveLeft(self,units):
		self.rect.topleft = [self.rect.topleft[0]-units,self.rect.topleft[1]]  

	def moveDown(self,units):
		self.rect.topleft = [self.rect.topleft[0],self.rect.topleft[1]+units]  

	def setPositionY(self,position_Y):
		self.rect.topleft = [self.rect.topleft[0],position_Y]   

	def update(self,speed):
		if self.attack_animation == True:
			self.current_sprite += speed
			if int(self.current_sprite) >= len(self.sprites):
				self.current_sprite = 0
				self.attack_animation = False

		self.image = self.sprites[int(self.current_sprite)]

	

#
# day 1
#

file1 = open(r'F:\programming\python\adventofcode\1\input_2.txt', 'r')
#file1 = open('input.txt', 'r')
Lines = file1.readlines()
numbers = []
for ele in Lines:
    numbers.append(int(ele.replace('\n','')))
print(numbers)

#####

bg = pygame.image.load("./img/background.png")



# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("advent of code")

GAME_FONT = pygame.freetype.Font("font.ttf", 12)
#GAME_FONT = pygame.font.SysFont("comicsansms", 12)

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(100,numbers[0])
moving_sprites.add(player)

finish = False
print_grid = False
i = 0
time_elapsed_since_last_action = 0
lastDept = numbers[0]
deptIncreaseCounter = 0

sonarping = pygame.mixer.Sound('./sound/ping.wav')

animate_1 = False


while not finish:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			player.attack()
			if(event.key == pygame.K_w or event.key == pygame.K_RIGHT):
				player.moveRight()		
			if(event.key == pygame.K_s or event.key == pygame.K_DOWN):
				player.moveDown(10)	   
			if(event.key == pygame.K_UP):
				player.moveUp(10)	   
			if(event.key == pygame.K_LEFT):
				player.moveLeft(10)	  
			if(event.key == pygame.K_SPACE):
				player.sonar()		
			if(event.key == pygame.K_F1):
				if not animate_1:
					animate_1 = True
				else:
					animate_1 = False	
			if(event.key == pygame.K_t):
				player.setPositionY(numbers[i])
				player.sonar()
				i += 1
				if(i >= len(numbers)):
					finish = True								   
			if(event.key == pygame.K_q):
				pygame.quit()	
				sys.exit()
			if(event.key == pygame.K_x):
				if(print_grid):
					print_grid = False
				else:
					print_grid = True 	


	#INSIDE OF THE GAME LOOP
	screen.blit(bg, (0, 0))


	
	time_elapsed_since_last_action += 30


	if(time_elapsed_since_last_action  > 180 and animate_1):
		if(lastDept < numbers[i]):
			deptIncreaseCounter += 1
		time_elapsed_since_last_action = 0
		player.setPositionY(numbers[i])
		player.sonar()
		i += 1
		if(i >= len(numbers)):
			finish = True	

	# Drawing
	#screen.fill((0,0,0))

	#pygame.draw.line(screen, (200, 0, 0), rect, 1)	

	if(print_grid):
		blockSize = 20 #Set the size of the grid block
		for y in range(0, screen_height, blockSize):
			pygame.draw.line(screen, (200, 200, 200), (0,y),(screen_width,y), 1)	
			GAME_FONT.render_to(screen,(0,y),'depth: ' + str(y) ,(200,200,200),True)


	for ele in player.sonars:
		if(ele[1] >= 300):
			player.sonars.remove(ele)
		pygame.draw.circle(screen, (200,0,0,0.5), ele[0], ele[1],2)
		ele[1] += 3	

	moving_sprites.draw(screen)
	if(not i >= len(numbers)):
		GAME_FONT.render_to(screen,(600,10),'current depth: ' + str(numbers[i]) ,(200,0,0),True)
		GAME_FONT.render_to(screen,(600,30),'current fps  : ' + str(int(clock.get_fps())) ,(200,0,0),True)
		GAME_FONT.render_to(screen,(600,50),'dept increase: ' + str(deptIncreaseCounter) ,(200,0,0),True)





	pygame.display.flip()
	clock.tick(30)