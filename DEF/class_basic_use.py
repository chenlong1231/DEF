class dog:
    species = 'mammal'

    def __init__(self, country, name, age):
        self.country = country
        self.name = name
        self.age = age


class dog_speed(dog):

    def dog_run(self, speed):
        return '{} runs {}'.format(self.name, speed)


a = dog('UK', "Tommy", 12)
b = dog('US', "Jim", 5)
c = dog_speed('CHN', 'Maomao', 4)
print(a.name + ' is from ' + a.country)
print(b.name + ' is from ' + b.country)
b.species = 'mammal'
a.species = 'Another'
if b.species == 'mammal':
    print(b.species)
else:
    print(False)

if a.species == 'mammal':
    print(a.species)
else:
    print(False)
print(c.dog_run('fast'))
print("{} is {} years old, which is from {}, and it runs {}".format(c.name, c.age, c.country, c.dog_run('fast')))
