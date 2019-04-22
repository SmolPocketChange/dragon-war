# Imports
import pygame
import random

# Initialize game engine
pygame.init()


# Window
WIDTH = 1000
HEIGHT = 800
SIZE = (WIDTH, HEIGHT)
TITLE = "Dragon War"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (100, 255, 100)


# Fonts
FONT_SM = pygame.font.Font(None, 24)
FONT_MD = pygame.font.Font(None, 32)
FONT_LG = pygame.font.Font(None, 64)
FONT_XL = pygame.font.Font("assets/fonts/DragonForcE.ttf", 150)


# Images
blueFireball_img = pygame.image.load('assets/images/blueFireball.png').convert_alpha()
orangeFireball_img = pygame.image.load('assets/images/orangeFireball.png').convert_alpha()
laserGreenShot_img = pygame.image.load('assets/images/laserGreenShot.png').convert_alpha()
title_img = pygame.image.load('assets/images/DragonWarsCoverArt.png').convert()
background_img = pygame.image.load('assets/images/background.png').convert()
cloud1_img = pygame.image.load('assets/images/cloud1.png').convert_alpha()
cloud2_img = pygame.image.load('assets/images/cloud2.png').convert_alpha()
cloud3_img = pygame.image.load('assets/images/cloud3.png').convert_alpha()
laserRedShot_img = pygame.image.load('assets/images/laserRedShot.png').convert_alpha()
meteorSmall_img = pygame.image.load('assets/images/meteorSmall.png').convert_alpha()
boss_img = pygame.image.load('assets/images/boss.png').convert_alpha()






blueDragon_img1 = pygame.image.load('assets/images/BlueDragonFolder/blueDragonMovingOpen.png').convert_alpha()
blueDragon_img2 = pygame.image.load('assets/images/BlueDragonFolder/blueDragonMovingClosed.png').convert_alpha()
blueDragonLeft_img1 = pygame.image.load('assets/images/BlueDragonFolder/blueDragonMovingLeftOpen.png').convert_alpha()
blueDragonLeft_img2 = pygame.image.load('assets/images/BlueDragonFolder/blueDragonMovingLeftClosed.png').convert_alpha()
blueDragonRight_img1 = pygame.image.load('assets/images/BlueDragonFolder/blueDragonMovingRightOpen.png').convert_alpha()
blueDragonRight_img2 = pygame.image.load('assets/images/BlueDragonFolder/blueDragonMovingRightClosed.png').convert_alpha()

oneHitBlueDragon_img1 = pygame.image.load('assets/images/BlueDragonFolder/oneHitBlueDragonMovingOpen.png').convert_alpha()
oneHitBlueDragon_img2 = pygame.image.load('assets/images/BlueDragonFolder/oneHitBlueDragonMovingClosed.png').convert_alpha()
oneHitBlueDragonLeft_img1 = pygame.image.load('assets/images/BlueDragonFolder/oneHitBlueDragonMovingLeftOpen.png').convert_alpha()
oneHitBlueDragonLeft_img2 = pygame.image.load('assets/images/BlueDragonFolder/oneHitBlueDragonMovingLeftClosed.png').convert_alpha()
oneHitBlueDragonRight_img1 = pygame.image.load('assets/images/BlueDragonFolder/oneHitBlueDragonMovingRightOpen.png').convert_alpha()
oneHitBlueDragonRight_img2 = pygame.image.load('assets/images/BlueDragonFolder/oneHitBlueDragonMovingRightClosed.png').convert_alpha()

twoHitBlueDragon_img1 = pygame.image.load('assets/images/BlueDragonFolder/twoHitBlueDragonMovingOpen.png').convert_alpha()
twoHitBlueDragon_img2 = pygame.image.load('assets/images/BlueDragonFolder/twoHitBlueDragonMovingClosed.png').convert_alpha()
twoHitBlueDragonLeft_img1 = pygame.image.load('assets/images/BlueDragonFolder/twoHitBlueDragonMovingLeftOpen.png').convert_alpha()
twoHitBlueDragonLeft_img2 = pygame.image.load('assets/images/BlueDragonFolder/twoHitBlueDragonMovingLeftClosed.png').convert_alpha()
twoHitBlueDragonRight_img1 = pygame.image.load('assets/images/BlueDragonFolder/twoHitBlueDragonMovingRightOpen.png').convert_alpha()
twoHitBlueDragonRight_img2 = pygame.image.load('assets/images/BlueDragonFolder/twoHitBlueDragonMovingRightClosed.png').convert_alpha()

