mission_type = []

earth_obs = {}
earth_obs['name'] = 'Earth observation'
earth_obs['slug'] = 'earth_obs'
earth_obs['opt_sensor'] = True
earth_obs['radio_sensor'] = True
earth_obs['spectrometer'] = False
earth_obs['probe'] = False
earth_obs['amplifier'] = False

mission_type.append(earth_obs)


cel_body_obs = {}
cel_body_obs['name'] = 'Body observation'
cel_body_obs['slug'] = 'cel_body_obs'
cel_body_obs['opt_sensor'] = True
cel_body_obs['radio_sensor'] = True
cel_body_obs['spectrometer'] = True
cel_body_obs['probe'] = False
cel_body_obs['amplifier'] = False

mission_type.append(cel_body_obs)

space_obs = {}
space_obs['name'] = 'Space observation'
space_obs['slug'] = 'deep_space_obs'
space_obs['opt_sensor'] = True
space_obs['radio_sensor'] = True
space_obs['spectrometer'] = True
space_obs['probe'] = False
space_obs['amplifier'] = True

mission_type.append(space_obs)

atm_analysis = {}
atm_analysis['name'] = 'Atmospheric analysis'
atm_analysis['slug'] = 'atm_analysis'
atm_analysis['opt_sensor'] = True
atm_analysis['radio_sensor'] = True
atm_analysis['spectrometer'] = True
atm_analysis['probe'] = False
atm_analysis['amplifier'] = False

mission_type.append(atm_analysis)

sample_collect = {}
sample_collect['name'] = 'Sample collection'
sample_collect['slug'] = 'sample_collect'
sample_collect['opt_sensor'] = True
sample_collect['radio_sensor'] = False
sample_collect['spectrometer'] = True
sample_collect['probe'] = True
sample_collect['amplifier'] = False

mission_type.append(sample_collect)

telecom = {}
telecom['name'] = 'Telecommunication'
telecom['slug'] = 'telecom'
telecom['opt_sensor'] = False
telecom['radio_sensor'] = False
telecom['spectrometer'] = False
telecom['probe'] = False
telecom['amplifier'] = True

mission_type.append(telecom)