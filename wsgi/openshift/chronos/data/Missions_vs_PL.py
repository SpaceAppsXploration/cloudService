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
earth_obs['laser_alt'] = True
earth_obs['mag'] = True
earth_obs['grav'] = True
earth_obs['particles'] = True
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
cel_body_obs['laser_alt'] = True
cel_body_obs['mag'] = True
cel_body_obs['grav'] = True
cel_body_obs['particles'] = True
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
space_obs['laser_alt'] = (False, 'Too far to measure')
space_obs['mag'] = (False, 'Too far to measure')
space_obs['grav'] = True
space_obs['particles'] = True
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
atm_analysis['laser_alt'] = (False, 'This is for surface measurement')
atm_analysis['mag'] = True
atm_analysis['particles'] = True
atm_analysis['grav'] = (False, 'Gravitation is not an atmospheric issue')
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
sample_collect['laser_alt'] = True
sample_collect['mag'] = True
sample_collect['grav'] = True
sample_collect['probe'] = True
sample_collect['particles'] = (False, 'It\'s definetly not necessary')
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
telecom['laser_alt'] = (False, 'Not needed for telecom')
telecom['mag'] = (False, 'Not needed for telecom')
telecom['grav'] = (False, 'Not needed for telecom')
telecom['particles'] = (False, 'It\'s definetly not necessary')
telecom['probe'] = (False, 'You do not need to analyze but only to send a signal')
telecom['amplifier'] = True

mission_type.append(telecom)
