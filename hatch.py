from datetime import datetime
import math

now = datetime.now()
currentYear = int(now.strftime("%Y"))

k = 30 #hatches per sqkm
p_d = 40000 #max population density

def inputNumber(msg): #метод проверяет введено ли число и положительно ли оно 
	flag = False
	res = 0
	while (not flag):
		try:
			res = int(input(msg + '(enter real values)'))
		except NameError:
			print ("Enter only numbers!")
		if (res > 0):
			flag = True
	return res
area = inputNumber('City urban area, sqkm ')
inhbs = inputNumber('Number of inhabitants ')
year = inputNumber('Foundation year, YYYY ')

if currentYear-year > 100: # старые города (условно старше 100 лет) имеют плохопродуманную сеть подземных коммуникаций
	res = int((area*k)/float(math.log(p_d/(inhbs/area))))
else:
	res = int((area*k)/float(math.log(p_d/(inhbs/area)))*1.2) 
print "Number of hatches: ", res


