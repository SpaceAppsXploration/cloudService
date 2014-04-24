# True/False Tables about mission's possible bus components

bus_vs_bus = []

aodcs_robust = {}
aodcs_robust['name'] = 'AODCS Robust'
aodcs_robust['slug'] = 'aodcs_robust'
aodcs_robust['therm_active'] = False
aodcs_robust['therm_passive'] = True
aodcs_robust['pow_prim_panels'] = True
aodcs_robust['pow_prim_rtg'] = True
aodcs_robust['pow_sec_batt'] = True
aodcs_robust['pow_sec_fc'] = True
aodcs_robust['comm_mono'] = True
aodcs_robust['comm_omni'] = True
aodcs_robust['aodcs_robust'] = True
aodcs_robust['aodcs_simple'] = False
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
aodcs_simple['therm_passive'] = False
aodcs_simple['pow_prim_panels'] = False
aodcs_simple['pow_prim_rtg'] = True
aodcs_simple['pow_sec_batt'] = True
aodcs_simple['pow_sec_fc'] = True
aodcs_simple['comm_mono'] = False
aodcs_simple['comm_omni'] = True
aodcs_simple['aodcs_robust'] = False
aodcs_simple['aodcs_simple'] = True
aodcs_simple['prop_electr'] = True
aodcs_simple['prop_chem'] = False
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
prop_elect['pow_sec_fc'] = False
prop_elect['comm_mono'] = True
prop_elect['comm_omni'] = True
prop_elect['aodcs_robust'] = True
prop_elect['aodcs_simple'] = True
prop_elect['prop_electr'] = True
prop_elect['prop_chem'] = False
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
prop_chem['aodcs_simple'] = False
prop_chem['prop_electr'] = False
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
cdh_standard['comm_omni'] = False
cdh_standard['aodcs_robust'] = True
cdh_standard['aodcs_simple'] = True
cdh_standard['prop_electr'] = True
cdh_standard['prop_chem'] = True
cdh_standard['cdh_standard'] = True
cdh_standard['cdh_optim'] = False
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
cdh_optim['cdh_standard'] = False
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
struct_stand['pow_prim_rtg'] = False
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
struct_stand['struct_high_resist'] = False

bus_vs_bus.append(struct_stand)


struct_high_resist = {}
struct_high_resist['name'] = 'Standard Structure'
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
struct_high_resist['struct_stand'] = False
struct_high_resist['struct_high_resist'] = True

bus_vs_bus.append(struct_high_resist)