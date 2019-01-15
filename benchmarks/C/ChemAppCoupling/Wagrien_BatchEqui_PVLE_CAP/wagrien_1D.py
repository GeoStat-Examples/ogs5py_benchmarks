# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='wagrien_1D_root',
    task_id='wagrien_1D',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 2],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=['CONSTANT', 2],
)
model.gli.read_file('wagrien_1D.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 2],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='water_liquid',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 47000.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Al[3+]',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 2.92e-10],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='CO2',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.153],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='CO3[2-]',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 7.22e-08],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Ca[2+]',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 296.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Cl[-]',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 5630.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Fe[2+]',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Fe[3+]',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='H[+]',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.00152],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='H2',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='HCO3[-]',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.00571],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='HS[-]',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='K[+]',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 34.5],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Mg[2+]',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 11.2],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Na[+]',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 5020.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='OH[-]',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 6.02e-06],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='SO4[2-]',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.000512],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='SiO2',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.107],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='AlCH2NaO5_dawsonite(s)_s',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='CO3Mg_mgco3(s)_s',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='HO2Al_alo(oh)_boehmit(s)_s',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='O2Si_sio2_quartz(s8)_s',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 23056.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='O3SiMg_mgsio3(s)_s',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='O4SiMg2_mg2sio4(s)_s',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='H4O9Al2Si2_al2si2o5((s3)_s',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='O8AlSi3Na_naalsi3o8_l(s)_s',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 733.43],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='O8AlSi3K_kalsi3o8_k-f(s)_s',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1208.6],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='H2O12Al3Si3K_kal2(als(s)_s',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 591.82],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='CO3Ca_caco3_calcite(s2)_s',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1981.5],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='C2O6CaMg_camg(co3)2(s)_s',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 426.73],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='O8Al2CaSi2_ca(al2si2)(s)_s',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='O4CaS_caso4(s)_s',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 2839.6],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='O3Fe2_fe2o3(s)_s',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='CO3Fe_feco3(s)_s',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='O4Fe2Si_fe2sio4(s)_s',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='S2Fe_fes2(s)_s',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Tracer',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='pH',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 5.0328],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='PCO2',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 95],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='water_liquid',
    MOBILE=1,
    DIFFUSION=[1, 1e-09],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Al[3+]',
    MOBILE=1,
    DIFFUSION=[1, 1e-09],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='CO2',
    MOBILE=1,
    DIFFUSION=[1, 1e-09],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='CO3[2-]',
    MOBILE=1,
    DIFFUSION=[1, 1e-09],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Ca[2+]',
    MOBILE=1,
    DIFFUSION=[1, 1e-09],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Cl[-]',
    MOBILE=1,
    DIFFUSION=[1, 1e-09],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Fe[2+]',
    MOBILE=1,
    DIFFUSION=[1, 1e-09],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Fe[3+]',
    MOBILE=1,
    DIFFUSION=[1, 1e-09],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='H[+]',
    MOBILE=1,
    DIFFUSION=[1, 1e-09],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='H2',
    MOBILE=1,
    DIFFUSION=[1, 1e-09],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='HCO3[-]',
    MOBILE=1,
    DIFFUSION=[1, 1e-09],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='HS[-]',
    MOBILE=1,
    DIFFUSION=[1, 1e-09],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='K[+]',
    MOBILE=1,
    DIFFUSION=[1, 1e-09],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Mg[2+]',
    MOBILE=1,
    DIFFUSION=[1, 1e-09],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Na[+]',
    MOBILE=1,
    DIFFUSION=[1, 1e-09],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='OH[-]',
    MOBILE=1,
    DIFFUSION=[1, 1e-09],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='SO4[2-]',
    MOBILE=1,
    DIFFUSION=[1, 1e-09],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='SiO2',
    MOBILE=1,
    DIFFUSION=[1, 1e-09],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='AlCH2NaO5_dawsonite(s)_s',
    MOBILE=0,
    TRANSPORT_PHASE=1,
    MOLAR_WEIGHT=0.144,
    MINERAL_DENSITY=2420,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='CO3Mg_mgco3(s)_s',
    MOBILE=0,
    TRANSPORT_PHASE=1,
    MOLAR_WEIGHT=0.084316,
    MINERAL_DENSITY=2980,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='HO2Al_alo(oh)_boehmit(s)_s',
    MOBILE=0,
    TRANSPORT_PHASE=1,
    MOLAR_WEIGHT=0.05999,
    MINERAL_DENSITY=3030,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='O2Si_sio2_quartz(s8)_s',
    MOBILE=0,
    TRANSPORT_PHASE=1,
    MOLAR_WEIGHT=0.060084,
    MINERAL_DENSITY=2650,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='O3SiMg_mgsio3(s)_s',
    MOBILE=0,
    TRANSPORT_PHASE=1,
    MOLAR_WEIGHT=0.100391,
    MINERAL_DENSITY=2510,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='O4SiMg2_mg2sio4(s)_s',
    MOBILE=0,
    TRANSPORT_PHASE=1,
    MOLAR_WEIGHT=0.140696,
    MINERAL_DENSITY=3220,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='H4O9Al2Si2_al2si2o5((s3)_s',
    MOBILE=0,
    TRANSPORT_PHASE=1,
    MOLAR_WEIGHT=0.258136,
    MINERAL_DENSITY=2620,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='O8AlSi3Na_naalsi3o8_l(s)_s',
    MOBILE=0,
    TRANSPORT_PHASE=1,
    MOLAR_WEIGHT=0.26224,
    MINERAL_DENSITY=2630,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='O8AlSi3K_kalsi3o8_k-f(s)_s',
    MOBILE=0,
    TRANSPORT_PHASE=1,
    MOLAR_WEIGHT=0.278338,
    MINERAL_DENSITY=2560,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='H2O12Al3Si3K_kal2(als(s)_s',
    MOBILE=0,
    TRANSPORT_PHASE=1,
    MOLAR_WEIGHT=0.39871,
    MINERAL_DENSITY=2820,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='CO3Ca_caco3_calcite(s2)_s',
    MOBILE=0,
    TRANSPORT_PHASE=1,
    MOLAR_WEIGHT=0.100089,
    MINERAL_DENSITY=2710,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='C2O6CaMg_camg(co3)2(s)_s',
    MOBILE=0,
    TRANSPORT_PHASE=1,
    MOLAR_WEIGHT=0.184405,
    MINERAL_DENSITY=2840,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='O8Al2CaSi2_ca(al2si2)(s)_s',
    MOBILE=0,
    TRANSPORT_PHASE=1,
    MOLAR_WEIGHT=0.279318,
    MINERAL_DENSITY=2730,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='O4CaS_caso4(s)_s',
    MOBILE=0,
    TRANSPORT_PHASE=1,
    MOLAR_WEIGHT=0.136138,
    MINERAL_DENSITY=2960,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='O3Fe2_fe2o3(s)_s',
    MOBILE=0,
    TRANSPORT_PHASE=1,
    MOLAR_WEIGHT=0.15969,
    MINERAL_DENSITY=5300,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='CO3Fe_feco3(s)_s',
    MOBILE=0,
    TRANSPORT_PHASE=1,
    MOLAR_WEIGHT=0.115856,
    MINERAL_DENSITY=3870,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='O4Fe2Si_fe2sio4(s)_s',
    MOBILE=0,
    TRANSPORT_PHASE=1,
    MOLAR_WEIGHT=0.203776,
    MINERAL_DENSITY=4390,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='S2Fe_fes2(s)_s',
    MOBILE=0,
    TRANSPORT_PHASE=1,
    MOLAR_WEIGHT=0.11998,
    MINERAL_DENSITY=5010,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Tracer',
    MOBILE=1,
    DIFFUSION=[1, 1e-09],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='pH',
    MOBILE=0,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='PCO2',
    MOBILE=0,
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='HEAD',
    DENSITY=[1, 1000.0],
    VISCOSITY=[1, 0.001],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=1,
    GEOMETRY_AREA=1.0,
    POROSITY=[13, 0.2],
    VOL_MAT=[1, 0.8],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1.157e-12],
    PERMEABILITY_FUNCTION_POROSITY=[8, 'Kozeny_Carman'],
    MASS_DISPERSION=[1, 0.001, 0.0],
    HEAT_DISPERSION=[1, 0.0, 0.0],
    DENSITY=[1, 1800.0],
)
model.msh.read_file('wagrien_1D.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 1800.0],
    THERMAL=[
        ['EXPANSION'],
        [1e-05],
        ['CAPACITY'],
        [1, 1000.0],
        ['CONDUCTIVITY'],
        [1, 0.1],
    ],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='GROUNDWATER_FLOW',
    ELE_GAUSS_POINTS=3,
    LINEAR_SOLVER=[2, 6, 1e-14, 1000, 1.0, 1, 2],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='MASS_TRANSPORT',
    LINEAR_SOLVER=[2, 6, 1e-14, 1000, 0.5, 1, 2],
    ELE_GAUSS_POINTS=3,
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['HEAD'],
        ['water_liquid'],
        ['Al[3+]'],
        ['CO2'],
        ['CO3[2-]'],
        ['Ca[2+]'],
        ['Cl[-]'],
        ['Fe[2+]'],
        ['Fe[3+]'],
        ['H[+]'],
        ['H2'],
        ['HCO3[-]'],
        ['HS[-]'],
        ['K[+]'],
        ['Mg[2+]'],
        ['Na[+]'],
        ['OH[-]'],
        ['SO4[2-]'],
        ['SiO2'],
        ['AlCH2NaO5_dawsonite(s)_s'],
        ['CO3Mg_mgco3(s)_s'],
        ['HO2Al_alo(oh)_boehmit(s)_s'],
        ['O2Si_sio2_quartz(s8)_s'],
        ['O3SiMg_mgsio3(s)_s'],
        ['O4SiMg2_mg2sio4(s)_s'],
        ['H4O9Al2Si2_al2si2o5((s3)_s'],
        ['O8AlSi3Na_naalsi3o8_l(s)_s'],
        ['O8AlSi3K_kalsi3o8_k-f(s)_s'],
        ['H2O12Al3Si3K_kal2(als(s)_s'],
        ['CO3Ca_caco3_calcite(s2)_s'],
        ['C2O6CaMg_camg(co3)2(s)_s'],
        ['O8Al2CaSi2_ca(al2si2)(s)_s'],
        ['O4CaS_caso4(s)_s'],
        ['O3Fe2_fe2o3(s)_s'],
        ['CO3Fe_feco3(s)_s'],
        ['O4Fe2Si_fe2sio4(s)_s'],
        ['S2Fe_fes2(s)_s'],
        ['pH'],
    ],
    GEO_TYPE=['POLYLINE', 'OUT_LINE'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 10],
)
model.out.add_block(
    main_key='OUTPUT',
    ELE_VALUES=[
        ['VELOCITY1_X'],
        ['POROSITY'],
        ['PERMEABILITY'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 10],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='GROUNDWATER_FLOW',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.rei.add_block(
    main_key='REACTION_INTERFACE',
    MOL_PER='VOLUME',
    WATER_CONCENTRATION=[
        ['VARIABLE'],
        ['Al[3+]'],
        ['CO3[2-]'],
        ['Ca[2+]'],
        ['Cl[-]'],
        ['Fe[2+]'],
        ['Fe[3+]'],
        ['H[+]'],
        ['HCO3[-]'],
        ['HS[-]'],
        ['K[+]'],
        ['Mg[2+]'],
        ['Na[+]'],
        ['OH[-]'],
        ['SO4[2-]'],
    ],
    WATER_SPECIES_NAME='water_liquid',
    DISSOLVED_NEUTRAL_CO2_SPECIES_NAME='CO2',
    PRESSURE=['CONSTANT', 305.87],
    TEMPERATURE=['CONSTANT', 367.15],
    RESIDUAL='RECORD',
    P_VLE=['PCO2', 'CO2'],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='GROUNDWATER_FLOW',
    TIME_STEPS=[10, 86400],
    TIME_END=315360000000.0,
    TIME_START=0.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MASS_TRANSPORT',
    TIME_STEPS=[10, 86400],
    TIME_END=315360000000.0,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
