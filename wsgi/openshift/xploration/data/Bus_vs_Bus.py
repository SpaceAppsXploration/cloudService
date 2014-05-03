# True/False Tables about mission's possible bus components

bus_vs_bus = []

therm_active = {}
therm_active['name'] = 'Thermal Active'
therm_active['slug'] = 'therm_active'
therm_active['therm_active'] = True
therm_active['therm_passive'] = True
therm_active['pow_prim_panels'] = True
therm_active['pow_prim_rtg'] = True
therm_active['pow_sec_batt'] = True
therm_active['pow_sec_fc'] = True
therm_active['comm_mono'] = True
therm_active['comm_omni'] = True
therm_active['aodcs_robust'] = True
therm_active['aodcs_simple'] = True
therm_active['prop_electr'] = True
therm_active['prop_chem'] = True
therm_active['cdh_standard'] = True
therm_active['cdh_optim'] = True
therm_active['struct_stand'] = True
therm_active['struct_high_resist'] = True

bus_vs_bus.append(therm_active)

therm_passive = {}
therm_passive['name'] = 'Thermal Passive'
therm_passive['slug'] = 'therm_passive'
therm_passive['therm_active'] = True
therm_passive['therm_passive'] = True
therm_passive['pow_prim_panels'] = True
therm_passive['pow_prim_rtg'] = True
therm_passive['pow_sec_batt'] = True
therm_passive['pow_sec_fc'] = True
therm_passive['comm_mono'] = True
therm_passive['comm_omni'] = True
therm_passive['aodcs_robust'] = True
therm_passive['aodcs_simple'] = (False, 'If you want a passive thermal control, you have to precisely control the attitude')
therm_passive['prop_electr'] = True
therm_passive['prop_chem'] = True
therm_passive['cdh_standard'] = True
therm_passive['cdh_optim'] = True
therm_passive['struct_stand'] = True
therm_passive['struct_high_resist'] = True

bus_vs_bus.append(therm_passive)


pow_prim_panels = {}
pow_prim_panels['name'] = 'Primary Power Solar Arrays'
pow_prim_panels['slug'] = 'pow_prim_panels'
pow_prim_panels['therm_active'] = True
pow_prim_panels['therm_passive'] = True
pow_prim_panels['pow_prim_panels'] = True
pow_prim_panels['pow_prim_rtg'] = True
pow_prim_panels['pow_sec_batt'] = True
pow_prim_panels['pow_sec_fc'] = True
pow_prim_panels['comm_mono'] = True
pow_prim_panels['comm_omni'] = True
pow_prim_panels['aodcs_robust'] = True
pow_prim_panels['aodcs_simple'] = (False, 'If you want to maximize the power output of solar arrays, you have to precisely control the attitude')
pow_prim_panels['prop_electr'] = True
pow_prim_panels['prop_chem'] = True
pow_prim_panels['cdh_standard'] = True
pow_prim_panels['cdh_optim'] = True
pow_prim_panels['struct_stand'] = True
pow_prim_panels['struct_high_resist'] = True

bus_vs_bus.append(pow_prim_panels)

pow_prim_rtg = {}
pow_prim_rtg['name'] = 'Primary Power RTG'
pow_prim_rtg['slug'] = 'pow_prim_rtg'
pow_prim_rtg['therm_active'] = True
pow_prim_rtg['therm_passive'] = True
pow_prim_rtg['pow_prim_panels'] = True
pow_prim_rtg['pow_prim_rtg'] = True
pow_prim_rtg['pow_sec_batt'] = True
pow_prim_rtg['pow_sec_fc'] = True
pow_prim_rtg['comm_mono'] = True
pow_prim_rtg['comm_omni'] = True
pow_prim_rtg['aodcs_robust'] = True
pow_prim_rtg['aodcs_simple'] = True
pow_prim_rtg['prop_electr'] = True
pow_prim_rtg['prop_chem'] = True
pow_prim_rtg['cdh_standard'] = True
pow_prim_rtg['cdh_optim'] = True
pow_prim_rtg['struct_stand'] = (False, 'Maybe it is better to account for radiation shielding')
pow_prim_rtg['struct_high_resist'] = True

