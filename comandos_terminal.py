import os
#os.system ("ls -l") funcionou
#os.system ("cd ..")
import subprocess as sbp
'''test = subprocess.Popen(["ping","-W","2","-c", "1", "192.168.1.70"], stdout=subprocess.PIPE)
output = test.communicate()[0]
'''
#from subprocess import call
'''
	sbp.call(["ls", "-l"]) funciona
	abc = a.c
	call(["vim", abc])'''
#sbp.call(["ls", "-l"])
'''	a = "ping"
	b = "8.8.8.8"
'''
a = "cd"
b = ".."

sbp.call([a, b])
