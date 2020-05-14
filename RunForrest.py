'''
Created on Apr 27, 2020

@author: RaghuwanshiS
'''
import ctypes, time

m_event = ctypes.windll.user32.mouse_event
m_event_move = 0x0001
print("!!!!!!!!!!!_____________DISCLAIMER_____________!!!!!!!!!!!")
print("==========================================================")
print("SACHIN RAGHUWANSHI TAKES NO RESPONSIBILITY FOR THIS ACT!!!")
print("==========================================================\n")
print("I KNOW YOU WANNA SNEAK OUT!\n\nWHILE YOU'RE AWAY I'LL HOLD YOUR CASTLE!! :)\n\nWHEN YOU'RE BACK, JUST PRESS 'CTRL+C' TO STOP THE MOUSE.\n")
print("NOW GO... RUN, FORREST, RUN!!!...\n\n")
t1 = time.time()
try:
    while True:
        m_event(m_event_move,25,0,0,0)
        time.sleep(1)
        m_event(m_event_move,0,25,0,0)
        time.sleep(1)
        m_event(m_event_move,-25,0,0,0)
        time.sleep(1)
        m_event(m_event_move,0,-25,0,0)
        time.sleep(1)
except KeyboardInterrupt:
    t2 = time.time()
    print("==========================================================")
    print("WELCOME BACK!!! You Were away for " + str(round(((t2-t1)/60),2)) +" Minutes!"+ "\n\nSHARE ANY FEEDBACK YOU HAVE @ SACHINRAGHU13@GMAIL.COM.")
    print("See Ya Later!! Bye...\n\nThe terminal will auto close.")
    print("==========================================================")
    time.sleep(25)
