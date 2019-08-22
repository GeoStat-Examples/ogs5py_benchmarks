# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='1d_isofrac_root',
    task_id='1d_isofrac',
    output_dir='out',
)
model.msh.read_file('1d_isofrac.msh')
model.gli.read_file('1d_isofrac.gli')
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
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT:', 100.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=['CONSTANT:', 97.81],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='pH',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 7.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='pe',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 4.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Pce_l',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT:', 0.00098921763658],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Pce_h',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT:', 1.0782363425e-05],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Tce_l',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT:', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Tce_h',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT:', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Dce_l',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT:', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Dce_h',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT:', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Vc_l',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT:', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Vc_h',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT:', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Eth_l',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT:', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Eth_h',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT:', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Chl',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT:', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 100.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='pH',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 9.91],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='pe',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 4.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Pce_l',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-12],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Pce_h',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-12],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Tce_l',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-12],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Tce_h',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-12],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Dce_l',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-12],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Dce_h',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-12],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Vc_l',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-12],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Vc_h',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-12],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Eth_l',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-12],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Eth_h',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-12],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Chl',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-12],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POINT:', 'POINT1'],
    DIS_TYPE=['CONSTANT', 0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.25],
    VOL_MAT=[1, 0.74],
    VOL_BIO=[1, 0.01],
    TORTUOSITY=[1, 1.0],
    STORAGE=[1, 0.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 0.000115741],
    MASS_DISPERSION=[1, 1.0, 1e-10],
    DENSITY=[1, 2650.0],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2.65],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='HEAD',
    DENSITY=[1, 1000.0],
    VISCOSITY=[1, 0.001],
    HEAT_CAPACITY=[1, 0.0],
    HEAT_CONDUCTIVITY=[1, 0.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='pH',
    MOBILE=0,
    DIFFUSION=0,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='pe',
    MOBILE=0,
    DIFFUSION=0,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Pce_l',
    MOBILE=1,
    DIFFUSION=[1, 3.0093e-10],
    TRANSPORT_PHASE=0,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Pce_h',
    MOBILE=1,
    DIFFUSION=[1, 3.0093e-10],
    TRANSPORT_PHASE=0,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Tce_l',
    MOBILE=1,
    DIFFUSION=[1, 3.0093e-10],
    TRANSPORT_PHASE=0,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Tce_h',
    MOBILE=1,
    DIFFUSION=[1, 3.0093e-10],
    TRANSPORT_PHASE=0,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Dce_l',
    MOBILE=1,
    DIFFUSION=[1, 3.0093e-10],
    TRANSPORT_PHASE=0,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Dce_h',
    MOBILE=1,
    DIFFUSION=[1, 3.0093e-10],
    TRANSPORT_PHASE=0,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Vc_l',
    MOBILE=1,
    DIFFUSION=[1, 3.0093e-10],
    TRANSPORT_PHASE=0,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Vc_h',
    MOBILE=1,
    DIFFUSION=[1, 3.0093e-10],
    TRANSPORT_PHASE=0,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Eth_l',
    MOBILE=1,
    DIFFUSION=[1, 3.0093e-10],
    TRANSPORT_PHASE=0,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Eth_h',
    MOBILE=1,
    DIFFUSION=[1, 3.0093e-10],
    TRANSPORT_PHASE=0,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Chl',
    MOBILE=1,
    DIFFUSION=[1, 3.0093e-10],
    TRANSPORT_PHASE=0,
)
model.pqc.read_file('1d_isofrac.pqc')
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
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='GROUNDWATER_FLOW',
    TIME_STEPS=[200, 3153600],
    TIME_END=6307200000,
    TIME_START=0.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MASS_TRANSPORT',
    TIME_STEPS=[200, 3153600],
    TIME_END=6307200000,
    TIME_START=0.0,
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['HEAD'],
        ['Pce_l'],
        ['Pce_h'],
        ['Tce_l'],
        ['Tce_h'],
        ['Dce_l'],
        ['Dce_h'],
        ['Vc_l'],
        ['Vc_h'],
        ['Eth_l'],
        ['Eth_h'],
        ['Chl'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 20],
)
model.pqcdat.read_file('phreeqc.dat')
model.write_input()
model.run_model()
