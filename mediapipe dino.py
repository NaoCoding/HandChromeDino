import tkinter as tk
import mediapipe as mp
import pyautogui
import threading
import cv2

gui = tk.Tk()
gui.title("Python Mediapipe Chrome Dino")
gui.geometry("800x600")
gui.resizable(0,0)

def Detect_def():
   print("Start Detecting ... ")
   mp_hand = mp.solutions.hands
   mp_drawing = mp.solutions.drawing_utils
   mp_drawing_styles = mp.solutions.drawing_styles

   hands = mp_hand.Hands(
       static_image_mode=False,
       max_num_hands=1,
       min_detection_confidence=0.75,
       min_tracking_confidence=0.75
   )
   cap = cv2.VideoCapture(0)
   while True:
       _ , frame = cap.read()
       frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
       frame = cv2.flip(frame , 1)
       results = hands.process(frame)
       frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

       if results.multi_hand_landmarks:
           for hand_landmarks in results.multi_hand_landmarks:

               mp_drawing.draw_landmarks(
                   frame, hand_landmarks,
                   mp_hand.HAND_CONNECTIONS,
                   mp_drawing_styles.get_default_hand_landmarks_style(),
                   mp_drawing_styles.get_default_hand_connections_style()
               )
               kpos = []
               for i in range(21):
                   x = hand_landmarks.landmark[i].x*frame.shape[1]
                   y = hand_landmarks.landmark[i].y*frame.shape[0]
                   kpos.append((x,y))

                   if kpos[8][1] + 20 > kpos[7][1]:
                       pyautogui.press('space')

                   if kpos[4][1] + 20 > kpos[3][1]:
                       pyautogui.keyDown('down')
                   else:
                       pyautogui.keyUp('down')




       cv2.imshow("OpenCV" , frame)
       if cv2.waitKey(5) == ord('q'):
           break
   cap.release()



def start_detect():
   detect_thread = threading.Thread(target = Detect_def)
   detect_thread.start()

title_frame = tk.Frame(gui)
title_frame.pack()
title = tk.Label(title_frame ,
                text = "Python Chrome Dino\n",
                font = ("Times New Roman" , 36))

title_frame.place(x=200, y=100)
title.pack()

start_frame = tk.Frame()
start_frame.pack()

start = tk.Button(start_frame,
                 text = "Start",
                 font = ("Times New Roman" , 36),
                 bg = "pink",
                 command = start_detect)
start_frame.place(x=450,y=350)
start.pack()

package_frame = tk.Frame()
package_frame.pack()

package = tk.Label(package_frame,
                  text = '  Version and Packages：\n Python 3.9\n Mediapipe \n PyAutoGUI\n OpenCV\n Tkinter',
                  font = ("Times New Roman", 20))

package.pack()
package_frame.place(x=50,y=300)



gui.mainloop()

