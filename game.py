#####Sprite Code#####
###Win Screen###
def Win(player):
    Rect(50, 100, 300, 150, fill='lightGreen', opacity=50)
    Rect(50, 100, 300, 150, fill=None, border='green', borderWidth=15)
    Label(player, 200, 150, size=50)
    Label('Wins!', 200, 200, size=50)
###The sky###
app.background = 'skyBlue'
###Hands###
Hand1=Circle(85, 215, 1)#Knight
Hand2=Circle(315, 215, 1)#Roman
###The ground###
Ground = Rect(0, 290, 400, 400, fill='forestGreen')
###Sword1###
Sword1 = Group(Line(92, 200, 122, 140, lineWidth=5, fill='lightGrey'),
    Line(85, 215, 92, 200, lineWidth=5, fill='gold'), 
    Line(85, 197, 99, 203, lineWidth=4, fill='gold'))
###Sword2###
Sword2 = Group(Line(317, 220, 308, 200, lineWidth=5, fill='maroon'), 
    Line(308, 200, 278, 140, fill='darkGrey', lineWidth=5), 
    Arc(308, 200, 15, 15, 90, 180, rotateAngle=-25, fill='grey'), 
    Circle(317, 220, 4, fill='grey'))
###Knight###
Bobby = Group(Line(50, 290, 65, 230),
    Line(65, 230, 70, 290), 
    Line(65,230, 65, 180, lineWidth=2.5),
    Line(65, 180, 85, 215), 
    Line(65, 180, 70, 210),
    Line(70, 210, 85, 215),
    Polygon(52, 180, 52, 140, 74, 140, 78, 160, 78, 180, fill='lightGrey'),
    Line(75, 153, 65, 153, lineWidth=4),
    Line(73, 140, 77, 160, fill='gold'),
    Line(77, 160, 77, 180, fill='gold'), 
    Line(75, 156, 63, 156, fill='gold', lineWidth=3),
    Hand1)
###Roman###
Charlie = Group(Line(350, 290, 335, 230),
    Line(330, 290, 335, 230),
    Line(335, 230, 335, 180, lineWidth=2.5),
    Line(335, 180, 315, 215),
    Line(335, 180, 330, 210),
    Line(330, 210, 315, 215),
    Circle(335, 162, 18, fill='burlyWood'),
    Line(315, 168, 320, 157, fill='burlyWood', lineWidth=5),
    Arc(335, 157, 36, 28, 90, 180, fill='grey', rotateAngle=180),
    Arc(340, 162, 33, 27, 90, 170, fill='grey', rotateAngle=270),
    Circle(335, 157, 7, fill='gold'),
    Line(317, 157, 335, 157, fill='gold'),
    Arc(340, 169, 24, 20, 90, 90, fill='burlyWood'),
    Arc(346, 168, 10, 18, 180, 90, fill='gold'),
    Arc(348, 168, 10, 18, 180, 90, fill='grey'),
    Line(342, 168, 340, 157, fill='gold'),
    Arc(346, 177, 38, 18, 360, 90, fill='grey'), 
    Rect(327, 158, 13, 10, fill='burlyWood'),
    Circle(335, 157, 4, fill='burlyWood'),
    Hand2)
#####Game Code#####
###Movement Code###
###Knight Code###
def onKeyPress(key):
    if key=='d' or key=='D':
        Bobby.centerX+=15
        Sword1.centerX+=15
    if key=='a' or key=='A':
        Bobby.centerX-=15
        Sword1.centerX-=15
    
    ###Roman Code###
    if key=='right':
        Charlie.centerX+=15
        Sword2.centerX+=15
    if key=='left':
        Charlie.centerX-=15
        Sword2.centerX-=15
###Sword Swing###
###Knight Code###
def onKeyHold(keys):
    if 'w' in keys or 'W' in keys:
        Sword1.rotateAngle=-20
        Sword1.centerX=Hand1.centerX+2.5
        Sword1.centerY=Hand1.centerY-42
    if 's' in keys or 'S' in keys:
        Sword1.rotateAngle=+35
        Sword1.centerX=Hand1.centerX+35
        Sword1.centerY=Hand1.centerY-21
        if ((Sword1.hitsShape(Charlie)) and (Sword2.centerY>180)):
            Win('Player1')
            app.stop()
        if ((Sword1.hitsShape(Charlie)) and (Sword2.centerY<180)):
            print('block')
    ###Roman Code###
    if 'up' in keys:
        Sword2.rotateAngle=+20
        Sword2.centerX=Hand2.centerX-2
        Sword2.centerY=Hand2.centerY-39
    if 'down' in keys:
        Sword2.rotateAngle=-35
        Sword2.centerX=Hand2.centerX-35
        Sword2.centerY=Hand2.centerY-19.5
        if ((Sword2.hitsShape(Bobby)) and (Sword1.centerY>175)):
            Win('Player2')
            app.stop()
        if ((Sword2.hitsShape(Bobby)) and (Sword1.centerY<175)):
            print ('block2')
###Reset Sword###
###Knight Code###
def onKeyRelease(key):
    if key=='w'or'W':
        Sword1.rotateAngle=+0
        Sword1.centerX=Hand1.centerX+18.5
        Sword1.centerY=Hand1.centerY-37.5
    if key=='s'or'W':
        Sword1.rotateAngle=+0
        Sword1.centerX=Hand1.centerX+18.5
        Sword1.centerY=Hand1.centerY-37.5
    ###Roman Code###
    if key=='up':
        Sword2.rotateAngle=+0
        Sword2.centerX=Hand2.centerX-17
        Sword2.centerY=Hand2.centerY-34
    if key=='down':
        Sword2.rotateAngle=+0
        Sword2.centerX=Hand2.centerX-17
        Sword2.centerY=Hand2.centerY-34