largeBlueDragon_img = pygame.image.load('assets/images/BlueDragonFolder/largeBlueDragon.png').convert_alpha()
largeBlueDragonLeft_img = pygame.image.load('assets/images/BlueDragonFolder/largeBlueDragonLeft.png').convert_alpha()
largeBlueDragonRight_img = pygame.image.load('assets/images/BlueDragonFolder/largeBlueDragonRight.png').convert_alpha()

redDragon_img1 = pygame.image.load('assets/images/RedDragonFolder/redDragonMovingOpen.png').convert_alpha()
redDragon_img2 = pygame.image.load('assets/images/RedDragonFolder/redDragonMovingClosed.png').convert_alpha()



zero_hit_imgs = [blueDragon_img1, blueDragon_img2]
zero_hit_left_imgs = [blueDragonLeft_img1, blueDragonLeft_img2]
zero_hit_right_imgs = [blueDragonRight_img1, blueDragonRight_img2]

one_hit_imgs = [oneHitBlueDragon_img1, oneHitBlueDragon_img2]
one_hit_left_imgs = [oneHitBlueDragonLeft_img1, oneHitBlueDragonLeft_img2]
one_hit_right_imgs = [oneHitBlueDragonRight_img1, oneHitBlueDragonRight_img2]

two_hit_imgs = [twoHitBlueDragon_img1, twoHitBlueDragon_img2]
two_hit_left_imgs = [twoHitBlueDragonLeft_img1, twoHitBlueDragonLeft_img2]
two_hit_right_imgs = [twoHitBlueDragonRight_img1, twoHitBlueDragonRight_img2]

invincibility_imgs = [largeBlueDragon_img, largeBlueDragon_img]
invincibility_left_imgs = [largeBlueDragonLeft_img, largeBlueDragonLeft_img]
invincibility_right_imgs = [largeBlueDragonRight_img, largeBlueDragonRight_img]

enemy_imgs = [redDragon_img1, redDragon_img2]

# Sounds
EXPLOSION = pygame.mixer.Sound('assets/sounds/explosion.ogg')
PEW = pygame.mixer.Sound('assets/sounds/fireball.ogg')

start_theme = "assets/sounds/dragons_village.ogg"
main_theme = "assets/sounds/rightside.ogg"
end_theme = "assets/sounds/coast.ogg"

# Stages
START = 0
PLAYING = 1
BOSS = 2
WIN = 3
LOSE = 4



