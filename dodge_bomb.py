import os
import sys
import pygame as pg
import random
import time
#import cv2

WIDTH, HEIGHT = 1000, 600
IDOU = { #移動量省略
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, +5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT: (+5, 0)
}
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def check_bound(ob_rct:pg.Rect) -> tuple[bool, bool]:
    #画面内判定、画面内ならTrue
    yoko, tate = True, True
    if ob_rct.left < 0 or WIDTH < ob_rct.right: 
        yoko = False
    if ob_rct.top < 0 or HEIGHT < ob_rct.bottom:
        tate = False
    return yoko, tate



def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg")    
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 2.0)
    kk2_img = pg.transform.rotozoom(pg.image.load("fig/2.png"), 0, 2.0)
    kk3_img = pg.transform.rotozoom(pg.image.load("fig/0.png"), 0, 2.0)
    kk4_img = pg.transform.rotozoom(pg.image.load("fig/5.png"), 0, 2.0)
    baku_img = pg.transform.rotozoom(pg.image.load("fig/11.png"), 0, 2.0)
    kk5_img = pg.transform.rotozoom(pg.image.load("fig/6.png"), 0, 2.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400
    bd_img = pg.Surface((20, 20))
    bd_img.set_colorkey((0, 0, 0))
    pg.draw.circle(bd_img, (255, 0, 0), (10, 10), 10)
    bd_rct = bd_img.get_rect()
    bd_rct.center = random.randint(0, WIDTH), random.randint(0, HEIGHT)
    fonto=pg.font.Font(None, 80)
    txt = fonto.render("game over", True, (0, 0, 0))
    vx, vy = +5, +5
    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        #衝突管理 
        #if kk_rct.colliderect(bd_rct):
            #screen.blit(kk2_img,(500, 300))
        
        screen.blit(bg_img, [0, 0]) 

        #mouse_lst=pg.mouse.mouseDragged()
        mouse_lst=pg.mouse.get_pressed()
        #kk_img=[mouseX, mouseY]
        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        for k, v in IDOU.items():
            if key_lst[k]:
               sum_mv[0] += v[0]
               sum_mv[1] += v[1]
        kk_rct.move_ip(sum_mv)
        if check_bound(kk_rct) != (True, True):
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])
        screen.blit(kk_img, kk_rct)
        bd_rct.move_ip(vx, vy)       
        screen.blit(bd_img, bd_rct)
        yoko, tate = check_bound(bd_rct)
        #衝突したときにゲームオーバー表示
        if kk_rct.colliderect(bd_rct):
            screen.blit(txt,[350, 250])
            sikaku=pg.Surface((WIDTH, HEIGHT))
            pg.draw.rect(sikaku,(0, 0, 0), (0, 0, WIDTH, HEIGHT))
            sikaku.set_alpha(170)
            #sikaku.set_colorkey((0, 0, 0))
            screen.blit(sikaku,[0, 0])
            #screen.blit(baku_img,[0, 0])
            pg.display.update()
            time.sleep(5)
            return


            
        if not yoko:  
            vx *= -1
        if not tate:  
            vy *= -1
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
