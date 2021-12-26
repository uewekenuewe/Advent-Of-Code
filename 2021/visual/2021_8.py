import pygame
import pygame.freetype  # Import the freetype module.




def convertCharToNumber(input_str,configuration):
    result = None
    for i in range(0,len(configuration)):
        if configuration[i] == input_str: 
            result = i
    return result

def getValueOfLines(line,configuration):
    result = ''
    for l in line: 
        for c in range(0,len(configuration)): 
            if( len(list(l)) == len(list(configuration[c]))):
                if( len(set(l)&set(configuration[c])) == len(list(l))):
                    result += str(c)
    return result 


# dddd
#e    a
#e    a
# ffff
#g    b
#g    b
# cccc

def asciiNumber(number,poschar):
    result = []
    if number == 9:
        result.append( ' '+4*poschar[0])
        result.append( poschar[1]+'    ' + poschar[2])
        result.append( poschar[1]+'    ' + poschar[2])
        result.append( ' '+4*poschar[3])
        result.append( '     ' + poschar[5])
        result.append( '     ' + poschar[5])
        result.append( ' '+4*poschar[5])    
    if number == 8:
        result.append( ' '+4*poschar[0])
        result.append( poschar[1]+'    ' + poschar[2])
        result.append( poschar[1]+'    ' + poschar[2])
        result.append( ' '+4*poschar[3])
        result.append( poschar[4]+'    ' + poschar[5])
        result.append( poschar[4]+'    ' + poschar[5])
        result.append( ' '+4*poschar[5])

    if number == 7:
        result .append( ' '+4*poschar[0])
        result .append( '    ' + poschar[1])
        result .append( '    ' + poschar[1])
        result .append( '      ')
        result .append( '    ' + poschar[2])
        result .append( '    ' + poschar[2])
        result .append( '     ')

    if number == 6:
        result .append( ' '+4*poschar[0])
        result .append( poschar[1]+'     ')
        result .append( poschar[1]+'     ')
        result .append( ' '+4*poschar[3])
        result .append( poschar[4]+'    ' + poschar[5])
        result .append( poschar[4]+'    ' + poschar[5])
        result .append( ' '+4*poschar[5])    

    if number == 5:
        result .append( ' '+4*poschar[0])
        result .append( poschar[1]+'     ')
        result .append( poschar[1]+'     ')
        result .append( ' '+4*poschar[3])
        result .append( '     ' + poschar[5])
        result .append( '     ' + poschar[5])
        result .append( ' '+4*poschar[5])         

    if number == 4:
        result .append( '      ')
        result .append( poschar[1]+'    ' + poschar[2])
        result .append( poschar[1]+'    ' + poschar[2])
        result .append( ' '+4*poschar[3])
        result .append( '    ' + poschar[5])
        result .append( '    ' + poschar[5])
        result .append( '      ')       

    if number == 3:
        result .append( ' '+4*poschar[0])
        result .append( '     ' + poschar[2])
        result .append( '     ' + poschar[2])
        result .append( ' '+4*poschar[3])
        result .append( '     ' + poschar[5])
        result .append( '     ' + poschar[5])
        result .append( ' '+4*poschar[5]) 

    if number == 2:
        result .append( ' '+4*poschar[0])
        result .append( '     ' + poschar[2])
        result .append( '     ' + poschar[2])
        result .append( ' '+4*poschar[3])
        result .append( poschar[4]+'     ')
        result .append( poschar[4]+'     ')
        result .append( ' '+4*poschar[5])        

    if number == 1:
        result .append( '      ')
        result .append( '    ' + poschar[0])
        result .append( '    ' + poschar[0])
        result .append( '      ')
        result .append( '    ' + poschar[1])
        result .append( '    ' + poschar[1])
        result .append( '      ')

    if number == 0:
        result .append( ' '+4*poschar[0])
        result .append( poschar[1]+'    ' + poschar[2])
        result .append( poschar[1]+'    ' + poschar[2])
        result .append( '      ')
        result .append( poschar[4]+'    ' + poschar[5])
        result .append( poschar[4]+'    ' + poschar[5])
        result .append( ' '+4*poschar[5])        
    return result


