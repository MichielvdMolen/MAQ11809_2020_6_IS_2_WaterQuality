from jupylet.sprite import Sprite
from jupylet.label import Label
from jupylet.app import App

app = App()

# The x and y components of the spaceship's velocity.
vx = 0
vy = 0

# The objects.
ship         = Sprite('images/ship1.png',  x=app.width/2,  y=app.height/2,  scale=0.5, angle = -45)
stars        = Sprite('images/stars.png',  scale=2.5)
alien        = Sprite('images/marvin.png', scale=0.1)
nemo         = Sprite('images/nemo.jpeg',  scale=0.8, x=app.height/2, y=app.height/2)
lauwersmeer  = Sprite('images/Lauwersmeer.jpeg', scale=0.4, x=app.height/2, y=app.height/2)
lauwersmeerc = Sprite('images/Lauwersmeer_karta.jpeg', scale=0.8, x=app.height/2, y=app.height/1)
wadden       = Sprite('images/wadden.jpeg', scale=0.8, x=app.height/2, y=app.height/2)
waddenc      = Sprite('images/wadden_karta.jpeg', scale=0.2, x=app.height/1.5, y=app.height/1)
rotterdam    = Sprite('images/rotterdam.jpeg', scale=1.0, x=app.height/2, y=app.height/2)
rotterdamc   = Sprite('images/rotterdam_karta.jpeg', scale=0.5, x=app.height/1.1, y=app.height/1.1)
zeeland      = Sprite('images/zeeland.jpeg', scale=1.2, x=app.height/2, y=app.height/2)
zeelandc     = Sprite('images/zeeland_karta.jpeg', scale=0.6, x=app.height/1.1, y=app.height/1.1)
rajareef     = Sprite('images/rajareef.jpeg', scale=0.4, x=app.height/1.1, y=app.height/1.1)
rainbowreef  = Sprite('images/rainbowreef.jpeg', scale=0.6, x=app.height/1.1, y=app.height/1.1)
coralreef    = Sprite('images/coralreef.jpeg', scale=0.7, x=app.height/1.1, y=app.height/1.1)
nemomarvin   = Sprite('images/nemomarvin.png', scale=0.2, x=app.height/1.5, y=app.height/1.5)
bucket       = Sprite('images/bucket.png', scale=0.5, x=app.height/1.1, y=app.height/1.1)

draw_alien = False
draw_stars = False
draw_nemo  = False
draw_lauwersmeer  = False
draw_lauwersmeerc = False 
draw_wadden  = False
draw_waddenc = False 
draw_rotterdam  = False
draw_rotterdamc = False 
draw_zeeland  = False
draw_zeelandc = False 
draw_rajareef = False 
draw_rainbowreef = False 
draw_coralreef = False 
draw_nemomarvin = False 
draw_bucket = False 


# The x and y components of the spaceship's velocity.
vx = 0
vy = 0

# Current pressed state of the arrow keys.
up    = False
left  = False
right = False

@app.run_me_every(1/60)
def update_ship(ct, dt):
    global vx, vy

    if left:
        ship.angle += 150 * dt
        
    if right:
        ship.angle -= 120 * dt
        
    if up:
        vx += 3 * math.cos(math.radians(90 + ship.angle))
        vy += 3 * math.sin(math.radians(90 + ship.angle))

    #
    # Update ship position according to its velocity.
    #
    ship.x += vx * dt
    ship.y += vy * dt

    ship.wrap_position(app.width, app.height)
    

@app.run_me_every(1/60)
def rotate(ct, dt):
    
    alien.angle += 64 * dt

@app.event
def mouse_position_event(x, y, dx, dy):
    
    alien.x = x
    alien.y = y
    
@app.event
def render(ct, dt):
    
    app.window.clear()

    if draw_stars:
        stars.draw()    
    if draw_nemo:
        nemo.draw()
    if draw_lauwersmeer:
        lauwersmeer.draw() 
    if draw_lauwersmeerc:
        lauwersmeerc.draw()
    if draw_wadden:
        wadden.draw() 
    if draw_waddenc:
        waddenc.draw() 
    if draw_rotterdam:
        rotterdam.draw() 
    if draw_rotterdamc:
        rotterdamc.draw() 
    if draw_zeeland:
        zeeland.draw() 
    if draw_zeelandc:
        zeelandc.draw()
    if draw_rajareef:
        rajareef.draw()      
    if draw_rainbowreef:
        rainbowreef.draw()   
    if draw_coralreef:
        coralreef.draw()     
    if draw_bucket:
        bucket.draw()            
        nemomarvin.draw()
    if draw_alien:
        alien.draw()
        
def set_nemo():
    global draw_stars, draw_alien, left, right, up, draw_nemo

    left       = False
    right      = False
    draw_stars = False
    draw_alien = False
    draw_nemo  = True

