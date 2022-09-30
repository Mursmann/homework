from datetime import date
from datetime import datetime
#date main
date = date.today()
correct_date = date.strftime('%d/%m/%Y')
#time main
time = datetime.now()
correct_time = time.strftime('%H:%M:%S')
#output
print('Astazi e data de: ', correct_date)
print('Este ora: ', correct_time)