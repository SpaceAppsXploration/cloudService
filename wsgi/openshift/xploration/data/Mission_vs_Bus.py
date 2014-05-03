# True/False Tables about mission's operations (objectives)

bus_vs_mission_type = []

earth_obs = {}
earth_obs['name'] = 'Earth observation'
earth_obs['slug'] = 'earth_obs'
earth_obs['therm_active'] = True
earth_obs['therm_passive'] = True
earth_obs['pow_prim_panels'] = True
earth_obs['pow_prim_rtg'] = True
earth_obs['pow_sec_batt'] = True
earth_obs['pow_sec_fc'] = True
earth_obs['comm_mono'] = True
earth_obs['comm_omni'] = True
earth_obs['aodcs_robust'] = True
earth_obs['aodcs_simple'] = True
earth_obs['prop_electr'] = True
earth_obs['prop_chem'] = True
earth_obs['cdh_standard'] = True
earth_obs['cdh_optim'] = True
earth_obs['struct_stand'] = True
earth_obs['struct_high_resist'] = True

bus_vs_mission_type.append(earth_obs)


cel_body_obs = {}
cel_body_obs['name'] = 'Body observation'
cel_body_obs['slug'] = 'body_obs'
cel_body_obs['therm_active'] = True
cel_body_obs['therm_passive'] = True
cel_body_obs['pow_prim_panels'] = True
cel_body_obs['pow_prim_rtg'] = True
cel_body_obs['pow_sec_batt'] = True
cel_body_obs['pow_sec_fc'] = True
cel_body_obs['comm_mono'] = True
cel_body_obs['comm_omni'] = True
cel_body_obs['aodcs_robust'] = True
cel_body_obs['aodcs_simple'] = True
cel_body_obs['prop_electr'] = True
cel_body_obs['prop_chem'] = True
cel_body_obs['cdh_standard'] = True
cel_body_obs['cdh_optim'] = True
cel_body_obs['struct_stand'] = True
cel_body_obs['struct_high_resist'] = True

bus_vs_mission_type.append(cel_body_obs)



space_obs = {}
space_obs['name'] = 'Space observation'
space_obs['slug'] = 'space_obs'
space_obs['therm_active'] = True
space_obs['therm_passive'] = True
space_obs['pow_prim_panels'] = True
space_obs['pow_prim_rtg'] = True
space_obs['pow_sec_batt'] = True
space_obs['pow_sec_fc'] = True
space_obs['comm_mono'] = True
space_obs['comm_omni'] = True
space_obs['aodcs_robust'] = True
space_obs['aodcs_simple'] = True
space_obs['prop_electr'] = True
space_obs['prop_chem'] = True
space_obs['cdh_standard'] = True
space_obs['cdh_optim'] = True
space_obs['struct_stand'] = True
space_obs['struct_high_resist'] = True

bus_vs_mission_type.append(space_obs)



atm_analysis = {}
atm_analysis['name'] = 'Athmosphere Analysis'
atm_analysis['slug'] = 'atm_analysis'
atm_analysis['therm_active'] = True
atm_analysis['therm_passive'] = True
atm_analysis['pow_prim_panels'] = True
atm_analysis['pow_prim_rtg'] = True
atm_analysis['pow_sec_batt'] = True
atm_analysis['pow_sec_fc'] = True
atm_analysis['comm_mono'] = True
atm_analysis['comm_omni'] = True
atm_analysis['aodcs_robust'] = True
atm_analysis['aodcs_simple'] = True
atm_analysis['prop_electr'] = True
atm_analysis['prop_chem'] = True
atm_analysis['cdh_standard'] = True
atm_analysis['cdh_optim'] = True
atm_analysis['struct_stand'] = True
atm_analysis['struct_high_resist'] = True

bus_vs_mission_type.append(atm_analysis)



sample_collect = {}
sample_collect['name'] = 'Samples Collection'
sample_collect['slug'] = 'sample_collect'
sample_collect['therm_active'] = True
sample_collect['therm_passive'] = True
sample_collect['pow_prim_panels'] = True
sample_collect['pow_prim_rtg'] = True
sample_collect['pow_sec_batt'] = True
sample_collect['pow_sec_fc'] = True
sample_collect['comm_mono'] = True
sample_collect['comm_omni'] = True
sample_collect['aodcs_robust'] = True
sample_collect['aodcs_simple'] = (False, 'You have to locate precisely where you need to go')
sample_collect['prop_electr'] = True
sample_collect['prop_chem'] = True
sample_collect['cdh_standard'] = True
sample_collect['cdh_optim'] = True
sample_collect['struct_stand'] = True
sample_collect['struct_high_resist'] = True

bus_vs_mission_type.append(sample_collect)



telecom = {}
telecom['name'] = 'Telecommunications'
telecom['slug'] = 'telecom'
telecom['therm_active'] = True
telecom['therm_passive'] = True
telecom['pow_prim_panels'] = True
telecom['pow_prim_rtg'] = True
telecom['pow_sec_batt'] = True
telecom['pow_sec_fc'] = True
telecom['comm_mono'] = True
telecom['comm_omni'] = True
telecom['aodcs_robust'] = True
telecom['aodcs_simple'] = (False, 'You have to point exactly to where the signal must be sent')
telecom['prop_electr'] = True
telecom['prop_chem'] = True
telecom['cdh_standard'] = (False, 'A huge amount of data needs to be transferred')
telecom['cdh_optim'] = True
telecom['struct_stand'] = True
telecom['struct_high_resist'] = True

bus_vs_mission_type.append(telecom)
