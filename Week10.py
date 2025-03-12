
#solarobject class for general things in space
class SolarObject:
    def __init__(self, name, sun, orbit):
        self.name = name
        self.sun = sun
        self.orbit = orbit
        self.time = round((6000000000/sun) / 1000000000) #rounds the population of earth/sun distance and then rounds it to the billionth
        self.years = "days"                                 #think you wanted this to be called "Colonization"
    def spin(self):                                         #but i was alreadly like, halfway through the program when I read that, so it's called time!
        pass

class Planet(SolarObject):
    def __init__(self, name, sun, orbit):
        super().__init__(name, sun, orbit) #super makes Planet() inheret everything from solarobject
    def spin(self):
        spintype = "slightly eliptical"
        return spintype
class Comet(SolarObject):
    def __init__(self, name, sun, orbit):
        super().__init__(name, sun, orbit)
        self.orbit = self.orbit/365 #makes orbit in years
        self.years = "years"
    def spin(self):
        spintype = "like crazy"
        return spintype
earth = Planet("Earth", 1, 365.6)
mars = Planet("Mars",1.5, 687)
halley = Comet("Halley",35,27740)
halebopp = Comet("HaleBopp",354,875010.85)

#prints the info on halley, then halebopp, then eart, then mars
print(f'{halley.name} is {halley.sun} au away from the sun, spins {halley.spin()}, has an orbit taking {halley.orbit} {halley.years}, and can support a population of {halley.time} billion')
print(f'{halebopp.name} is {halebopp.sun} au away from the sun, spins {halebopp.spin()}, has an orbit taking {halebopp.orbit} {halebopp.years}, and can support a population of {halebopp.time} billion')
print(f'{earth.name} is {earth.sun} au away from the sun, spins {earth.spin()}, has an orbit taking {earth.orbit} {earth.years}, and can support a population of {earth.time} billion')
print(f'{mars.name} is {mars.sun} au away from the sun, spins {mars.spin()}, has an orbit taking {mars.orbit} {mars.years}, and can support a population of {mars.time} billion')

#f strings just make this all easier
#this one took me a minute, i think its just the looming threat of finals week gettin to me
#OOP is really interesting!