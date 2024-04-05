import socket
import pygame
tcp1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_ip = ""         # Any interface
port = 9000        # Arbitrary non-privileged port
buffer_size = 1024
msg = ("Connected...")

tcp1.bind((tcp_ip, port))
tcp1.listen(1)
con, addr = tcp1.accept()
print("TCP Connection from:", addr)
output=""
# Initialize Pygame
pygame.init()
pygame.display.set_mode((300,300))

while True:
    # creating a loop to check events that 
    # are occurring
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # key PRESS
        if event.type == pygame.KEYDOWN:

            # Key "W"- FORWARD
            if event.key == pygame.K_w:
                output='w'
            # Key "A" - LEFT
            if event.key == pygame.K_a:
                output='a'
            # Key "S" - LEFT
            if event.key == pygame.K_s:
                output='s'
            # Key "D" - REVERSE
            if event.key == pygame.K_d:
                output='d'
            # Key "E" - EXIT
            if event.key == pygame.K_e:
                output='exit'
                break
            # Key "E" - EXIT
            if event.key == pygame.K_h:
                output='h'
                break

    con.send(output.encode('utf-8'))

tcp1.close()
