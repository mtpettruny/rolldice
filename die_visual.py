from die import Die
import time

start = time.time()
# Create a D6
die = Die()

results = []
for roll_num in range(10000000):
	result = die.roll()
	results.append(result)

frequencies = []
for value in range(1, die.num_sides+1):
	frequency = results.count(value)
	frequencies.append(frequency)

print(frequencies)
end = time.time()
runtime = end-start
print(runtime)
