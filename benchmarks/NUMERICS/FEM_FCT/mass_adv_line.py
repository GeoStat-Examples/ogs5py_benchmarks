# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='mass_adv_line_root',
    task_id='mass_adv_line',
    output_dir='out',
)
model.msh.read_file('mass_adv_line.msh')
model.gli.read_file('mass_adv_line.gli')
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='LIQUID_FLOW',
    TIM_TYPE='STEADY',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    MEMORY_TYPE=1,
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=['CONSTANT', 100000],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='CONCENTRATION0',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='CONCENTRATION0',
    GEO_TYPE=['POLYLINE', 'PLY_1'],
    DIS_TYPE=['CONSTANT', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT_NEUMANN', 1],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=1,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 1.0],
    STORAGE=[1, 0.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-15],
    TORTUOSITY=[1, 1.0],
    MASS_DISPERSION=[1, 0, 0],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2650],
    THERMAL=[
        ['EXPANSION:'],
        [1e-05],
        ['CAPACITY:'],
        [1, 1000],
        ['CONDUCTIVITY:'],
        [1, 3.0],
    ],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='HEAD',
    DENSITY=[1, 1000.0],
    VISCOSITY=[1, 0.0003],
    SPECIFIC_HEAT_CAPACITY=[1, 4000],
    HEAT_CONDUCTIVITY=[1, 0.6],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='CONCENTRATION0',
    MOBILE=1,
    DIFFUSION=[1, 0.0],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='LIQUID_FLOW',
    LINEAR_SOLVER=[2, 2, 1e-15, 1000, 1.0, 100, 4],
    ELE_GAUSS_POINTS=2,
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='MASS_TRANSPORT',
    LINEAR_SOLVER=[2, 2, 1e-15, 1000, 1.0, 100, 4],
    FEM_FCT=[1, 0],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='LIQUID_FLOW',
    TIME_STEPS=[100, 0.001],
    TIME_END=0.5,
    TIME_START=0,
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES='CONCENTRATION0',
    GEO_TYPE=['POLYLINE', 'PLY_0'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 10],
)
model.write_input()
model.run_model()