bus_vs_bus.append(pow_prim_rtg)


pow_sec_batt = {}
pow_sec_batt['name'] = 'Backup Power Batteries'
pow_sec_batt['slug'] = 'pow_sec_batt'
pow_sec_batt['therm_active'] = True
pow_sec_batt['therm_passive'] = True
pow_sec_batt['pow_prim_panels'] = True
pow_sec_batt['pow_prim_rtg'] = True
pow_sec_batt['pow_sec_batt'] = True
pow_sec_batt['pow_sec_fc'] = True
pow_sec_batt['comm_mono'] = True
pow_sec_batt['comm_omni'] = True
pow_sec_batt['aodcs_robust'] = True
pow_sec_batt['aodcs_simple'] = True
pow_sec_batt['prop_electr'] = True
pow_sec_batt['prop_chem'] = True
pow_sec_batt['cdh_standard'] = True
pow_sec_batt['cdh_optim'] = True
pow_sec_batt['struct_stand'] = True
pow_sec_batt['struct_high_resist'] = True

bus_vs_bus.append(pow_sec_batt)


pow_sec_fc = {}
pow_sec_fc['name'] = 'Backup Power Fuel Cells'
pow_sec_fc['slug'] = 'pow_sec_fc'
pow_sec_fc['therm_active'] = True
pow_sec_fc['therm_passive'] = True
pow_sec_fc['pow_prim_panels'] = True
pow_sec_fc['pow_prim_rtg'] = True
pow_sec_fc['pow_sec_batt'] = True
pow_sec_fc['pow_sec_fc'] = True
pow_sec_fc['comm_mono'] = True
pow_sec_fc['comm_omni'] = True
pow_sec_fc['aodcs_robust'] = True
pow_sec_fc['aodcs_simple'] = True
pow_sec_fc['prop_electr'] = True
pow_sec_fc['prop_chem'] = True
pow_sec_fc['cdh_standard'] = True
pow_sec_fc['cdh_optim'] = True
pow_sec_fc['struct_stand'] = True
pow_sec_fc['struct_high_resist'] = True

bus_vs_bus.append(pow_sec_fc)


comm_mono = {}
comm_mono['name'] = 'Communication Monodirectional Atenna'
comm_mono['slug'] = 'comm_mono'
comm_mono['therm_active'] = True
comm_mono['therm_passive'] = True
comm_mono['pow_prim_panels'] = True
comm_mono['pow_prim_rtg'] = True
comm_mono['pow_sec_batt'] = True
comm_mono['pow_sec_fc'] = True
comm_mono['comm_mono'] = True
comm_mono['comm_omni'] = (False, 'Pick one!')
comm_mono['aodcs_robust'] = True
comm_mono['aodcs_simple'] = (False, 'A simple AODCS cannot guarantee an optimal pointing setup')
comm_mono['prop_electr'] = True
comm_mono['prop_chem'] = True
comm_mono['cdh_standard'] = True
comm_mono['cdh_optim'] = True
comm_mono['struct_stand'] = True
comm_mono['struct_high_resist'] = True

bus_vs_bus.append(comm_mono)


comm_omni = {}
comm_omni['name'] = 'Communication Omnidirectional Atenna'
comm_omni['slug'] = 'comm_omni'
comm_omni['therm_active'] = True
comm_omni['therm_passive'] = True
comm_omni['pow_prim_panels'] = True
comm_omni['pow_prim_rtg'] = True
comm_omni['pow_sec_batt'] = True
comm_omni['pow_sec_fc'] = True
comm_omni['comm_mono'] = (False, 'Pick one!')
comm_omni['comm_omni'] = True
comm_omni['aodcs_robust'] = True
comm_omni['aodcs_simple'] = True
comm_omni['prop_electr'] = True
comm_omni['prop_chem'] = True
comm_omni['cdh_standard'] = True
comm_omni['cdh_optim'] = True
comm_omni['struct_stand'] = True
comm_omni['struct_high_resist'] = True