def set_lauwersmeer():
    global draw_stars, draw_alien, left, right, up, draw_nemo, draw_lauwersmeer, draw_lauwersmeerc

    left       = False
    right      = False
    draw_stars = False
    draw_alien = True
    draw_nemo  = False
    draw_lauwersmeer  = True
    draw_lauwersmeerc = True
    
    lauwersmeer.x, lauwersmeer.y = app.width/2, app.height/2
    lauwersmeerc.x, lauwersmeerc.y = app.width/1, app.height/1
    
def set_wadden():
    global draw_stars, draw_alien, left, right, up, draw_nemo, draw_wadden, draw_waddenc

    left       = False
    right      = False
    draw_stars = False
    draw_alien = True
    draw_nemo  = False
    draw_wadden  = True
    draw_waddenc = True

    wadden.x, wadden.y = app.width/2, app.height/2
    waddenc.x, waddenc.y = app.width/1.0, app.height/1.2
    
def set_rotterdam():
    global draw_stars, draw_alien, left, right, up, draw_nemo, draw_rotterdam, draw_rotterdamc

    left       = False
    right      = False
    draw_stars = False
    draw_alien = True
    draw_nemo  = False 
    draw_rotterdam  = True
    draw_rotterdamc = True
    
    rotterdam.x, rotterdam.y = app.width/2, app.height/2
    rotterdamc.x, rotterdamc.y = app.width/1.1, app.height/1.1
    
def set_zeeland():
    global draw_stars, draw_alien, left, right, up, draw_nemo, draw_zeeland, draw_zeelandc

    left       = False
    right      = False
    draw_stars = False
    draw_alien = True
    draw_nemo  = False 
    draw_zeeland  = True
    draw_zeelandc = True
    
    zeeland.x, zeeland.y = app.width/2, app.height/2
    zeelandc.x, zeelandc.y = app.width/1.1, app.height/1.1    
    
def set_IS201():
    global draw_stars, draw_alien, left, right, up, draw_nemo, draw_rajareef

    left       = False
    right      = False
    draw_stars = False
    draw_alien = True
    draw_nemo  = False 
    draw_rajareef = True
    
    rajareef.x, rajareef.y = app.width/2, app.height/2     

    
def set_IS202():
    global draw_stars, draw_alien, left, right, up, draw_nemo, draw_rainbowreef

    left       = False
    right      = False
    draw_stars = False
    draw_alien = True
    draw_nemo  = False 
    draw_rainbowreef = True
    
    rainbowreef.x, rainbowreef.y = app.width/2, app.height/2     

def set_IS203():
    global draw_stars, draw_alien, left, right, up, draw_nemo, draw_coralreef

    left       = False
    right      = False
    draw_stars = False
    draw_alien = True
    draw_nemo  = False 
    draw_coralreef = True
    
    coralreef.x, coralreef.y = app.width/2, app.height/2     

def set_IS204():
    global draw_stars, draw_alien, left, right, up, draw_nemo, draw_bucket, draw_nemomarvin

    left       = False
    right      = False
    draw_stars = False
    draw_alien = False
    draw_nemo  = False 
    draw_bucket = True
    draw_nemomarvin = True
    
    bucket.x, bucket.y = app.width/2, app.height/2     
    nemomarvin.x, nemomarvin.y = app.width/1.5, app.height/1.5     

    
def check_my_answer_nemo(x, y, z):
    if x == 'does not' and y == 'do' and z == 'winter':
        print('Hoera! Your answer is correct! Are you ready to go fishing with me? We need to find Nemo!')
        set_nemo()
        return True
    else:
        print('Your answer is not correct. Please, try again!')
        if x != 'does not'          : print('x is incorrect')
        if y != 'do'                : print('y is incorrect')
        if z != 'winter'            : print('z is incorrect')  
        return False

def check_my_answer_lauwersmeer(x, y1, y2, z):
#   if x == 'do' and y1 == 'constant' and y2 == 'precipitation' and z == ('2014/2015', '2015/2016', '2017/2018', '2019/2020'):
    if x == 'do' and y1 == 'constant' and y2 == 'precipitation' and '2014/2015' in z and '2015/2016' in z and '2017/2018' in z and '2019/2020' in z:
        print('Hoera! Your answer is correct! Do you think Nemo is in Lauwersmeer? No, Lauwersmeer is popular for record-size pikes and zanders.')
        set_lauwersmeer()
        return True
    else:
        print('Your answer is not correct. Please, try again!')
        if x  != 'do'                : print('x  is incorrect')
        if y1 != 'constant'          : print('y1 is incorrect')
        if y2 != 'precipitation'     : print('y2 is incorrect')
        if z != ('2014/2015', '2015/2016', '2017/2018', '2019/2020'): 
            print('z is incorrect')    
            if '2014/2015' in z          : print('   but 2014/2015 is correct')   
            if '2015/2016' in z          : print('   but 2015/2016 is correct')
            if '2017/2018' in z          : print('   but 2017/2018 is correct')
            if '2019/2020' in z          : print('   but 2019/2020 is correct')    
        return False 
    