def RCIL(input_str,char_list):
    result = input_str
    for k in char_list:
        result = result.replace(k,'')
    return result


pygame.init()
display_x = 1200
display_y = 600
screen = pygame.display.set_mode((display_x, display_y))
GAME_FONT_BOLD = pygame.freetype.Font("SourceCodePro-ExtraBold.ttf", 12)
GAME_FONT_MED = pygame.freetype.Font("SourceCodePro-Medium.ttf", 12)
running =  True

time_elapsed_since_last_action = 0
clock = pygame.time.Clock()

linex = ['acedgfb','cdfbe','gcdfa','fbcad','dab','cefabd','cdfgeb','eafb','cagedb','ab','|','cdfeb', 'fcadb', 'cdfeb', 'cdbaf']

linex = [''.join(sorted(x)) for x in linex]


linex_2 = ['cdfeb', 'fcadb', 'cdfeb', 'cdbaf']

boldIndex = 0

figure_eight = asciiNumber(8,'cefabd')
figure_four = asciiNumber(4,'cefabd')
figure_one = asciiNumber(1,'cefabd')

figure_eight_b = False
figure_one_b = False
figure_four_b = False


figure_eight_X = 40
figure_X = 40

figures = []
result = [None] * 10

step_1 = True
step_2 = False 
step_3 = False 

zero = None 

