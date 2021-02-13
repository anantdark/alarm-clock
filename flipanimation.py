import time
man1 =r'''
   o/
   |
__/|________
'''
man2 =r'''
   o/
 __|
___|________
'''
man3 =r'''
   o__
 \/
__|_________
'''
man4 =r'''

\ __o
_|__\_______
'''
man5 =r'''
  /
 / \o
____\_______
'''
man6 = r'''
__ __
  |o
__|_________
'''
man7 = r'''
   \
   /\
__|o________
'''
man8 = r'''

   __|
__/o_|______
'''
man9 = r'''
   |
  o\ /
____|_______
'''
man10 = r'''
  o/
  |__
__|_________
'''
tval ='''
┏━━━┓ ┏━┓ ┏┓ ┏━━━┓ ┏━┓ ┏┓ ┏━━━━┓
┃┏━┓┃ ┃ ┗┓┃┃ ┃┏━┓┃ ┃ ┗┓┃┃ ┃┏┓┏┓┃
┃┃ ┃┃ ┃┏┓┗┛┃ ┃┃ ┃┃ ┃┏┓┗┛┃ ┗┛┃┃┗┛
┃┗━┛┃ ┃┃┗┓ ┃ ┃┗━┛┃ ┃┃┗┓ ┃   ┃┃
┃┏━┓┃ ┃┃ ┃ ┃ ┃┏━┓┃ ┃┃ ┃ ┃  ┏┛┗┓ 
┗┛ ┗┛ ┗┛ ┗━┛ ┗┛ ┗┛ ┗┛ ┗━┛  ┗━━┛ 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

'''
def printer(var, val):
    print(var)
    print(val)
    print(tval)
    time.sleep(0.2)
    os.system('clear')
def runner(val = ' '):
  for i in range(1):
      printer(man1, val)
      printer(man2, val)
      printer(man3, val)
      printer(man4, val)
      printer(man5, val)
      printer(man6, val)
      printer(man7, val)
      printer(man8, val)
      printer(man9, val)
      printer(man10, val)

import os
if __name__ == "__main__":
  runner()
