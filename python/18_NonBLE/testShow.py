import pygame
import random
import serial
import time

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
ser = serial.Serial('/dev/tty.usbserial-0001', 115200)

def create_new_ball():
    return {'x': random.randint(50, width-50), 'y': random.randint(50, height-50), 'dx': 0, 'dy': 0.25, 'number': random.randint(1, 5)}

def draw_ball(number, x, y):
    # Draw the circle
    pygame.draw.circle(window, black, (x, y), 50, 5)  # the last parameter is the width of the circle outline
    
    # Draw the ball number
    text = font.render(str(number), True, (255, 0, 0))  # change text color to red
    window.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

def main():
    running = True
    score = 0
    balls = [create_new_ball() for _ in range(3)]
    start_time = time.time()
    
    while running:
        # Check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Create a new ball every 3 seconds
        current_time = time.time()
        if current_time - start_time >= 3:
            if len(balls) < 15:
                balls.append(create_new_ball())
            else:
                print("Game over! Your score is:", score)
                running = False
            start_time = current_time
        
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
        
        # Move the balls
        for ball in balls:
            ball['x'] += ball['dx']
            ball['y'] += ball['dy']
            
            # Bounce the balls off the walls
            if ball['y'] < 50 or ball['y'] > height - 50:
                ball['dy'] = max(-0.05, min(0.05, -ball['dy']))  
                      
        # Draw the balls
        window.fill(white)
        for ball in balls:
            if ball['number'] != 0:
                draw_ball(ball['number'], ball['x'], ball['y'])
        pygame.display.update()
        
    pygame.quit()

if __name__ == "__main__":
    main()
