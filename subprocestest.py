# varianta 1:
#
# import subprocess
#
# cmd = r'./meniutest.exe'
# with open("output.txt", "a") as f:
#     for i in range(1, 5):
#         option = str(i)
#
#         process = subprocess.Popen([cmd],
#                                    stdin=subprocess.PIPE,
#                                    stdout=subprocess.PIPE,
#                                    stderr=subprocess.PIPE)
#         input_data = f"{option}\n".encode()
#         output, error = process.communicate(input_data)
#         output_str = output.decode().strip()
#
#         # Foloseste output_str pentru a salva sau procesa outputul
#         print(f"Output pentru optiunea {option}: {output_str}")
#         f.write(f"Output pentru optiunea {option}: {output_str}\n")
#
# print("input_data: %s" % input_data)
# print("stdout: %s" % output)
# print("stderr: %s" % error)

# Varianta 2 :

import subprocess

process = subprocess.Popen(["./meniutest.exe"],
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
input_data = b"1\n 4 \n"
output, error = process.communicate(input_data)
output_str = output.decode().strip()
print(f"Output: {output_str}")

import subprocess

process = subprocess.Popen(["./meniutest.exe"],
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
input_data = b"2\n 4 \n"
output, error = process.communicate(input_data)
output_str = output.decode().strip()
print(f"Output: {output_str}")

# import subprocess
#
process = subprocess.Popen(["./meniutest.exe"],
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
input_data = b"3\n 4 \n"
output, error = process.communicate(input_data)
output_str = output.decode().strip()
print(f"Output: {output_str}")
#

process = subprocess.Popen(["./meniutest.exe"],
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
input_data = b"4\n 4 \n"
output, error = process.communicate(input_data)
output_str = output.decode().strip()
print(f"Output: {output_str}")
