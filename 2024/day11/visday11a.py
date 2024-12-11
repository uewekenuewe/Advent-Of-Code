from raylibpy import *
import re
import sys
import numpy as np
import copy 

ans1 = 0
ans2 = 0

if len(sys.argv) > 1:
    filename = sys.argv[1]
    f = open(sys.argv[1], "r")
else:
    f = open("10", "r")

ends = []
lines = [l.strip() for l in f.readlines()]
m = []
mcpy = []
height,width = 0,0
for l in lines:
    height += 1
    m.append([int(x) for x in l])
    width = len(l)
    mcpy.append(["." for _ in l])

starts = []
for i in range(len(m)):
    for k in range(len(m[i])):
        if m[i][k] == 0:
            starts.append((i,k))
        if m[i][k] == 9:
            ends.append((i,k))

dd = [(-1,0),(1,0),(0,-1),(0,1)]
def part1():
    ans1arr = []
    for s in starts:
        mtemp = copy.deepcopy(mcpy)
        sx,sy = s 
        v = []
        q = [s]
        arr1temp = []
        i = 0
        while(len(q) > 0):
            x,y = q.pop()
            mtemp[x][y] = m[x][y]
            v.append((x,y))
            if i != 0 and m[x][y] == 0:
                continue
            else:
                for d in dd:
                    dx,dy = d
                    dx += x
                    dy += y 
                    if 0<= dx < len(m) and 0<=dy  < len(m):
                        if m[dx][dy] != 0:
                            if (m[dx][dy] - m[x][y]) == 1 and (dx,dy) not in v:
                                q.append((dx,dy))
                                if m[dx][dy] == 9 and m[x][y] == 8:
                                    ans1arr.append((dx,dy,x,y))
        anstemp = 0
        for x in mtemp:
            anstemp += x.count(9)
        ans1+=anstemp

def part2():
    ans2arr = []
    for s in starts:
        mtemp = copy.deepcopy(mcpy)
        sx,sy = s 
        sans = 0
        for e in ends:
            v = []
            q = [s]
            arr2temp = []
            i = 0
            while(len(q) > 0):
                x,y = q.pop()
                mtemp[x][y] = m[x][y]
                v.append((x,y))
                if i != 0 and m[x][y] == 0:
                    continue
                if (x,y) == e:
                    sans += 1
                else:
                    for d in dd:
                        dx,dy = d
                        dx += x
                        dy += y 
                        if 0<= dx < len(m) and 0<=dy  < len(m):
                            if m[dx][dy] != 0:
                                if (m[dx][dy] - m[x][y]) == 1 and (dx,dy) not in v:
                                    q.insert(0,(dx,dy))
        ans2+=sans






factor = 30
mcolor = {}
def initColor():
    for i in range(len(m)):
        for k in range(len(m[i])):
            mcolor[(i,k)] = LIGHTGRAY

def setColor(p,color):
    xx,yy = p
    if m[xx][yy] == 0:
        mcolor[(xx,yy)] = RED
        return
    if m[xx][yy] == 9:
        mcolor[(xx,yy)] = BLACK
        return

    mcolor[(xx,yy)]= color
    return

map_lines = []

def main():

    width = len(m)
    height = len(m[0])
    init_window(10+ (width*factor) , (height+3)*factor, "AOC - DAY10")

    set_target_fps(120)

    while not window_should_close():
        ans1arr = []
        anstemp = 0
        mtemp = copy.deepcopy(mcpy)
        initColor()
        for s in starts:
            map_lines = []
            for x in mtemp:
                anstemp += x.count(9)
            mtemp = copy.deepcopy(mcpy)
            v = []
            q = [s]
            i = 0
            while(len(q) > 0):
                x,y = q.pop()
                mtemp[x][y] = m[x][y]
                v.append((x,y))

                setColor((x,y),GREEN)

                begin_drawing()
                drawFrame(anstemp)
                end_drawing()

                if i != 0 and m[x][y] == 0:
                    continue
                else:
                    for d in dd:
                        dx,dy = d
                        dx += x
                        dy += y 
                        if 0<= dx < len(m) and 0<=dy  < len(m):
                            if m[dx][dy] != 0:
                                if (m[dx][dy] - m[x][y]) == 1 and (dx,dy) not in v:
                                    q.append((dx,dy))
                                    map_lines.append((x,y,dx,dy))
                                    if m[dx][dy] == 9 and m[x][y] == 8:
                                        ans1arr.append((dx,dy,x,y))



    close_window()

def drawFrame(x):
        clear_background(RAYWHITE)
        for i in range(len(m)):
            for k in range(len(m[i])):
                draw_text(str(m[i][k]), i*factor, k*factor, factor, mcolor[(i,k)])
        draw_text("ANS1 : " + str(x), 0, factor *  (height+1), factor, RED)
        for l in map_lines:
            x,y,dx,dy = l
            draw_line(x*factor,y*factor,dx*factor,dy*factor,BLACK)
 
if __name__ == '__main__':
    main()
