from scoop import Scoop, Bowl, BigBowl

s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('coffee')
s4 = Scoop('chocolate')
s5 = Scoop('vanilla')
s6 = Scoop('coffee')

print(s1.flavor)   # should print chocolate

for one_scoop in [s1, s2, s3]:
    print(one_scoop.flavor)

b = Bowl()
b.add_scoops(s1, s2)   # add_scoops can take *any* number of Scoop arguments
b.add_scoops(s3)
b.add_scoops(s4, s5, s6)
print(b.scoops)        # prints a list of scoop objects (it'll look ugly)
print(b.flavors())     # prints a list of strings, the flavors from the scoops

bb = BigBowl()
bb.add_scoops(s1, s2)   # add_scoops can take *any* number of Scoop arguments
bb.add_scoops(s3)
bb.add_scoops(s4, s5, s6)
print(bb.flavors())     # prints a list of strings, the flavors from the scoops
