# rh_stable.py

import numpy

# === Input ===
print("Enter the coefficients of the characteristic equation: ", end='')
coefficient_array = [float(x) for x in input().split()]

column_len = len(coefficient_array)
row_len = column_len/2
rh_matrix = numpy.zeros((int(column_len), int(row_len)))

print(rh_matrix)

# === Computation ===

# === Output ===

for i in range(0,column_len):
	if (rh_matrix[i][0] > 0):
		# if positive
		print("true")
	elif (rh_matrix[i][0] < 0):
		#if negative
		print("false")
	else:
		print("debug")
