# Class_Ex1:
# Write python program that converts seconds to
# (x Hour, x min, x seconds)
# ----------------------------------------------------------------

S=int(input('Please enter seconds:'))
if S>=3600:
    H=S//3600
    M=((S%3600)//60)
    Sec=((S%3600)%60)
    print('Hours:',H,'Minutes:',M,'Seconds:',Sec)
else:
    print('Hours:', '0', 'Minutes:', S//60, 'Seconds:', S%60)
exit()
#-----------------------------------------------------------
