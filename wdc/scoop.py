class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor


# is-a : inheritance  A is-a B    Car is-a Vehicle
# has-a: composition  A has-a B   Bowl has-a Scoop


class Bowl:
    max_scoops = 3

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *args):
        self.scoops += args[:self.max_scoops - len(self.scoops)]

        # for one_scoop in args:
        #     if len(self.scoops) >= self.max_scoops:
        #         break
        #     self.scoops.append(one_scoop)

    def flavors(self):
        return [one_scoop.flavor
                for one_scoop in self.scoops]

        # output = []
        #
        # for one_scoop in self.scoops:
        #     output.append(one_scoop.flavor)
        #
        # return output


class BigBowl(Bowl):
    max_scoops = 5


# Create a new class, BigBowl
# maximum scoops will be 5 (not 3)
# minimize code