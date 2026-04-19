import pygame
import random
import sys

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
FPS = 60

# Player class
class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.color = (0, 0, 255)
        self.score = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        self.rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

# Ball class
class Ball:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, 20, 20)
        self.color = (255, 0, 0)
        self.speed = random.choice([-5, 5]), random.choice([-5, 5])

    def move(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed = -self.speed[0], self.speed[1]
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed = self.speed[0], -self.speed[1]

    def draw(self, surface):
        pygame.draw.ellipse(surface, self.color, self.rect)

# Main game function
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('2D Football Game')
    clock = pygame.time.Clock()

    player1 = Player(100, HEIGHT // 2)
    player2 = Player(WIDTH - 150, HEIGHT // 2)
    ball = Ball()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player1.move(0, -5)
        if keys[pygame.K_s]:
            player1.move(0, 5)
        if keys[pygame.K_UP]:
            player2.move(0, -5)
        if keys[pygame.K_DOWN]:
            player2.move(0, 5)

        ball.move()

        # Ball collision with players
        if ball.rect.colliderect(player1.rect) or ball.rect.colliderect(player2.rect):
            ball.speed = -ball.speed[0], ball.speed[1]

        screen.fill(GREEN)
        player1.draw(screen)
        player2.draw(screen)
        ball.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == '__main__':
    main()