def check_my_answer_wadden(x, y, z, u1, u2):
    if x == 'more' and y == ('a','b','c') and z == 'less' and u1 == '2018/2019' and u2 == 'Makkink':
        print('Hoera! Your answer is correct! Let us search further for my Nemo around the Wadden sea islands! Ah, he is also not there. In Wadden you can only find sea bass.')
        set_wadden()
        return True
    else:
        print('Your answer is not correct. Please, try again!')
        if x  != 'more'          : print('x  is incorrect')
        if y!= ('a','b','c')     : 
            print('y  is incorrect')
            if 'a' in y              : print('   but a  is correct') 
            if 'b' in y              : print('   but b  is correct') 
            if 'c' in y              : print('   but c  is correct')     
        if z  != 'less'          : print('z  is incorrect')
        if u1 != '2018/2019'     : print('u1 is incorrect, write something like \'2000/2001\'. ')
        if u2 != 'Makkink'       : print('u2 is incorrect')    
        return False

def check_my_answer_rotterdam(x, y):
    dy = 200
    if x == 'last' and 500-dy <= y <= 500+dy:
        print('Hoera! Your answer is correct! Do you think Nemo might be in Rotterdam fishing area? I don not think so. Rotterdam is a great seabass angling spot.')
        set_rotterdam()
        return True
    else:
        print('Your answer is not correct. Please, try again!')
        if x  != 'last'              : print('x  is incorrect')
        if y<500-dy  or y>500+dy     : print('y  is incorrect')
        return False   
    
def check_my_answer_zeeland(x1, x2, y, z):
    if x1 == 'is' and x2 == 2 and y == 'is not' and z >= 2:
        print('Hoera! Your answer is correct! But, still no Nemo. Zeeland currently is a fantastic varied area for sea anglers, not clown fishes. Do you think we will find him in Integration skills 2?')
        set_zeeland()
        return True
    else:
        print('Your answer is not correct. Please, try again!')
        if x1 != 'is'              : print('x1 is incorrect')
        if x2 != 2                 : print('x2 is incorrect')
        if y  != 'is not'          : print('y2 is incorrect')
        if z<2                     : print('z  is incorrect')    
        return False    
    
def check_my_answer_IS201(x,y):
    if x == 'has' and y == 'maximum':
        print('Hoera! Your answer is correct! Hope you did not forget we still need to find Nemo! Let us start in Fiji, at the Raja reef. Do you think he is there? No, he is not, but a biodiversity here includes  dugongs, manta rays, sharks, and turtles.')
        set_IS201()
        return True
    else:
        print('Your answer is not correct. Please, try again!')
        if x  != 'has'              : print('y  is incorrect')
        if y  != 'maximum'          : print('y  is incorrect')
        return False
    
    
def check_my_answer_IS202(x,y):
    dy = 900000
    if     x == 'increase' and 3500000 - dy <= y <= 3500000 + dy:
        print('Hoera! Your answer is correct! At rainbowreef in Fiji, I see swarms of anthias hanging in the current, but again no Nemo.')
        set_IS202()
        return True
    else:
        print('Your answer is not correct. Please, try again!')
        if x  != 'increase'                :  print('y  is incorrect')
        if y < 3500000-dy or y>3500000 + dy:  print('z  is incorrect')
        return False

    
def check_my_answer_IS203(x,y,z):
    if x  == 'more' and y  == 'Fall'  and z  == 'Spring':
        print('Hoera! Your answer is correct! The Great Barrier reef is probably the most famous coral reef in the world. It can (partly) thank for its popularity to Nemo. Globally, there are over 28 species of the clown fish, with its bright orange colouring and distinctive white band with black outline, is the most easy to identify. They live amongst the poisonous tentacles of the fish-eating anemone, which they become immune to, by coating themselves with a layer of mucus. How do they do this? By gently letting the tentacles touch their body in various different places, they establish immunity and the mucus covering. Once safe, they enter the anemone and take up residence. Interesting anemone fish facts: they are able to change sex during their lifetime & the males care for the nest and eggs until they hatch. But unfortunately our Nemo is still not here.')
        set_IS203()
        return True
    else:
        print('Your answer is not correct. Please, try again!')
        if x  != 'more'                :  print('x  is incorrect')
        if y  != 'Fall'                :  print('y  is incorrect')
        if z  != 'Spring'              :  print('z  is incorrect')
        return False
    
def check_my_answer_IS204(x,y):
     if x == 'inversely proportional' and y == 'd':
        print('Hoera! Your answer is correct! Look who is here!!! Can you guess what sort of fishes he swims with?')
        set_IS204()
        return True
     else:
        print('Your answer is not correct. Please, try again!')
        if x  != 'inversely proportional'                :  print('x  is incorrect')
        if y  != 'd':
            print('y  is incorrect')
            if 'd' in y: print('    but \'d\' is correct')
        return False
        