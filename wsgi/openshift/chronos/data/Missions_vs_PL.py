mission_type = []

earth_obs = {}
earth_obs['name'] = 'Earth observation'
earth_obs['slug'] = 'earth_obs'
earth_obs['opt_sensor'] = True
earth_obs['radio_sensor'] = True
earth_obs['microwave'] = True
earth_obs['infrared'] = True
earth_obs['ultraviolet'] = True
earth_obs['x_rays'] = True
earth_obs['gamma_rays'] = True
earth_obs['probe'] = (False, 'Remember that you are here to observe')
earth_obs['amplifier'] = (False, 'Maybe in the BUS')

mission_type.append(earth_obs)


cel_body_obs = {}
cel_body_obs['name'] = 'Body observation'
cel_body_obs['slug'] = 'cel_body_obs'
cel_body_obs['opt_sensor'] = True
cel_body_obs['radio_sensor'] = True
cel_body_obs['microwave'] = True
cel_body_obs['infrared'] = True
cel_body_obs['ultraviolet'] = True
cel_body_obs['x_rays'] = True
cel_body_obs['gamma_rays'] = True
cel_body_obs['satellite'] = True
cel_body_obs['lander_orbiter'] = True
cel_body_obs['lander_rover'] = True
cel_body_obs['probe'] = (False, 'Remember that you are here to observe')
cel_body_obs['amplifier'] = (False, 'Maybe in the BUS')

mission_type.append(cel_body_obs)

space_obs = {}
space_obs['name'] = 'Space observation'
space_obs['slug'] = 'deep_space_obs'
space_obs['opt_sensor'] = True
space_obs['radio_sensor'] = True
space_obs['microwave'] = True
space_obs['infrared'] = True
space_obs['ultraviolet'] = True
space_obs['x_rays'] = True
space_obs['gamma_rays'] = True
space_obs['satellite'] = True
space_obs['lander_orbiter'] = (False, 'Cannot land or orbit deep space')
space_obs['lander_rover'] = (False, 'Cannot land or orbit deep space')
space_obs['probe'] = (False, 'Space dust doesn''t help you observe') 
space_obs['amplifier'] = True

mission_type.append(space_obs)

atm_analysis = {}
atm_analysis['name'] = 'Atmospheric analysis'
atm_analysis['slug'] = 'atm_analysis'
atm_analysis['opt_sensor'] = True
atm_analysis['radio_sensor'] = True
atm_analysis['microwave'] = True
atm_analysis['infrared'] = True
atm_analysis['ultraviolet'] = True
atm_analysis['x_rays'] = True
atm_analysis['gamma_rays'] = True
atm_analysis['satellite'] = True
atm_analysis['lander_orbiter'] = True
atm_analysis['lander_rover'] = True
atm_analysis['probe'] = (False, 'It''s difficult to collect and bring back gases')
atm_analysis['amplifier'] = (False, 'Maybe in the BUS')

mission_type.append(atm_analysis)

sample_collect = {}
sample_collect['name'] = 'Sample collection'
sample_collect['slug'] = 'sample_collect'
sample_collect['opt_sensor'] = True
sample_collect['radio_sensor'] = (False, 'That''s not the wavelength you are interested in')
sample_collect['microwave'] = True
sample_collect['infrared'] = True
sample_collect['ultraviolet'] = True
sample_collect['x_rays'] = True
sample_collect['gamma_rays'] = True
sample_collect['satellite'] = (False, 'Cannot sample collect')
sample_collect['lander_orbiter'] = True
sample_collect['lander_rover'] = True
sample_collect['probe'] = True
sample_collect['amplifier'] = (False, 'You have to bring the sample back')

mission_type.append(sample_collect)

telecom = {}
telecom['name'] = 'Telecommunication'
telecom['slug'] = 'telecom'
telecom['opt_sensor'] = (False, 'You do not need to analyze but only to send a signal')
telecom['radio_sensor'] = (False, 'You do not need to analyze but only to send a signal')
telecom['microwave'] = (False, 'You do not need to analyze but only to send a signal')
telecom['infrared'] = (False, 'You do not need to analyze but only to send a signal')
telecom['ultraviolet'] = (False, 'You do not need to analyze but only to send a signal')
telecom['x_rays'] = (False, 'You do not need to analyze but only to send a signal')
telecom['gamma_rays'] = (False, 'You do not need to analyze but only to send a signal')
telecom['satellite'] = True
telecom['lander_orbiter'] = (False, 'No need for a lander for telecom')
telecom['lander_rover'] = (False, 'No need for a lander for telecom')
telecom['probe'] = (False, 'You do not need to analyze but only to send a signal')
telecom['amplifier'] = True

mission_type.append(telecom)