# Game classes
class Main_Dragon(pygame.sprite.Sprite):
    def __init__(self, images):
        super().__init__()

        self.images = images
        self.image_index = 0
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 3
        self.max_health = 3
        self.health = self.max_health 
        self.shoots_double = False
        self.invincibility_timer = 0
        self.ticks = 0
        
    def move_left(self):
        self.rect.x -= self.speed

        if self.invincibility_timer > 0:
            self.images = invincibility_left_imgs
        elif self.health == 3:
            self.images = zero_hit_left_imgs
        elif self.health == 2:
            self.images = one_hit_left_imgs
        elif self.health == 1:
            self.images = two_hit_left_imgs

            
    def move_right(self):
        self.rect.x += self.speed
        if self.invincibility_timer > 0:
            self.images = invincibility_right_imgs
        elif self.health == 3:
            self.images = zero_hit_right_imgs
        elif self.health == 2:
            self.images = one_hit_right_imgs
        elif self.health == 1:
            self.images = two_hit_right_imgs
            
    def stop(self):
        if self.invincibility_timer > 0:
            self.images = invincibility_imgs
        elif self.health == 3:
            self.images = zero_hit_imgs
        elif self.health == 2:
            self.images = one_hit_imgs
        elif self.health == 1:
            self.images = two_hit_imgs
            
    def move_up(self):
        self.rect.y -= self.speed

    def move_down(self):
        self.rect.y += self.speed

    def shoot(self):
        print("Pew!")

        if self.shoots_double:
            blue_fireball1 = Blue_Fireball(blueFireball_img)
            blue_fireball1.rect.centerx = self.rect.centerx - 20
            blue_fireball1.rect.centery = self.rect.top
            blue_fireballs.add(blue_fireball1)

            blue_fireball2 = Blue_Fireball(blueFireball_img)
            blue_fireball2.rect.centerx = self.rect.centerx + 20
            blue_fireball2.rect.centery = self.rect.top
            blue_fireballs.add(blue_fireball2)
             
        else:
            blue_fireball = Blue_Fireball(blueFireball_img)
            blue_fireball.rect.centerx = self.rect.centerx
            blue_fireball.rect.centery = self.rect.top
            blue_fireballs.add(blue_fireball)

    def flap(self):
        self.image_index += 1
        if self.image_index > 1:
            self.image_index = 0
            
        self.image = self.images[self.image_index]
        
    def update(self):
        if self.ticks % 5 == 0:
            self.flap()
        self.ticks += 1
        
        '''check screen edges'''
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > WIDTH:
            self.rect.right = WIDTH
        elif self.rect.top < 0:
            self.rect.top = 0            
        elif self.rect.bottom > HEIGHT:
            self.rect.bottom= HEIGHT


        '''check orange_fireballs, powerups'''
        if self.invincibility_timer == 0:
            hit_list = pygame.sprite.spritecollide(self, orange_fireballs, True,
                                               pygame.sprite.collide_mask)
            for hit in hit_list:

                self.health -= 1
                print("ouch!")
                
                if self.health == 2:
                    self.images = one_hit_imgs
                elif self.health == 1:
                    self.images = two_hit_imgs

                if self.shoots_double:
                    self.shoots_double = False

        else:
            self.invincibility_timer -= 1
            
   
        hit_list = pygame.sprite.spritecollide(self, mobs, True,
                                               pygame.sprite.collide_mask)
        if self.health == 0 or len(hit_list) > 0:
            EXPLOSION.play()
            self.kill()

        hit_list = pygame.sprite.spritecollide(self, powerups, True,
                                               pygame.sprite.collide_mask)
        for hit in hit_list:
            hit.apply(self)


