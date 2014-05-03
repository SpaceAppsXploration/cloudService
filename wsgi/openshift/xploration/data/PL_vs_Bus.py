# True/False about PL

pl_vs_bus_type = []

opt_sensor = {}
opt_sensor['name'] = 'Optical Sensor'
opt_sensor['slug'] = 'opt_sensor'
opt_sensor['therm_active'] = True
opt_sensor['therm_passive'] = True
opt_sensor['pow_prim_panels'] = True
opt_sensor['pow_prim_rtg'] = True
opt_sensor['pow_sec_batt'] = True
opt_sensor['pow_sec_fc'] = True
opt_sensor['comm_mono'] = True
opt_sensor['comm_omni'] = True
opt_sensor['aodcs_robust'] = True
opt_sensor['aodcs_simple'] = (False, 'You need to be precise in pointing where you wanna look at')
opt_sensor['prop_electr'] = True
opt_sensor['prop_chem'] = True
opt_sensor['cdh_standard'] = (False, 'A huge amount of data might be tranferred')
opt_sensor['cdh_optim'] = True
opt_sensor['struct_stand'] = True
opt_sensor['struct_high_resist'] = True

pl_vs_bus_type.append(opt_sensor)


radio_sensor = {}
radio_sensor['name'] = 'Radio Sensor'
radio_sensor['slug'] = 'radio_sensor'
radio_sensor['therm_active'] = True
radio_sensor['therm_passive'] = True
radio_sensor['pow_prim_panels'] = True
radio_sensor['pow_prim_rtg'] = (False, 'RTGs might be not completely shielded and can interfere with radio sensors')
radio_sensor['pow_sec_batt'] = True
radio_sensor['pow_sec_fc'] = True
radio_sensor['comm_mono'] = True
radio_sensor['comm_omni'] = True
radio_sensor['aodcs_robust'] = True
radio_sensor['aodcs_simple'] = True
radio_sensor['prop_electr'] = True
radio_sensor['prop_chem'] = True
radio_sensor['cdh_standard'] = True
radio_sensor['cdh_optim'] = True
radio_sensor['struct_stand'] = True
radio_sensor['struct_high_resist'] = True

pl_vs_bus_type.append(radio_sensor)



spectrometer = {}
spectrometer['name'] = 'Spectrometer'
spectrometer['slug'] = 'spectrometer'
spectrometer['therm_active'] = True
spectrometer['therm_passive'] = (False, 'the spectrometer needs a quasi-constant thermal environment')
spectrometer['pow_prim_panels'] = True
spectrometer['pow_prim_rtg'] = (False, 'RTGs might be not completely shielded and can interfere with radio sensors')
spectrometer['pow_sec_batt'] = True
spectrometer['pow_sec_fc'] = True
spectrometer['comm_mono'] = True
spectrometer['comm_omni'] = True
spectrometer['aodcs_robust'] = True
spectrometer['aodcs_simple'] = True
spectrometer['prop_electr'] = (False, 'Charged particles might interfere with spectrometeres')
spectrometer['prop_chem'] = True
spectrometer['cdh_standard'] = True
spectrometer['cdh_optim'] = True
spectrometer['struct_stand'] = True
spectrometer['struct_high_resist'] = True

pl_vs_bus_type.append(spectrometer)



probe = {}
probe['name'] = 'Probe'
probe['slug'] = 'probe'
probe['therm_active'] = True
probe['therm_passive'] = True
probe['pow_prim_panels'] = True
probe['pow_prim_rtg'] = True
probe['pow_sec_batt'] = True
probe['pow_sec_fc'] = True
probe['comm_mono'] = True
probe['comm_omni'] = True
probe['aodcs_robust'] = True
probe['aodcs_simple'] = (False, 'You have to locate precisely where you need to go')
probe['prop_electr'] = True
probe['prop_chem'] = True
probe['cdh_standard'] = True
probe['cdh_optim'] = True
probe['struct_stand'] = (False, 'the spacecraft must withstand high structural stresses')
probe['struct_high_resist'] = True

pl_vs_bus_type.append(probe)



amplifier = {}
amplifier['name'] = 'Amplifier'
amplifier['slug'] = 'amplifier'
amplifier['therm_active'] = True
amplifier['therm_passive'] = True
amplifier['pow_prim_panels'] = True
amplifier['pow_prim_rtg'] = True
amplifier['pow_sec_batt'] = True
amplifier['pow_sec_fc'] = True
amplifier['comm_mono'] = True
amplifier['comm_omni'] = True
amplifier['aodcs_robust'] = True
amplifier['aodcs_simple'] = True
amplifier['prop_electr'] = True
amplifier['prop_chem'] = True
amplifier['cdh_standard'] = True
amplifier['cdh_optim'] = True
amplifier['struct_stand'] = True
amplifier['struct_high_resist'] = True

pl_vs_bus_type.append(amplifier)


