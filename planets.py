planet_list = ["Mercury", "Mars"]

#Use append() to add Jupiter and Saturn at the end of the list.
planet_list.append('Jupiter')
planet_list.append('Saturn')
print('planets appended: {}'.format(planet_list))

#Use the extend() method to add another list of 
#the last two planets in our solar system to the end of the list.
planet_list.extend(['Uranus', 'Neptune'])
print('planets extended: {}'.format(planet_list))

#Use insert() to add Earth, and Venus in the correct order.
planet_list.insert(1, 'Venus')
planet_list.insert(2, 'Earth')
print('planets inserted: {}'.format(planet_list))

#Use append() again to add Pluto to the end of the list.
planet_list.append('Pluto')
print('planets with pluto: {}'.format(planet_list))

#Now that all the planets are in the list, 
#slice the list in order to get the 
#rocky planets into a new list called rocky_planets.
rocky_planets = list()
rocky_planets = planet_list[0:3]
print('rocky planets: {}'.format(rocky_planets))

#Being good amateur astronomers, 
#we know that Pluto is now a dwarf planet, 
#so use the del operation to remove it from the end of planet_list.
del planet_list[-1]
print('no pluto: {}'.format(planet_list))

#Create another list containing tuples.
#Each tuple will hold the name of a spacecraft that we have launched, 
#and the names of the planet(s) that it has visited, 
#or landed on. (e.g. ('Cassini', 'Saturn')).
space_missions = list()
space_missions.extend([
	('a', 'Mercury', 'Venus'),
	('b', 'Venus'),
	('c', 'Earth', 'Uranus', 'Neptune', 'Venus'),
	('d', 'Mars'),
	('e', 'Jupiter'),
	('f', 'Saturn', 'Neptune', 'Venus'),
	('g', 'Uranus')])

#Iterate over your list of planets, 
#and inside that loop, iterate over the list of tuples. 
#Print, for each planet, which satellites have visited.
planets_and_their_satellites = dict()
for planet in planet_list:
	planets_and_their_satellites[planet] = list()
	for mission in space_missions:
		if planet in mission:
			planets_and_their_satellites[planet].append(mission[0])
			print('planets_and_their_satellites: {}'.format(planets_and_their_satellites))

for planet, satellites in planets_and_their_satellites.items():
	print('{} has been visited by satellites: {}'.format(planet, satellites))



			
















