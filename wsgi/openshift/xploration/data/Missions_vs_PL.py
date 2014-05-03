mission_type = []

earth_obs = {}
earth_obs['name'] = 'Earth observation'
earth_obs['slug'] = 'earth_obs'
earth_obs['opt_sensor'] = True
earth_obs['radio_sensor'] = True
earth_obs['spectrometer'] = True
earth_obs['probe'] = (False, 'remember that you are here to observe')
earth_obs['amplifier'] = (False, 'Maybe in the BUS')

mission_type.append(earth_obs)


cel_body_obs = {}
cel_body_obs['name'] = 'Body observation'
cel_body_obs['slug'] = 'cel_body_obs'
cel_body_obs['opt_sensor'] = True
cel_body_obs['radio_sensor'] = True
cel_body_obs['spectrometer'] = True
cel_body_obs['probe'] = (False, 'remember that you are here to observe')
cel_body_obs['amplifier'] = (False, 'Maybe in the BUS')

mission_type.append(cel_body_obs)

space_obs = {}
space_obs['name'] = 'Space observation'
space_obs['slug'] = 'deep_space_obs'
space_obs['opt_sensor'] = True
space_obs['radio_sensor'] = True
space_obs['spectrometer'] = True
space_obs['probe'] = (False, 'Space dust doesn''t help you observe') 
space_obs['amplifier'] = True

mission_type.append(space_obs)

atm_analysis = {}
atm_analysis['name'] = 'Atmospheric analysis'
atm_analysis['slug'] = 'atm_analysis'
atm_analysis['opt_sensor'] = True
atm_analysis['radio_sensor'] = True
atm_analysis['spectrometer'] = True
atm_analysis['probe'] = (False, 'It''s difficult to collect and bring back gases')
atm_analysis['amplifier'] = (False, 'Maybe in the BUS')

mission_type.append(atm_analysis)

sample_collect = {}
sample_collect['name'] = 'Sample collection'
sample_collect['slug'] = 'sample_collect'
sample_collect['opt_sensor'] = True
sample_collect['radio_sensor'] = (False, 'That''s not the wavelength you are interested in')
sample_collect['spectrometer'] = True
sample_collect['probe'] = True
sample_collect['amplifier'] = (False, 'You have to bring the sample back')

mission_type.append(sample_collect)

telecom = {}
telecom['name'] = 'Telecommunication'
telecom['slug'] = 'telecom'
telecom['opt_sensor'] = (False, 'You do not need to analyze but only to send a signal')
telecom['radio_sensor'] = (False, 'You do not need to analyze but only to send a signal')
telecom['spectrometer'] = (False, 'You do not need to analyze but only to send a signal')
telecom['probe'] = (False, 'You do not need to analyze but only to send a signal')
telecom['amplifier'] = True

mission_type.append(telecom)
