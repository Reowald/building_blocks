class C:
    def __init__(self):
        self.b= {}

c1=C()
c2=C()

c1.b[1]='s1'
c1.b[2]='s5'
c2.b[1]='s1'
c2.b[2]='s8'

print(c1.b[1]) #s1
print(c2.b[1]) #s1

print(id(c1.b[1]))
print(id(c1.b[2]))
print(id(c2.b[1]))
print(id(c2.b[2]))

print(type(c1.b))
print(c1.b)
print(type(c2.b))
print(c2.b)