bus_vs_bus.append(comm_omni)

aodcs_robust = {}
aodcs_robust['name'] = 'AODCS Robust'
aodcs_robust['slug'] = 'aodcs_robust'
aodcs_robust['therm_active'] = True
aodcs_robust['therm_passive'] = True
aodcs_robust['pow_prim_panels'] = True
aodcs_robust['pow_prim_rtg'] = True
aodcs_robust['pow_sec_batt'] = True
aodcs_robust['pow_sec_fc'] = True
aodcs_robust['comm_mono'] = True
aodcs_robust['comm_omni'] = True
aodcs_robust['aodcs_robust'] = True
aodcs_robust['aodcs_simple'] = (False, 'Pick one!')
aodcs_robust['prop_electr'] = True
aodcs_robust['prop_chem'] = True
aodcs_robust['cdh_standard'] = True
aodcs_robust['cdh_optim'] = True
aodcs_robust['struct_stand'] = True
aodcs_robust['struct_high_resist'] = True

bus_vs_bus.append(aodcs_robust)


aodcs_simple = {}
aodcs_simple['name'] = 'AODCS Simple'
aodcs_simple['slug'] = 'aodcs_simple'
aodcs_simple['therm_active'] = True
aodcs_simple['therm_passive'] = (False, 'If you want a passive thermal control, you have to precisely control the attitude')
aodcs_simple['pow_prim_panels'] = (False, 'If you want to maximize the power output of solar arrays, you have to precisely control the attitude')
aodcs_simple['pow_prim_rtg'] = True
aodcs_simple['pow_sec_batt'] = True
aodcs_simple['pow_sec_fc'] = True
aodcs_simple['comm_mono'] = (False, 'A simple AODCS cannot guarantee an optimal pointing setup')
aodcs_simple['comm_omni'] = True
aodcs_simple['aodcs_robust'] = (False, ' Pick one!')
aodcs_simple['aodcs_simple'] = True
aodcs_simple['prop_electr'] = True
aodcs_simple['prop_chem'] = (False, 'Since chemical rockets burn for a short time, you need to precisely control the thrust direction if you want to enter the right trajectory')
aodcs_simple['cdh_standard'] = True
aodcs_simple['cdh_optim'] = True
aodcs_simple['struct_stand'] = True
aodcs_simple['struct_high_resist'] = True

bus_vs_bus.append(aodcs_simple)



prop_elect = {}
prop_elect['name'] = 'Electric Propulsion'
prop_elect['slug'] = 'prop_elect'
prop_elect['therm_active'] = True
prop_elect['therm_passive'] = True
prop_elect['pow_prim_panels'] = True
prop_elect['pow_prim_rtg'] = True
prop_elect['pow_sec_batt'] = True
prop_elect['pow_sec_fc'] = True
prop_elect['comm_mono'] = True
prop_elect['comm_omni'] = True
prop_elect['aodcs_robust'] = True
prop_elect['aodcs_simple'] = True
prop_elect['prop_electr'] = True
prop_elect['prop_chem'] = (False, 'Pick one!')
prop_elect['cdh_standard'] = True
prop_elect['cdh_optim'] = True
prop_elect['struct_stand'] = True
prop_elect['struct_high_resist'] = True

bus_vs_bus.append(prop_elect)



prop_chem = {}
prop_chem['name'] = 'Chemical Propulsion'
prop_chem['slug'] = 'prop_chem'
prop_chem['therm_active'] = True
prop_chem['therm_passive'] = True
prop_chem['pow_prim_panels'] = True
prop_chem['pow_prim_rtg'] = True
prop_chem['pow_sec_batt'] = True
prop_chem['pow_sec_fc'] = True
prop_chem['comm_mono'] = True
prop_chem['comm_omni'] = True
prop_chem['aodcs_robust'] = True
prop_chem['aodcs_simple'] = (False, 'Since chemical rockets burn for a short time, you need to precisely control the thrust direction if you want to enter the right trajectory')
prop_chem['prop_electr'] = (False, 'Pick one!')
prop_chem['prop_chem'] = True
prop_chem['cdh_standard'] = True
prop_chem['cdh_optim'] = True
prop_chem['struct_stand'] = True
prop_chem['struct_high_resist'] = True

