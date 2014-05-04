# True/False Tables about mission's possible destinations

destinations = []

mercury = {}
mercury['name'] = 'Mercury'
mercury['slug'] = 'mercury'
mercury['distance'] = 0.4
mercury['earth_obs'] = (False, 'Why go this far when you have a nice view in Low Earth Orbit?')
mercury['cel_body_obs'] = True
mercury['deep_space_obs'] = (False, 'To observe outer space, either you travel outside the Solar System to have a "full immersion", or you stay close to Earth to send back more data.')
mercury['atm_analysis'] = True
mercury['sample_collect'] = True
mercury['telecom'] = (False, 'Telecom is intended for Earth, thus stay close to Gaia.')

venus = {}
venus['name'] = 'Venus'
venus['slug'] = 'venus'
venus['distance'] = 0.7
venus['earth_obs'] = (False, 'Why go this far when you have a nice view in Low Earth Orbit?')
venus['cel_body_obs'] = True
venus['deep_space_obs'] = (False, 'To observe outer space, either you travel outside the Solar System to have a "full immersion", or you stay close to Earth to send back more data.')
venus['atm_analysis'] = True
venus['sample_collect'] = True
venus['telecom'] = (False, 'Telecom is intended for Earth, thus stay close to Gaia.')

earth = {}
earth['name'] = 'Earth'
earth['slug'] = 'earth'
earth['distance'] = 1
earth['earth_obs'] = True
earth['cel_body_obs'] = (False, 'Maybe "Earth Observation" is better!')
earth['deep_space_obs'] = True
earth['atm_analysis'] = True
earth['sample_collect'] = (False, 'You do not need a probe to collect samples from Earth. Use a bulldozer instead!')
earth['telecom'] = True

moon = {}
moon['name'] = 'Moon'
moon['slug'] = 'moon'
moon['distance'] = 1
moon['earth_obs'] = (False, 'Why go this far when you have a nice view in Low Earth Orbit?')
moon['cel_body_obs'] = True
moon['deep_space_obs'] = (False, 'To observe outer space, either you travel outside the Solar System to have a "full immersion", or you stay close to Earth to send back more data.')
moon['atm_analysis'] = (False, 'The Moon does not have an atmosphere. Go back to your astronomy book!')
moon['sample_collect'] = True
moon['telecom'] = (False, 'Telecom is intended for Earth, thus stay close to Gaia.')

mars = {}
mars['name'] = 'Mars'
mars['slug'] = 'mars'
mars['distance'] = 1.5
mars['earth_obs'] = (False, 'Why go this far when you have a nice view in Low Earth Orbit?')
mars['cel_body_obs'] = True
mars['deep_space_obs'] = (False, 'To observe outer space, either you travel outside the Solar System to have a "full immersion", or you stay close to Earth to send back more data.')
mars['atm_analysis'] = True
mars['sample_collect'] = True
mars['telecom'] = (False, 'Telecom is intended for Earth, thus stay close to Gaia.')

asteroids = {}
asteroids['name'] = 'Asteroids'
asteroids['slug'] = 'asteroids'
asteroids['distance'] = 2.8
asteroids['earth_obs'] = (False, 'Why go this far when you have a nice view in Low Earth Orbit?')
asteroids['cel_body_obs'] = True
asteroids['deep_space_obs'] = (False, 'To observe outer space, either you travel outside the Solar System to have a "full immersion", or you stay close to Earth to send back more data.')
asteroids['atm_analysis'] = (False, 'Asteroids do not have an atmosphere.')
asteroids['sample_collect'] = True
asteroids['telecom'] = (False, 'Telecom is intended for Earth, thus stay close to Gaia.')

jupiter = {}
jupiter['name'] = 'Jupiter'
jupiter['slug'] = 'jupiter'
jupiter['distance'] = 5.2
jupiter['earth_obs'] = (False, 'Why go this far when you have a nice view in Low Earth Orbit?')
jupiter['cel_body_obs'] = True
jupiter['deep_space_obs'] = (False, 'To observe outer space, either you travel outside the Solar System to have a "full immersion", or you stay close to Earth to send back more data.')
jupiter['atm_analysis'] = True
jupiter['sample_collect'] = (False, 'You could, but once you land it is nearly impossible to go back due to gravity.')
jupiter['telecom'] = (False, 'Telecom is intended for Earth, thus stay close to Gaia.')



saturn = {}
saturn['name'] = 'Saturn'
saturn['slug'] = 'saturn'
saturn['distance'] = 9.5
saturn['earth_obs'] = (False, 'Why go this far when you have a nice view in Low Earth Orbit?')
saturn['cel_body_obs'] = True
saturn['deep_space_obs'] = (False, 'To observe outer space, either you travel outside the Solar System to have a "full immersion", or you stay close to Earth to send back more data.')
saturn['atm_analysis'] = True
saturn['sample_collect'] = (False, 'You could, but once you land it is nearly impossible to go back due to gravity.')
saturn['telecom'] = (False, 'Telecom is intended for Earth, thus stay close to Gaia.')


#uranus = {}
#uranus['name'] = 'Uranus'
#uranus['slug'] = 'uranus'
#uranus['distance'] = 19.2
#uranus['earth_obs'] = (False, 'Why go this far when you have a nice view in Low Earth Orbit?')
#uranus['cel_body_obs'] = True
#uranus['deep_space_obs'] = (False, 'To observe outer space, either you travel outside the Solar System to have a "full immersion", or you stay close to Earth to send back more data.')
#uranus['atm_analysis'] = True
#uranus['sample_collect'] = (False, 'You could, but once you land it is nearly impossible to go back due to gravity.')
#uranus['telecom'] = (False, 'Telecom is intended for Earth, thus stay close to Gaia.')


