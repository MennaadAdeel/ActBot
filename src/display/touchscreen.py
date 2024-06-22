import pygame
import cv2

pygame.init()
screen = pygame.display.set_mode((480, 320))  # Adjust as per your screen resolution
clock = pygame.time.Clock()

#A helper function that handles the video display logi
def display_video(video_path):
    
    #Opens the video file using OpenCV's cv2.VideoCapture
    cap = cv2.VideoCapture(video_path)

    #Reads frames from the video  
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        #converts them from BGR to RGB (as OpenCV uses BGR by default and Pygame uses RGB).
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        #Transpose the frame for correct orientation
        frame = cv2.transpose(frame) 
        
        #Converts the frame to a Pygame surface using pygame.surfarray.make_surface.
        frame = pygame.surfarray.make_surface(frame)
        
        #Displays the frame on the Pygame screen using screen.blit.
        screen.blit(frame, (0, 0))
        
        #Updates the display with pygame.display.update.
        pygame.display.update()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cap.release()
                pygame.quit()
                return

        clock.tick(30)  # Control the frame rate

    cap.release()

# happy video
def display_happy():
    display_video("assets/videos/happy.mp4")  


# sad video
def display_sad():
    display_video("assets/videos/sad.mp4")  


# confused video
def display_confused():
    display_video("assets/videos/confused.mp4")  


# celebrate video
def display_celebrate():
    display_video("assets/videos/celebrate.mp4")  


# talk video
def display_talk():
    display_video("assets/videos/talk.mp4")  
    
