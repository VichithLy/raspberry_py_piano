import pygame
import sys
from tkinter import *

pygame.init()
#FUNCTIONS TO PLAY THE RIGHT SOUND FOR EACH TILES
def tiles_Cs():
        sound = pygame.mixer.Sound("./sounds/C_s.wav")        
        sound.play()
        return
def tiles_Ds():
        sound = pygame.mixer.Sound("./sounds/D_s.wav")
        sound.play()
        return
def tiles_Fs():
        sound = pygame.mixer.Sound("./sounds/F_s.wav")        
        sound.play()
        return
def tiles_Gs():
        sound = pygame.mixer.Sound("./sounds/G_s.wav")
        sound.play()
        return
def tiles_Bb():
        sound = pygame.mixer.Sound("./sounds/Bb.wav")        
        sound.play()
        return
def tiles_Cs1():
        sound = pygame.mixer.Sound("./sounds/C_s1.wav")
        sound.play()
        return
def tiles_Ds1():
        sound = pygame.mixer.Sound("./sounds/D_s1.wav")
        sound.play()
        return
def tiles_C():
        sound = pygame.mixer.Sound("./sounds/C.wav")
        sound.play()
        return
def tiles_D():
        sound = pygame.mixer.Sound("./sounds/D.wav")
        sound.play()
        return
def tiles_E():
        sound = pygame.mixer.Sound("./sounds/E.wav")
        sound.play()
        return
def tiles_F():
        sound = pygame.mixer.Sound("./sounds/F.wav")
        sound.play()
        return
def tiles_G():
        sound = pygame.mixer.Sound("./sounds/G.wav")
        sound.play()
        return
def tiles_A():
        sound = pygame.mixer.Sound("./sounds/A.wav")
        sound.play()
        return
def tiles_B():
        sound = pygame.mixer.Sound("./sounds/B.wav")
        sound.play()
        return
def tiles_C1 ():
        sound = pygame.mixer.Sound("./sounds/C1.wav")
        sound.play()
        return
def tiles_D1 ():
        sound = pygame.mixer.Sound("./sounds/D1.wav")
        sound.play()
        return
def tiles_E1 ():
        sound = pygame.mixer.Sound("./sounds/E1.wav")
        sound.play()
        return
def tiles_F1 ():
        sound = pygame.mixer.Sound("./sounds/F1.wav")
        sound.play()
        return

#INTERFACE PART
program = Tk()
frame = Frame(program)
frame.pack()
program.title("Piano")
blackTilesFrame = Frame(program)
blackTilesFrame.pack(side = TOP)

blackTiles1= Button(blackTilesFrame,padx=8,height = 7,pady=8,
bd=8, text="C#", bg="black",fg="white",command=tiles_Cs)
blackTiles1.pack(side=LEFT)

spaceTiles= Button(blackTilesFrame,state=DISABLED,
height=7,width=1,padx=0,pady=0,relief=RIDGE)
spaceTiles.pack(side=LEFT)

blackTiles2= Button(blackTilesFrame,padx=8,height = 7,
pady=8, bd=8, text="D#", bg="black",fg="white",command=tiles_Ds)
blackTiles2.pack(side=LEFT)

spaceTiles= Button(blackTilesFrame,state=DISABLED,
height=7,width=6,padx=0,pady=0,relief=RIDGE)
spaceTiles.pack(side=LEFT)

blackTiles3= Button(blackTilesFrame,padx=8,height = 7,
pady=8, bd=8, text="F#", bg="black",fg="white",command=tiles_Fs)
blackTiles3.pack(side=LEFT)

spaceTiles= Button(blackTilesFrame,state=DISABLED,
height=7,width=1,padx=0,pady=0,relief=RIDGE)
spaceTiles.pack(side=LEFT)

blackTiles4= Button(blackTilesFrame,padx=8,
height = 7,pady=8, bd=8, text="G#", bg="black",fg="white",command=tiles_Gs)
blackTiles4.pack(side=LEFT)

spaceTiles= Button(blackTilesFrame,state=DISABLED,height=7,width=1,padx=0,pady=0,relief=RIDGE)
spaceTiles.pack(side=LEFT)

blackTiles2= Button(blackTilesFrame,padx=8,height = 7,pady=8, bd=8, text="Bb", bg="black",fg="white",command=tiles_Bb)
blackTiles2.pack(side=LEFT)

spaceTiles= Button(blackTilesFrame,state=DISABLED,height=7,width=6,padx=0,pady=0,relief=RIDGE)
spaceTiles.pack(side=LEFT)

blackTiles3= Button(blackTilesFrame,padx=8,height = 7,pady=8, bd=8, text="C#1", bg="black",fg="white",command=tiles_Cs1)
blackTiles3.pack(side=LEFT)

spaceTiles= Button(blackTilesFrame,state=DISABLED,height=7,width=1,padx=0,pady=0,relief=RIDGE)
spaceTiles.pack(side=LEFT)

blackTiles4= Button(blackTilesFrame,padx=8,height = 7,pady=8, bd=8, text="D#1", bg="black",fg="white",command=tiles_Ds1)
blackTiles4.pack(side=LEFT)

spaceTiles= Button(blackTilesFrame,state=DISABLED,height=7,width=8,padx=0,pady=0,relief=RIDGE)
spaceTiles.pack(side=LEFT)

whiteTilesFrame = Frame(program)
whiteTilesFrame.pack(side=TOP)

whiteTiles1=Button(whiteTilesFrame,padx=16,pady=16,bd=8,height=8,text="C",fg="black",command=tiles_C)
whiteTiles1.pack(side=LEFT)
whiteTiles2=Button(whiteTilesFrame,padx=16,pady=16,bd=8,height=8,text="D",fg="black",command=tiles_D)
whiteTiles2.pack(side=LEFT)
whiteTiles3=Button(whiteTilesFrame,padx=16,pady=16,bd=8,height=8,text="E",fg="black",command=tiles_E)
whiteTiles3.pack(side=LEFT)
whiteTiles4=Button(whiteTilesFrame,padx=16,pady=16,bd=8,height=8,text="F",fg="black",command=tiles_F)
whiteTiles4.pack(side=LEFT)
whiteTiles5=Button(whiteTilesFrame,padx=16,pady=16,bd=8,height=8,text="G",fg="black",command=tiles_G)
whiteTiles5.pack(side=LEFT)
whiteTiles6=Button(whiteTilesFrame,padx=16,pady=16,bd=8,height=8,text="A",fg="black",command=tiles_A)
whiteTiles6.pack(side=LEFT)
whiteTiles7=Button(whiteTilesFrame,padx=16,pady=16,bd=8,height=8,text="B",fg="black",command=tiles_B)
whiteTiles7.pack(side=LEFT)
whiteTiles8=Button(whiteTilesFrame,padx=16,pady=16,bd=8,height=8,text="C1",fg="black",command=tiles_C1)
whiteTiles8.pack(side=LEFT)
whiteTiles9=Button(whiteTilesFrame,padx=16,pady=16,bd=8,height=8,text="D1",fg="black",command=tiles_D1)
whiteTiles9.pack(side=LEFT)
whiteTiles10=Button(whiteTilesFrame,padx=16,pady=16,bd=8,height=8,text="E1",fg="black",command=tiles_E1)
whiteTiles10.pack(side=LEFT)
whiteTiles11=Button(whiteTilesFrame,padx=16,pady=16,bd=8,height=8,text="F1",fg="black",command=tiles_F1)
whiteTiles11.pack(side=LEFT)

program.mainloop()
