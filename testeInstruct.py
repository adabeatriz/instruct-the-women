import math
import os
import random
import re
import sys

def automated_readability_index(sentence):
  quant_frase = len(sentence.split(','))
  quant_letra = len(sentence) - len(re.findall(' ', sentence))
  quant_palavra = len((sentence.split(' ')))

  total = math.ceil(((4.71 * (quant_letra/quant_palavra)) + (0.5 * quant_palavra/quant_frase) - 21.43))

  if total >= 1 and total < 14:
    print(total)
  elif total < 1:
    print('1')
  else: 
    print('14')


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    output = automated_readability_index(sentence)

    fptr.write(str(output) + '\n')

    fptr.close()