class Blue_Fireball(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 5

    def update(self):
        self.rect.y -= self.speed

        if self.rect.bottom < 0:
            self.kill()

class Mob(pygame.sprite.Sprite):
    def __init__(self, x, y, images):
        super().__init__()

        self.images = images
        self.image_index = 0
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.ticks = 0

    def drop_orange_fireball(self):
        print("BAM!")
        
        orange_fireball = Orange_Fireball(orangeFireball_img)
        orange_fireball.rect.centerx = self.rect.centerx
        orange_fireball.rect.centery = self.rect.bottom
        orange_fireballs.add(orange_fireball)

    def flap(self):
        self.image_index += 1
        if self.image_index > 1:
            self.image_index = 0
            
        self.image = self.images[self.image_index]

    def update(self):
        if self.ticks % 5 == 0:
            self.flap()
        self.ticks += 1
        
        hit_list = pygame.sprite.spritecollide(self, blue_fireballs, True,
                                               pygame.sprite.collide_mask)
        if len(hit_list) > 0:
            print("Boom!")
            EXPLOSION.play()
            self.kill()
            player.score += 3

class Orange_Fireball(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 3

    def update(self):
        self.rect.y += self.speed

        if self.rect.top > HEIGHT:
            self.kill()

class Fleet():
    def __init__(self, mobs):
        self.mobs = mobs
        self.speed = 5
        self.moving_right = True
        self.drop_speed = 30
        self.orange_fireball_rate = 20
                
        
    def move(self):
        hits_edge = False

        for m in mobs:
            if self.moving_right:
                m.rect.x += self.speed

                if m.rect.right >= WIDTH:
                    hits_edge = True

            else:
                m.rect.x -= self.speed

                if m.rect.left <= 0:
                    hits_edge = True
                    
        if hits_edge:
            self.reverse()
            self.move_down()
    
    def reverse(self):
        self.moving_right = not self.moving_right
    
    def move_down(self):
        for m in mobs:
            m.rect.y += self.speed

    def choose_orange_fireballer(self):
        rand = random.randrange(self.orange_fireball_rate)
        mob_list = mobs.sprites()

        if len(mob_list) > 0 and rand == 0:
            orange_fireballer = random.choice(mob_list)
            orange_fireballer.drop_orange_fireball()
    
    def update(self):
        self.move()
        self.choose_orange_fireballer()

class Boss(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.rect = image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y
        self.health = 10

    def drop_orange_fireball(self):
        print("BAM!")
        
        orange_fireball = Orange_Fireball(orangeFireball_img)
        orange_fireball.rect.centerx = self.rect.centerx
        orange_fireball.rect.centery = self.rect.bottom
        orange_fireballs.add(orange_fireball)

    def update(self):
        hit_list = pygame.sprite.spritecollide(self, blue_fireballs, True,
                                               pygame.sprite.collide_mask)
        for hit in hit_list:
            self.health -= 1
            
        if self.health <= 0:
            print("Boom!")
            EXPLOSION.play()
            self.kill()
            player.score += 1000
            

    
class Double_powerup(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.rect = image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 3
        self.rect.x = x
        self.rect.y = y

    def apply(self, main_dragon):
        main_dragon.shoots_double = True

    def update(self):
        self.rect.y += self.speed

        if self.rect.top > HEIGHT:
            self.kill()
        
            
class Health_powerup(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.rect = image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 3
        self.rect.x = x
        self.rect.y = y

    def apply(self, main_dragon):
        if main_dragon.health < main_dragon.max_health:
            main_dragon.health += 1

    def update(self):
        self.rect.y += self.speed

        if self.rect.top > HEIGHT:
            self.kill()

class Invincibility_powerup(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.rect = image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 3
        self.rect.x = x
        self.rect.y = y

    def apply(self, main_dragon):
        main_dragon.invincibility_timer = (5 * refresh_rate)

    def update(self):
        self.rect.y += self.speed

        if self.rect.top > HEIGHT:
            self.kill()
            

class Cloud(pygame.sprite.Sprite):
            
    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.rect = image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 1
        self.rect.x = x
        self.rect.y = y

    def update(self):
            self.rect.y += self.speed

            if self.rect.top > HEIGHT:
                self.rect.x = random.randrange(-100, WIDTH-100)
                self.rect.y = random.randrange(-1000, -100)

    
# Game helper functions
def show_title_screen():
    title_text = FONT_XL.render("Dragon Wars!", 1, WHITE)
    w = title_text.get_width()
    screen.blit(title_text, (WIDTH/2 - w/2, 300))

def show_win():
    title_text = FONT_XL.render("You Win!", 1, WHITE)
    w = title_text.get_width()
    screen.blit(title_text, (WIDTH/2 - w/2, 300))

    click_text = FONT_MD.render("Click SPACE to play again", 1, WHITE)
    w = title_text.get_width()
    screen.blit(click_text, (WIDTH/2, 500))

def show_lose():
    title_text = FONT_XL.render("You Lose", 1, WHITE)
    w = title_text.get_width()
    screen.blit(title_text, (WIDTH/2 - w/2, 300))

    click_text = FONT_MD.render("Click SPACE to play again", 1, WHITE)
    w = title_text.get_width()
    screen.blit(click_text, (WIDTH/2, 500))
    
def show_stats():
    score_txt = FONT_MD.render(str(player.score), 1, WHITE)
    screen.blit(score_txt, [980, 20])

    level_txt = FONT_MD.render(str(level), 1, WHITE)
    screen.blit(level_txt, [980, 40])

    health_bar = [20, 20, 50*main_dragon.health, 25]
    pygame.draw.rect(screen, GREEN, health_bar)
    pygame.draw.rect(screen, WHITE, [20, 20, 150, 25], 3)

def set_music(track):
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.fadeout(2500)

    if track != None:  
        pygame.mixer.music.load(track)
        pygame.mixer.music.play(-1)



def setup():
    global stage, done, stats, ticks, clouds, level, boss
    global player, main_dragon, blue_fireballs, mobs, fleet, orange_fireballs, powerups


    
    ''' Make game objects '''
    main_dragon = Main_Dragon(zero_hit_imgs)
    main_dragon.rect.centerx = WIDTH/2
    main_dragon.rect.bottom = HEIGHT

    ''' Make sprite groups '''
    player = pygame.sprite.GroupSingle()
    player.add(main_dragon)

    blue_fireballs = pygame.sprite.Group()
    orange_fireballs = pygame.sprite.Group()
    powerups = pygame.sprite.Group()

    
    clouds = pygame.sprite.Group()
    cloud_images = [cloud1_img, cloud2_img, cloud3_img]

    mob1 = Mob(100, 0, enemy_imgs)
    mob2 = Mob(300, 0, enemy_imgs)
    mob3 = Mob(500, 0, enemy_imgs)
    mob4 = Mob(200, 100, enemy_imgs)
    mob5 = Mob(400, 100, enemy_imgs)
    mob6 = Mob(100, 200, enemy_imgs)
    mob7 = Mob(300, 200, enemy_imgs)
    mob8 = Mob(500, 200, enemy_imgs)
    mob9 = Mob(200, 300, enemy_imgs)
    mob10 = Mob(400, 300, enemy_imgs)




    mobs = pygame.sprite.Group()
    mobs.add(mob1, mob2, mob3, mob4, mob5, mob6, mob7, mob8, mob9, mob10)

    fleet = Fleet(mobs)

    boss1 = Boss(WIDTH/2, 25, boss_img)
    boss = pygame.sprite.GroupSingle()
    boss.add(boss1)

    for n in range(10):
        x = random.randrange(0, WIDTH)
        y = random.randrange(-3000, -500)
        powerup1 = Double_powerup(x, y, laserGreenShot_img)
        powerup2 = Health_powerup(x, y, laserRedShot_img)
        powerup3 = Invincibility_powerup(x, y, meteorSmall_img)
        powerup = random.choice([powerup1, powerup2, powerup3])
        powerups.add(powerup)

    for c in range(30):
        x = random.randrange(-100, WIDTH-100)
        y = random.randrange(-100, WIDTH+100)

        img = random.choice(cloud_images)
        cloud = Cloud(x, y, img)
        clouds.add(cloud)

    


    ''' set stage '''
    player.score = 0
    level = 1
    ticks = 0
    stage = START
    set_music(start_theme)
    done = False

def check_win():
    global stage

    if len(player)== 0:
        stage = LOSE
        set_music(end_theme)
        
    if len(mobs) == 0:
        stage = BOSS

    if stage == BOSS and len(boss) == 0:
        stage = WIN
        set_music(end_theme)
    
# Game loop
setup()

while not done:
    # Input handling (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            if stage == START:
                if event.key == pygame.K_SPACE:
                    set_music(main_theme)
                    stage = PLAYING
            elif stage == PLAYING or BOSS:
                if event.key == pygame.K_SPACE:
                    main_dragon.shoot()
                    PEW.play()
            elif stage == WIN or LOSE:
                if event.key == pygame.K_SPACE:
                    setup()


    pressed = pygame.key.get_pressed()
    
    # Game logic (Check for collisions, update points, etc.)
    if stage == PLAYING or stage == BOSS:
        if pressed[pygame.K_LEFT]:
            main_dragon.move_left()
        elif pressed[pygame.K_RIGHT]:
            main_dragon.move_right()
        else:
            main_dragon.stop()
            
        if pressed[pygame.K_UP]:
            main_dragon.move_up()
        elif pressed[pygame.K_DOWN]:
            main_dragon.move_down()

        screen.blit(background_img, [0,0])
        player.update()
        clouds.update()
        blue_fireballs.update()
        mobs.update()
        fleet.update()
        orange_fireballs.update()
        powerups.update()
        check_win()

    elif stage == BOSS:
        boss.update()

        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)
    screen.blit(background_img, [0,0])
    clouds.draw(screen)
    blue_fireballs.draw(screen)
    player.draw(screen)

    orange_fireballs.draw(screen)
    powerups.draw(screen)
    show_stats()

               
    if stage == START:
        screen.blit(title_img, [0,0])
        show_title_screen()
    elif stage == PLAYING:
        mobs.draw(screen)
    elif stage == BOSS:
        boss.draw(screen)
    elif stage == WIN:
        show_win()
    elif stage == LOSE:
        show_lose()

        
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
