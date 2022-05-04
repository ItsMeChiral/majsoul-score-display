import pytesseract
from PIL import Image
import pyautogui
import scipy.stats
import pygame
import time
import keyboard

pygame.init()
white=(255,255,255)
green=(0,255,0)
red=(255,0,0)
uma=[45000,5000,-15000,-35000]
scoreinputdone=0
initialscores=[0,0,0,0]
savelocation=r'c:\users\chiral\desktop\player.jpg'
switchdealerkeybind='1'
keepdealerkeybind='3'
while scoreinputdone==0:
    print('Please enter the starting scores, starting from initial dealer and working clockwise.')
    initialscores[0]=input('Initial Dealer Score : ')
    initialscores[1]=input('Initial Shimocha Score : ')
    initialscores[2]=input('Initial Toimen Score : ')
    initialscores[3]=input('Initial Kamicha Score : ')
    try:
        x=0
        while x<len(initialscores):
            initialscores[x]=float(initialscores[x])
            x=x+1
        scoreinputdone=1
    except:
        print('One of those was not a float number, please try again!')
getstarted=1
  

def threewaytiecheck(a,b,c,d,score,uma):
    if(score[a]==score[b] and score[a]==score[c]):
        scoreswithuma[a]=((uma[a]+uma[b]+uma[c])/3)+score[a]
        scoreswithuma[b]=scoreswithuma[a]
        scoreswithuma[c]=scoreswithuma[a]
        scoreswithuma[d]=uma[d]+score[d]
        global threewaytie
        threewaytie=1

def twowaytiecheck(score,uma):
    x=1
    while x<len(score):
        if score[0]==score[x]:          
            scoreswithuma[0]=((uma[0]+uma[x])/2)+score[0]
            scoreswithuma[x]=scoreswithuma[0]
        x=x+1
    x=2    
    while x<len(score):
        if score[1]==score[x]:              
            scoreswithuma[1]=((uma[1]+uma[x])/2)+score[1]
            scoreswithuma[x]=scoreswithuma[1]
        x=x+1
    if (score[2]==score[3]):
        scoreswithuma[2]=((uma[2]+uma[3])/2)+score[2]
        scoreswithuma[3]=scoreswithuma[2]
            
