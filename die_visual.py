from die import Die
import time
import pygal

start = time.time()
# Create a D6
die1 = Die()
die2 = Die()
die3 = Die()
die4 = Die()
die5 = Die()

results = []
for roll_num in range(1000000000):
	result = die1.roll()+die2.roll()+die3.roll()+die4.roll()+die5.roll()
	results.append(result)

frequencies = []
for value in range(1, 30):
	frequency = results.count(value)
	frequencies.append(frequency)

# print(frequencies)

hist=pygal.Bar()

hist.title = "Results of rolling one D26 10000000 times"
hist.x_labels = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D26', frequencies)
hist.render_to_file('die_visual.svg')

end = time.time()
runtime = end-start
print(runtime)
