import cv2
import numpy as np
global xxx
global yyy
global motions
global m
motions=None
m=0
xxx=640-1
yyy=480-1
sets=0

def find_blue_cursor_position(frame):
    global xxx
    global yyy
    global motions
    global m
    if m==0:
        motions=frame
    for yy in range(480):
       
            
        for xx in range(640):
            
            blue_channel1,green_channel1,red_channel1=motions[yy,xx]
            blue_channel,green_channel,red_channel=frame[yy,xx]
            if blue_channel>blue_channel1:
                b=blue_channel-blue_channel1
            else:
                b=blue_channel1-blue_channel
            if red_channel>red_channel1:

                r=red_channel-red_channel1
            else:
                r=red_channel1-red_channel
            if green_channel>green_channel1:
                g=green_channel-green_channel1
            else:
                g=green_channel1-green_channel
            if b>60 or g>60 or r>60 :
                m=1
                motions==frame
                return (xx, yy)
            
    m=1        
    return None
            

def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Espelhar a imagem
        frame = cv2.flip(frame, 1)
       
        # Procurar a posição do cursor azul
        position = find_blue_cursor_position(frame)

        # Desenhar o cursor virtual (bola vermelha) se a posição foi encontrada
        if position is not None:
            cv2.circle(frame, position, 10, (0, 0, 255), -1)

        # Mostrar a imagem
        cv2.imshow('Augmented Reality - Blue Cursor Detection', frame)

        # Sair ao pressionar a tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
