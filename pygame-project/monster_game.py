import pygame

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

class Warrior(pygame.sprite.Sprite):
    def __init__(self, image, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = [x,y]
        self.speed = 5
        

    def update(self):
        self.x = self.x + self.speed_x
        self.y = self.y + self.speed_y     

class Hero(Warrior):
    pass


class Monster(Warrior):
    def __init__(self):
        self.x = self.x +1  

          

        

def main():
    width = 512
    height = 480
    #blue_color = (97, 159, 182)

    pygame.init()
    
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    #clock = pygame.time.Clock()
    background_image = pygame.image.load('images/background.png').convert_alpha()
    hero_image = pygame.image.load('images/hero.png').convert_alpha()
    monster_image = pygame.image.load('images/monster.png').convert_alpha()

    player = Hero(hero_image, 250,250)
    monster = Monster(monster_image, 100,100)

    player_group = pygame.sprite.Group()
    player_group.add(player)

    monster_group = pygame.sprite.Group()
    monster_group.add(monster)

    # Game initialization

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling
            if event.type == pygame.KEYDOWN:
                # activate the cooresponding speeds
                # when an arrow key is pressed down
                if event.key == KEY_DOWN:
                    player.speed_y = player.speed_y + 5
                elif event.key == KEY_UP:
                    player.speed_y = player.speed_y - 5
                elif event.key == KEY_LEFT:
                    player.speed_x = player.speed_x - 5
                elif event.key == KEY_RIGHT:
                    player.speed_x = player.speed_x + 5
            if event.type == pygame.KEYUP:
                # deactivate the cooresponding speeds
                # when an arrow key is released
                if event.key == KEY_DOWN:
                    player.speed_y = 0
                elif event.key == KEY_UP:
                    player.speed_y = 0
                elif event.key == KEY_LEFT:
                    player.speed_x = 0
                elif event.key == KEY_RIGHT:
                    player.speed_x = 0
            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic

        # Draw background
        #screen.fill(blue_color)
        screen.blit(background_image,[0,0])
        player_group.draw(screen)
        monster_group.draw(screen)

        # Game display

        pygame.display.update()
        monster.x = monster.x + monster.speed_x
        #clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
