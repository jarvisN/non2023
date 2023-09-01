import pygame
import random
import serial
import time
import os

# Initialize pygame
pygame.init()

# Set up display
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ball Game")

# Set up fonts
font = pygame.font.SysFont(None, 48)

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set up serial port
# ser = serial.Serial('/dev/tty.usbserial-0001', 115200)
ser = serial.Serial('/dev/tty.ESP32test', 115200) 
balloon_img = pygame.image.load(os.path.join('balloon.png'))
balloon_img = pygame.transform.scale(balloon_img, (100, 200))



def create_new_ball():
    return {'x': random.randint(50, width-50), 'y': height - 50, 'dx': 0, 'dy': -0.125, 'number': random.randint(1, 5)}

def draw_ball(number, x, y):
    # # Draw the circle
    # pygame.draw.circle(window, black, (x, y), 50, 5)

    window.blit(balloon_img, (x - balloon_img.get_width() / 2, y - balloon_img.get_height() / 2))
    
    
    # Draw the ball number
    text = font.render(str(number), True, (0, 0, 0))
    window.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

def draw_text(text, x, y):
    surface = font.render(text, True, black)
    window.blit(surface, (x, y))

def main():
    running = True
    score = 0
    balls = [create_new_ball() for _ in range(8)]
    start_time = time.time()
    game_time = time.time()
    ball_create_time = time.time()
    
    while running:
        # Check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # End game after 30 seconds
        current_game_time = time.time()
        if current_game_time - game_time >= 30:
            print("Time's up! Your score is:", score)
            running = False
        
        # Create a new ball every 1 second
        current_time = time.time()
        if current_time - ball_create_time >= 1:
            if len(balls) < 5 or len(balls) > 0:
                balls.append(create_new_ball())
                balls.append(create_new_ball())
            else:
                print("Too many balls! Your score is:", score)
                running = False
            ball_create_time = current_time
        
        # Check if data is available from ESP32
        if ser.in_waiting:
            # Read data from ESP32
            data = ser.readline().strip()
            
            # Try to convert the data to an integer
            try:
                data = int(data)
            except ValueError:
                continue
            
            # Check if the data matches any ball number
            for ball in balls:
                if data == ball['number']:
                    # Destroy the ball
                    ball['number'] = 0
                    score += 1
                    break
        
        # Move the balls
        new_balls = []
        for ball in balls:
            if ball['y'] <= height - 50:
                ball['x'] += ball['dx']
                ball['y'] += ball['dy']
                new_balls.append(ball)
        balls = new_balls
        
        # Draw the balls and text
        window.fill(white)
        for ball in balls:
            if ball['number'] != 0:
                draw_ball(ball['number'], ball['x'], ball['y'])
        draw_text("Score: " + str(score), 10, 10)
        draw_text("Time remaining: " + str(int(30 - (current_game_time - game_time))), 10, 50)
        pygame.display.update()
        
    pygame.quit()

if __name__ == "__main__":
    main()