while getstarted==1:
    umapass=[]
    scoreswithuma=[0,0,0,0]
    rank=[]

    
    global threewaytie
    threewaytie=0
    sumcheck=0
    while sumcheck==0:
        screenshotconfirm=1
        finalscores=[]
        while screenshotconfirm==1:
            try:
                player=pyautogui.screenshot(region=(900,460,130,50))
                player=player.save(savelocation)
                player=pytesseract.image_to_string(savelocation)
                clean=''.join(c for c in player if c.isdigit())
                finalscores.append(int(clean))
                screenshotconfirm=0
            except:
                time.sleep(2)
                screenshotconfirm=1
        screenshotconfirm=1
        
        while screenshotconfirm==1:
            try:
                im1=pyautogui.screenshot(region=(1024,360,50,130))
                shimocha=im1.rotate(270,expand=True)
                shimocha=shimocha.save(savelocation)
                shimocha=pytesseract.image_to_string(savelocation,config='digits')
                clean=''.join(c for c in shimocha if c.isdigit())
                finalscores.append(int(clean))
                screenshotconfirm=0
            except:
                time.sleep(2)
                screenshotconfirm=1
        screenshotconfirm=1
        while screenshotconfirm==1:
            try:
               im1=pyautogui.screenshot(region=(890,340,120,50))
               toimen=im1.rotate(180,expand=True)
               toimen=toimen.save(savelocation)
               toimen=pytesseract.image_to_string(savelocation,config='digits')
               clean=''.join(c for c in toimen if c.isdigit())
               finalscores.append(int(clean))
               screenshotconfirm=0
            except:
               time.sleep(2)
               screenshotconfirm=1
        screenshotconfirm=1
        while screenshotconfirm==1:
            try:
               im1=pyautogui.screenshot(region=(855,360,50,130))
               kamicha=im1.rotate(90,expand=True)
               kamicha=kamicha.save(savelocation)
               kamicha=pytesseract.image_to_string(savelocation,config='digits')
               clean=''.join(c for c in kamicha if c.isdigit())
               finalscores.append(int(clean))
               screenshotconfirm=0
            except:
               time.sleep(2)
               screenshotconfirm=1
        screenshotconfirm=1

        scoresum=sum(finalscores)    
        remainder = scoresum % 1000
        if scoresum>95000 and scoresum<101000 and remainder==0:
            sumcheck=1
        else:
            x=0
            while x<len(finalscores):
                testcheck=scoresum-(2*finalscores[x])
                remainder = testcheck % 1000
                if testcheck>95000 and testcheck<101000 and remainder==0:
                    finalscores[x]=-finalscores[x]
                    sumcheck=1
                    break
                else:
                    x=x+1
            if sumcheck==0:
                x=1
                while x<len(finalscores):
                    testcheck=scoresum-(2*finalscores[x])-(2*finalscores[0])
                    remainder = testcheck % 1000
                    if testcheck>95000 and testcheck<101000 and remainder==0:
                        finalscores[x]=-finalscores[x]
                        finalscores[0]=-finalscores[0]
                        sumcheck=1
                        break
                    else:
                        x=x+1
            if sumcheck==0:
                x=2
                while x<len(finalscores):
                    testcheck=scoresum-(2*finalscores[x])-(2*finalscores[1])
                    remainder = testcheck % 1000
                    if testcheck>95000 and testcheck<101000 and remainder==0:
                        finalscores[x]=-finalscores[x]
                        finalscores[0]=-finalscores[0]
                        sumcheck=1
                        break
                    else:
                        x=x+1
            if sumcheck==0:
                testcheck=scoresum-(2*finalscores[2])-(2*finalscores[3])
                remainder = testcheck % 1000
                if testcheck>95000 and testcheck<101000 and remainder==0:
                    
                        finalscores[2]=-finalscores[2]
                        finalscores[3]=-finalscores[3]
                        sumcheck=1
                
                
        
        

    rank=scipy.stats.rankdata(finalscores,method='ordinal')
    x=0
    while x<len(rank):
        rank[x]=5-rank[x]
        umapass.append(uma[rank[x]-1])
        x=x+1
    x=0
    while x<len(umapass):
        scoreswithuma[x]=umapass[x]+finalscores[x]
        x=x+1
    if finalscores[0]==finalscores[1] and finalscores[0]==finalscores[2] and finalscores[0]==finalscores[3]:
        scoreswithuma=(finalscores)
    else:
        threewaytiecheck(0,1,2,3,finalscores,umapass)
        threewaytiecheck(1,2,3,0,finalscores,umapass)
        threewaytiecheck(0,1,3,2,finalscores,umapass)
        threewaytiecheck(0,2,3,1,finalscores,umapass)
        if(threewaytie==0):
            twowaytiecheck(finalscores,umapass)

    newscorepredictions=[0,0,0,0]
    x=0
    while x<len(newscorepredictions):
        newscorepredictions[x]=round((scoreswithuma[x]/1000)-25,1)+initialscores[x]
        x=x+1
    scoresranked=scipy.stats.rankdata(newscorepredictions,method='max')        
    scoredisplay=pygame.display.set_mode((400,1000))
    pygame.display.set_caption('Scores!')
    scoredisplay.fill(white)

    font=pygame.font.Font('C:\Windows\Fonts\consolab.ttf',64)
    x=0
    y=50
    while x<len(scoreswithuma):
        score=round((scoreswithuma[x]/1000)-25,1)
        if(score>0):
            score='+'+str(score)
            text=font.render(score,True,green,white)
        else:
            if(score<0):
                text=font.render(str(score),True,red,white)
            else:
                text=font.render(str(score),True,(132,71,5),white)
        if x==1:
            text=pygame.transform.rotate(text,2)
        if x==3:
            text=pygame.transform.rotate(text,-2)
        textRect=text.get_rect()
        textRect.center = (200,y)
        scoredisplay.blit(text,textRect)
        x=x+1
        y=y+80
    x=0
    while x<len(finalscores):
        
        text=font.render(str(finalscores[x]),True,(249,166,2),white)
        if x==1:
            text=pygame.transform.rotate(text,1)
        if x==3:
            text=pygame.transform.rotate(text,-3)
        textRect=text.get_rect()
        textRect.center = (200,y)
        scoredisplay.blit(text,textRect)
        x=x+1
        y=y+80
    x=0
    while x<len(initialscores):
        score=round((scoreswithuma[x]/1000)-25,1)
        if(scoresranked[x]==4):
            text=font.render(str(round(newscorepredictions[x],1)),True,(255,215,0),white)
        else:
            if(scoresranked[x]==3):
                text=font.render(str(round(newscorepredictions[x],1)),True,(170,169,173),white)
            else:
                if(scoresranked[x]==2):
                    text=font.render(str(round(newscorepredictions[x],1)),True,(190,108,0),white)
                else:
                    text=font.render(str(round(newscorepredictions[x],1)),True,(254,111,94),white)
        textRect=text.get_rect()
        textRect.center = (200,y)
        scoredisplay.blit(text,textRect)
        x=x+1
        y=y+80
        
    
        
    pygame.display.update()
    time.sleep(4)
    while 1==1:
        pygame.event.pump()
        if(keyboard.read_key()==switchdealerkeybind):
            pyautogui.click(1771,327)
            time.sleep(0.3)
            pyautogui.click(1715,470)
            blah=[0,0,0,0]
            blah[0]=initialscores[1]
            blah[1]=initialscores[2]
            blah[2]=initialscores[3]
            blah[3]=initialscores[0]
            initialscores=blah
            break
        if(keyboard.read_key()==keepdealerkeybind):
            break
            

