import random
import curses

try:
    s = curses.initscr() #inicializar a tela, 
    curses.curs_set(0)
    #sh, sw =s.getmaxyx()
    #print(f'tamanaho maximo horizontal {sw} tamanaho maximo vertical {sh} ')

except:
    print("An exception occurred")
exit()    
# print("cheguei até aqui!!")