neptune = {}
neptune['name'] = 'Neptune'
neptune['slug'] = 'neptune'
neptune['distance'] = 30
neptune['earth_obs'] = (False, 'Why go this far when you have a nice view in Low Earth Orbit?')
neptune['cel_body_obs'] = True
neptune['deep_space_obs'] = (False, 'To observe outer space, either you travel outside the Solar System to have a "full immersion", or you stay close to Earth to send back more data.')
neptune['atm_analysis'] = True
neptune['sample_collect'] = (False, 'You could, but once you land it is nearly impossible to go back due to gravity.')
neptune['telecom'] = (False, 'Telecom is intended for Earth, thus stay close to Gaia.')


#comets = {}
#comets['name'] = 'Comets'
#comets['slug'] = 'comets'
#comets['distance'] = 10
#comets['earth_obs'] = (False, 'Why go this far when you have a nice view in Low Earth Orbit?')
#comets['cel_body_obs'] = True
#comets['deep_space_obs'] = (False, 'To observe outer space, either you travel outside the Solar System to have a "full immersion", or you stay close to Earth to send back more data.')
#comets['atm_analysis'] = (False, 'Comets have a "tail" that can be studied, not a proper atmosphere.')
#comets['sample_collect'] = True
#comets['telecom'] = (False, 'Telecom is intended for Earth, thus stay close to Gaia.')


halley = {}
halley['name'] = 'Halley comet'
halley['slug'] = 'halley'
halley['distance'] = 10
halley['earth_obs'] = (False, 'Why go this far when you have a nice view in Low Earth Orbit?')
halley['cel_body_obs'] = True
halley['deep_space_obs'] = (False, 'To observe outer space, either you travel outside the Solar System to have a "full immersion", or you stay close to Earth to send back more data.')
halley['atm_analysis'] = (False, 'Comets have a "tail" that can be studied, not a proper atmosphere.')
halley['sample_collect'] = True
halley['telecom'] = (False, 'Telecom is intended for Earth, thus stay close to Gaia.')

beyond = {}
beyond['name'] = 'Beyond System'
beyond['slug'] = 'beyond'
beyond['distance'] = 50
beyond['earth_obs'] = (False, 'Why go this far when you have a nice view in Low Earth Orbit?')
beyond['cel_body_obs'] = (False, 'Do not travel so far to observe something that is closer.')
beyond['deep_space_obs'] = True
beyond['atm_analysis'] = (False, "What atmposphere are you talkin' about?")
beyond['sample_collect'] = (False, 'Wanna collect space dust this far?')
beyond['telecom'] = (False, 'Telecom is intended for Earth, thus stay close to Gaia.')

sun = {}
sun['name'] = 'Sun'
sun['slug'] = 'sun'
sun['distance'] = 1
sun['earth_obs'] = (False, 'Why go this far when you have a nice view in Low Earth Orbit?')
sun['cel_body_obs'] = True
sun['deep_space_obs'] = (False, 'To observe outer space, either you travel outside the Solar System to have a "full immersion", or you stay close to Earth to send back more data.')
sun['atm_analysis'] = (False, 'You do not want to get a sunburn!')
sun['sample_collect'] = (False, 'You do not want to get a sunburn!')
sun['telecom'] = (False, 'Telecom is intended for Earth, thus stay close to Gaia.')

kbos = {}
kbos['name'] = 'Kuiber Belt'
kbos['slug'] = 'kbos'
kbos['distance'] = 45
kbos['earth_obs'] = (False, 'Why go this far when you have a nice view in Low Earth Orbit?')
kbos['cel_body_obs'] = True
kbos['deep_space_obs'] = (False, 'To observe outer space, either you travel outside the Solar System to have a "full immersion", or you stay close to Earth to send back more data.')
kbos['atm_analysis'] = (False, 'It''s space dust!')
kbos['sample_collect'] = (False, 'Wanna collect space dust this far?')
kbos['telecom'] = (False, 'Telecom is intended for Earth, thus stay close to Gaia.')

dwarf = {}
dwarf['name'] = 'Dwarf planets'
dwarf['slug'] = 'dwarf'
dwarf['distance'] = 45
dwarf['earth_obs'] = (False, 'Why go this far when you have a nice view in Low Earth Orbit?')
dwarf['cel_body_obs'] = True
dwarf['deep_space_obs'] = (False, 'To observe outer space, either you travel outside the Solar System to have a "full immersion", or you stay close to Earth to send back more data.')
dwarf['atm_analysis'] = (False, 'How do you get there?')
dwarf['sample_collect'] = (False, 'Do you know how far they are?!')
dwarf['telecom'] = (False, 'Telecom is intended for Earth, thus stay close to Gaia.')

titan = {}
titan['name'] = 'Titan'
titan['slug'] = 'titan'
titan['distance'] = 9.5
titan['earth_obs'] = (False, 'Why go this far when you have a nice view in Low Earth Orbit?')
titan['cel_body_obs'] = True
titan['deep_space_obs'] = (False, 'To observe outer space, either you travel outside the Solar System to have a "full immersion", or you stay close to Earth to send back more data.')
titan['atm_analysis'] = True
titan['sample_collect'] = True
titan['telecom'] = (False, 'Telecom is intended for Earth, thus stay close to Gaia.')



destinations.append(mercury)
destinations.append(venus)
destinations.append(earth)
destinations.append(moon)
destinations.append(mars)
destinations.append(asteroids)
destinations.append(jupiter)
destinations.append(saturn)
#destinations.append(uranus)
destinations.append(neptune)
#destinations.append(comets)
destinations.append(beyond)
destinations.append(sun)
destinations.append(kbos)
destinations.append(dwarf)
destinations.append(titan)
destinations.append(halley)

