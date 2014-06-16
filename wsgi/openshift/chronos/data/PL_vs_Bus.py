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
radio_sensor['pow_prim_rtg'] = True
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



microwave = {}
microwave['name'] = 'Microwave'
microwave['slug'] = 'microwave'
microwave['therm_active'] = True
microwave['therm_passive'] = (False, 'the spectrometer needs a quasi-constant thermal environment')
microwave['pow_prim_panels'] = True
microwave['pow_prim_rtg'] = True
microwave['pow_sec_batt'] = True
microwave['pow_sec_fc'] = True
microwave['comm_mono'] = True
microwave['comm_omni'] = True
microwave['aodcs_robust'] = True
microwave['aodcs_simple'] = True
microwave['prop_electr'] = True
microwave['prop_chem'] = True
microwave['cdh_standard'] = True
microwave['cdh_optim'] = True
microwave['struct_stand'] = True
microwave['struct_high_resist'] = True

pl_vs_bus_type.append(microwave)



infrared = {}
infrared['name'] = 'Infrared'
infrared['slug'] = 'infrared'
infrared['therm_active'] = True
infrared['therm_passive'] = (False, 'the spectrometer needs a quasi-constant thermal environment')
infrared['pow_prim_panels'] = True
infrared['pow_prim_rtg'] = True
infrared['pow_sec_batt'] = True
infrared['pow_sec_fc'] = True
infrared['comm_mono'] = True
infrared['comm_omni'] = True
infrared['aodcs_robust'] = True
infrared['aodcs_simple'] = True
infrared['prop_electr'] = True
infrared['prop_chem'] = True
infrared['cdh_standard'] = True
infrared['cdh_optim'] = True
infrared['struct_stand'] = True
infrared['struct_high_resist'] = True

pl_vs_bus_type.append(infrared)



ultraviolet = {}
ultraviolet['name'] = 'Ultravioet'
ultraviolet['slug'] = 'ulraviolet'
ultraviolet['therm_active'] = True
ultraviolet['therm_passive'] = (False, 'the spectrometer needs a quasi-constant thermal environment')
ultraviolet['pow_prim_panels'] = True
ultraviolet['pow_prim_rtg'] = True
ultraviolet['pow_sec_batt'] = True
ultraviolet['pow_sec_fc'] = True
ultraviolet['comm_mono'] = True
ultraviolet['comm_omni'] = True
ultraviolet['aodcs_robust'] = True
ultraviolet['aodcs_simple'] = True
ultraviolet['prop_electr'] = True
ultraviolet['prop_chem'] = True
ultraviolet['cdh_standard'] = True
ultraviolet['cdh_optim'] = True
ultraviolet['struct_stand'] = True
ultraviolet['struct_high_resist'] = True

pl_vs_bus_type.append(ultraviolet)

x_rays = {}
x_rays['name'] = 'X_rays'
x_rays['slug'] = 'x_rays'
x_rays['therm_active'] = True
x_rays['therm_passive'] = (False, 'the spectrometer needs a quasi-constant thermal environment')
x_rays['pow_prim_panels'] = True
x_rays['pow_prim_rtg'] = True
x_rays['pow_sec_batt'] = True
x_rays['pow_sec_fc'] = True
x_rays['comm_mono'] = True
x_rays['comm_omni'] = True
x_rays['aodcs_robust'] = True
x_rays['aodcs_simple'] = True
x_rays['prop_electr'] = True
x_rays['prop_chem'] = True
x_rays['cdh_standard'] = True
x_rays['cdh_optim'] = True
x_rays['struct_stand'] = True
x_rays['struct_high_resist'] = True

pl_vs_bus_type.append(x_rays)



gamma_rays = {}
gamma_rays['name'] = 'Gamma_rays'
gamma_rays['slug'] = 'gamma_rays'
gamma_rays['therm_active'] = True
gamma_rays['therm_passive'] = (False, 'the spectrometer needs a quasi-constant thermal environment')
gamma_rays['pow_prim_panels'] = True
gamma_rays['pow_prim_rtg'] = True
gamma_rays['pow_sec_batt'] = True
gamma_rays['pow_sec_fc'] = True
gamma_rays['comm_mono'] = True
gamma_rays['comm_omni'] = True
gamma_rays['aodcs_robust'] = True
gamma_rays['aodcs_simple'] = True
gamma_rays['prop_electr'] = True
gamma_rays['prop_chem'] = True
gamma_rays['cdh_standard'] = True
gamma_rays['cdh_optim'] = True
gamma_rays['struct_stand'] = True
gamma_rays['struct_high_resist'] = True

pl_vs_bus_type.append(gamma_rays)



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


