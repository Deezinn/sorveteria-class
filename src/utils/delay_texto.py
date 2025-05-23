import time
import sys

def digitar(texto, delay=0.05):
   for caractere in texto:
      print(caractere, end='', flush=True)
      time.sleep(delay)
   print()

