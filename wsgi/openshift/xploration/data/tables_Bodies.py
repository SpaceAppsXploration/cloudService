# True/False Tables about mission's possible destinations

destinations = []

mercury = {}
mercury['name'] = 'Mercury'
mercury['slug'] = 'mercury'
mercury['distance'] = 0.4
mercury['earth_obs'] = False
mercury['cel_body_obs'] = True
mercury['deep_space_obs'] = False
mercury['atm_analysis'] = True
mercury['sample_collect'] = True
mercury['telecom'] = False

venus = {}
venus['name'] = 'Venus'
venus['slug'] = 'venus'
venus['distance'] = 0.7
venus['earth_obs'] = False
venus['cel_body_obs'] = True
venus['deep_space_obs'] = False
venus['atm_analysis'] = True
venus['sample_collect'] = True
venus['telecom'] = False

earth = {}
earth['name'] = 'Earth'
earth['slug'] = 'earth'
earth['distance'] = 1
earth['earth_obs'] = True
earth['cel_body_obs'] = False
earth['deep_space_obs'] = True
earth['atm_analysis'] = True
earth['sample_collect'] = False
earth['telecom'] = True

moon = {}
moon['name'] = 'Moon'
moon['slug'] = 'moon'
moon['distance'] = 1
moon['earth_obs'] = False
moon['cel_body_obs'] = True
moon['deep_space_obs'] = False
moon['atm_analysis'] = False
moon['sample_collect'] = True
moon['telecom'] = False

mars = {}
mars['name'] = 'Mars'
mars['slug'] = 'mars'
mars['distance'] = 1.5
mars['earth_obs'] = False
mars['cel_body_obs'] = True
mars['deep_space_obs'] = False
mars['atm_analysis'] = True
mars['sample_collect'] = True
mars['telecom'] = False

asteroids = {}
asteroids['name'] = 'Asteroids'
asteroids['slug'] = 'asteroids'
asteroids['distance'] = 2.8
asteroids['earth_obs'] = False
asteroids['cel_body_obs'] = True
asteroids['deep_space_obs'] = False
asteroids['atm_analysis'] = False
asteroids['sample_collect'] = True
asteroids['telecom'] = False

jupiter = {}
jupiter['name'] = 'Jupiter'
jupiter['slug'] = 'jupiter'
jupiter['distance'] = 5.2
jupiter['earth_obs'] = False
jupiter['cel_body_obs'] = True
jupiter['deep_space_obs'] = False
jupiter['atm_analysis'] = True
jupiter['sample_collect'] = True
jupiter['telecom'] = False



saturn = {}
saturn['name'] = 'Saturn'
saturn['slug'] = 'saturn'
saturn['distance'] = 9.5 
saturn['earth_obs'] = False
saturn['cel_body_obs'] = True
saturn['deep_space_obs'] = False
saturn['atm_analysis'] = True
saturn['sample_collect'] = True
saturn['telecom'] = False


uranus = {}
uranus['name'] = 'Uranus'
uranus['slug'] = 'uranus'
uranus['distance'] = 19.2
uranus['earth_obs'] = False
uranus['cel_body_obs'] = True
uranus['deep_space_obs'] = False
uranus['atm_analysis'] = True
uranus['sample_collect'] = True
uranus['telecom'] = False


neptune = {}
neptune['name'] = 'Neptune'
neptune['slug'] = 'neptune'
neptune['distance'] = 30
neptune['earth_obs'] = False
neptune['cel_body_obs'] = True
neptune['deep_space_obs'] = False
neptune['atm_analysis'] = True
neptune['sample_collect'] = True
neptune['telecom'] = False


comets = {}
comets['name'] = 'Comets'
comets['slug'] = 'comets'
comets['distance'] = 10
comets['earth_obs'] = False
comets['cel_body_obs'] = True
comets['deep_space_obs'] = False
comets['atm_analysis'] = False
comets['sample_collect'] = True
comets['telecom'] = False

space = {}
space['name'] = 'Space'
space['slug'] = 'space'
space['distance'] = 50
space['earth_obs'] = False
space['cel_body_obs'] = False
space['deep_space_obs'] = True
space['atm_analysis'] = False
space['sample_collect'] = False
space['telecom'] = False

destinations.append(mercury)
destinations.append(venus)
destinations.append(earth)
destinations.append(moon)
destinations.append(mars)
destinations.append(asteroids)
destinations.append(jupiter)
destinations.append(saturn)
destinations.append(uranus)
destinations.append(neptune)
destinations.append(comets)
destinations.append(space)
