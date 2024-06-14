import pygame

pygame.init()
screen = pygame.display.set_mode((480, 320))  # Adjust as per your screen resolution

def display_expression(image_path):
    image = pygame.image.load(image_path)
    screen.blit(image, (0, 0))
    pygame.display.update()

# Example usage
display_expression("happy_face.png")  # Replace with actual path to image file

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
