import subprocess


#dir is built into the shell
# subprocess.run('dir', capture_output= True, shell=True)
#
# p1 = subprocess.run('dir', capture_output=True, shell=True)
#
# print(p1.args)
# print(p1.returncode)
# print(p1.stdout)
#
# print(p1.stdout.decode())
#
# p2 = subprocess.run('dir', capture_output=True, shell=True, text=True)
#
# print(p2.stdout)
#
# p3 = subprocess.run('dir', stdout=subprocess.PIPE, shell=True, text=True)
#
# print(p3)

# with open('output.txt', 'w') as f:
#     p3 = subprocess.run('dir', stdout=f, shell=True, text=True)



# p3 = subprocess.run('dir /dne', capture_output=True, shell=True, text=True)
p3 = subprocess.run('dir /dne', stderr=subprocess.DEVNULL, shell=True)

print(p3.returncode)
print(p3.stderr)