bus_vs_bus.append(prop_chem)



cdh_standard = {}
cdh_standard['name'] = 'CDH Standard'
cdh_standard['slug'] = 'cdh_standard'
cdh_standard['therm_active'] = True
cdh_standard['therm_passive'] = True
cdh_standard['pow_prim_panels'] = True
cdh_standard['pow_prim_rtg'] = True
cdh_standard['pow_sec_batt'] = True
cdh_standard['pow_sec_fc'] = True
cdh_standard['comm_mono'] = True
cdh_standard['comm_omni'] = True
cdh_standard['aodcs_robust'] = True
cdh_standard['aodcs_simple'] = True
cdh_standard['prop_electr'] = True
cdh_standard['prop_chem'] = True
cdh_standard['cdh_standard'] = True
cdh_standard['cdh_optim'] = (False, 'Pick one!')
cdh_standard['struct_stand'] = True
cdh_standard['struct_high_resist'] = True

bus_vs_bus.append(cdh_standard)



cdh_optim = {}
cdh_optim['name'] = 'CDH Optimized'
cdh_optim['slug'] = 'cdh_optim'
cdh_optim['therm_active'] = True
cdh_optim['therm_passive'] = True
cdh_optim['pow_prim_panels'] = True
cdh_optim['pow_prim_rtg'] = True
cdh_optim['pow_sec_batt'] = True
cdh_optim['pow_sec_fc'] = True
cdh_optim['comm_mono'] = True
cdh_optim['comm_omni'] = True
cdh_optim['aodcs_robust'] = True
cdh_optim['aodcs_simple'] = True
cdh_optim['prop_electr'] = True
cdh_optim['prop_chem'] = True
cdh_optim['cdh_standard'] = (False, 'Pick one!')
cdh_optim['cdh_optim'] = True
cdh_optim['struct_stand'] = True
cdh_optim['struct_high_resist'] = True

bus_vs_bus.append(cdh_optim)



struct_stand = {}
struct_stand['name'] = 'Standard Structure'
struct_stand['slug'] = 'struct_stand'
struct_stand['therm_active'] = True
struct_stand['therm_passive'] = True
struct_stand['pow_prim_panels'] = True
struct_stand['pow_prim_rtg'] = (False, 'Maybe it is better to account for radiation shielding')
struct_stand['pow_sec_batt'] = True
struct_stand['pow_sec_fc'] = True
struct_stand['comm_mono'] = True
struct_stand['comm_omni'] = True
struct_stand['aodcs_robust'] = True
struct_stand['aodcs_simple'] = True
struct_stand['prop_electr'] = True
struct_stand['prop_chem'] = True
struct_stand['cdh_standard'] = True
struct_stand['cdh_optim'] = True
struct_stand['struct_stand'] = True
struct_stand['struct_high_resist'] = (False, 'Pick one!')

bus_vs_bus.append(struct_stand)


struct_high_resist = {}
struct_high_resist['name'] = 'High Resistance Structure'
struct_high_resist['slug'] = 'struct_high_resist'
struct_high_resist['therm_active'] = True
struct_high_resist['therm_passive'] = True
struct_high_resist['pow_prim_panels'] = True
struct_high_resist['pow_prim_rtg'] = True
struct_high_resist['pow_sec_batt'] = True
struct_high_resist['pow_sec_fc'] = True
struct_high_resist['comm_mono'] = True
struct_high_resist['comm_omni'] = True
struct_high_resist['aodcs_robust'] = True
struct_high_resist['aodcs_simple'] = True
struct_high_resist['prop_electr'] = True
struct_high_resist['prop_chem'] = True
struct_high_resist['cdh_standard'] = True
struct_high_resist['cdh_optim'] = True
struct_high_resist['struct_stand'] = (False, 'Pick one!')
struct_high_resist['struct_high_resist'] = True

bus_vs_bus.append(struct_high_resist)