top            = ''
topLeft        = ''
topRight       = ''
middle         = ''
bottomLeft     = ''
bottomRight    = ''
bottom         = ''


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((15,15,35))
    
    dt = clock.tick() 
    time_elapsed_since_last_action += dt
    # dt is measured in milliseconds, therefore 250 ms = 0.25 seconds
    if time_elapsed_since_last_action > 100:

        if step_1:
            #print(boldIndex,len(linex[boldIndex % len(linex)]),linex[boldIndex % len(linex)])
            if(len(linex[boldIndex % len(linex)]) == 7 and not figure_eight_b):
                figure_eight_b = True 
                figure_X = 40 + (boldIndex % len(linex)) * display_x / len(linex)
                figures.append((figure_X,asciiNumber(8,'cefabd')))
                result[8] = linex[boldIndex % len(linex)]

            if(len(linex[boldIndex % len(linex)]) == 4 and not figure_four_b):
                figure_four_b = True 
                figure_X = 40 + (boldIndex % len(linex)) * display_x / len(linex)
                figures.append((figure_X,asciiNumber(4,'cefabd')))
                result[4] = linex[boldIndex % len(linex)]

            if(len(linex[boldIndex % len(linex)]) == 2):
                figure_one_b = True 
                figure_X = 40 + (boldIndex % len(linex)) * display_x / len(linex)
                figures.append((figure_X,asciiNumber(1,linex[boldIndex % len(linex)])))
                result[1] = linex[boldIndex % len(linex)]

            if(len(linex[boldIndex % len(linex)]) == 3):
                #figure_one_b = True 
                figure_X = 40 + (boldIndex % len(linex)) * display_x / len(linex)
                figures.append((figure_X,asciiNumber(7,linex[boldIndex % len(linex)])))
                result[7] = linex[boldIndex % len(linex)]


        if step_2:
            if(len(linex[boldIndex % len(linex)]) == 6):
                ele = linex[boldIndex % len(linex)]
                numberFound = False
                zero = ele 
                replaced4_ele = RCIL(ele,result[4])
                replaced1_ele = RCIL(ele,result[1])
                if(len(replaced4_ele) == 2):
                    zero = None 
                    #print('found 9:' , ele) 
                    result[9] = ''.join(sorted(ele))
                    figure_X = 40 + (boldIndex % len(linex)) * display_x / len(linex)
                    figures.append((figure_X,asciiNumber(9,linex[boldIndex % len(linex)])))                    
                    numberFound = True
                if(len(replaced1_ele) == 5):
                    #print('found 6:' , ele) 
                    result[6] = ''.join(sorted(ele))
                    figure_X = 40 + (boldIndex % len(linex)) * display_x / len(linex)
                    figures.append((figure_X,asciiNumber(6,linex[boldIndex % len(linex)])))                    
                    numberFound = True
                if not numberFound:
                    result[0] = ele 
                    figure_X = 40 + (boldIndex % len(linex)) * display_x / len(linex)
                    figures.append((figure_X,asciiNumber(0,linex[boldIndex % len(linex)])))  

        if step_3:

            if(''.join(sorted(linex[boldIndex % len(linex)])) == result[3]):
                figure_X = 40 + (boldIndex % len(linex)) * display_x / len(linex)
                figures.append((figure_X,asciiNumber(3,'abcdefg')))  

            if(''.join(sorted(linex[boldIndex % len(linex)])) == result[2]):
                figure_X = 40 + (boldIndex % len(linex)) * display_x / len(linex)
                figures.append((figure_X,asciiNumber(2,'abcdefg'))) 

            if(''.join(sorted(linex[boldIndex % len(linex)])) == result[5]):
                figure_X = 40 + (boldIndex % len(linex)) * display_x / len(linex)
                figures.append((figure_X,asciiNumber(5,'abcdefg'))) 

        if boldIndex == len(linex):
            step_1 = False
            step_2 = True 

        if boldIndex == len(linex)*2:
            step_2 = False 
            step_3 = True  
            top = RCIL(result[7],result[1])
            middle = RCIL(result[8],result[0])
            topRight = RCIL(result[8],result[6])
            bottomLeft = RCIL(result[8],result[9])
            bottom =  RCIL(RCIL(RCIL(result[6],result[4]),bottomLeft),top)
            result[3] = ''.join(sorted(result[7] + middle + bottom ))
            result[2] = ''.join(sorted(top + topRight + middle + bottomLeft + bottom))
            
            topLeft = ''.join(sorted(RCIL(RCIL(result[4],middle),result[1])))
            
            bottomRight = ''.join(sorted(result[4].replace(topLeft,'').replace(topRight,'').replace(middle,'').replace(bottomLeft,'')))
            
            result[5] = ''.join(sorted(top + topLeft + middle + bottomRight + bottom))
            

            #result[5] = ''.join(sorted(top + topLeft + middle + bottomRight + bottom ))
            #result_5 = RCIL(result[+],result[0]) + top + topLeft + middle + bottomRight + bottom
            #result[5] = ''.join(result_5)
            print('xo',result,len(figures))
            print('top:'        ,top            )
            print('topleft:'    ,topLeft        )
            print('topRight'    ,topRight       )
            print('middle'      ,middle         )
            print('bottomLeft'  ,bottomLeft     )
            print('bottomRight' ,bottomRight    )
            print('bottom'      ,bottom         )        
            print(result)

        if boldIndex == len(linex)*3:
            
            step_3 = False  

        boldIndex += 1
        if linex[boldIndex % len(linex)] == '|':
            boldIndex += 1
        time_elapsed_since_last_action = 0 # reset it to 0 so you can count again

    textToRender = ''
    text_X = 40
    for i in range(0,len(linex)):
        if i == (boldIndex % len(linex)):
            GAME_FONT_BOLD.render_to(screen, (text_X, 40), linex[i], (5, 136, 23))
        else:
            GAME_FONT_MED.render_to(screen, (text_X, 40), linex[i], (204, 204, 204))
        text_X += display_x / len(linex)

    if(figure_eight_b or figure_four_b or figure_one_b):
        for k in figures:
            for i in range(0,len(k[1])):
                GAME_FONT_MED.render_to(screen, (k[0], 100+(12*i)), k[1][i], (204, 204, 204))


    pygame.display.flip()

pygame.quit()