'''
    aula sobre praticidade de listas, utilzando um crawler para realizar buscas na internet
        https://www.youtube.com/watch?v=IUkvRa0omX4&t=495s
    arquivo no git:
        https://github.com/cursodepython/modulo-01/tree/master/aula04   '''

import urllib.request

content = urllib.request.urlopen("https://www.melhorcambio.com/dolar-hoje").read()
content= str( content )
find ='<input type="text" value=" '