import subprocess
import time

def run_lp(lp_formulation, input_file, output_file):
	
	with open(input_file, "w") as f:
		f.write(lp_formulation)

	t0 = time.time()
	bits = subprocess.check_output(['lp_solve', input_file])
	t1 = time.time()
	t = t1 - t0 

	with open(output_file, "wb") as f:
		f.write(bits)

	return t

