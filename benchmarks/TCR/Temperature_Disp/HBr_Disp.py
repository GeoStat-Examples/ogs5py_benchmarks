# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='HBr_Disp_root',
    task_id='HBr_Disp',
    output_dir='out',
)
model.msh.read_file('HBr_Disp.msh')
model.gli.read_file('HBr_Disp.gli')
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='GROUNDWATER_FLOW',
    BOUNDARY_CONDITION_OUTPUT=[],
    TIM_TYPE='STEADY',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    MEMORY_TYPE=1,
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='HEAT_TRANSPORT',
    TEMPERATURE_UNIT='KELVIN',
    MEMORY_TYPE=1,
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POLYLINE', 'PLY_BC_LEFT'],
    DIS_TYPE=['CONSTANT', 1.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POLYLINE', 'PLY_BC_RIGHT'],
    DIS_TYPE=['CONSTANT', 0.9984987745],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['POLYLINE', 'PLY_BC_LEFT'],
    DIS_TYPE=['CONSTANT', 283.15],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['POLYLINE', 'PLY_BC_RIGHT'],
    DIS_TYPE=['CONSTANT', 283.15],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='TRACER',
    GEO_TYPE=['POLYLINE', 'PLY_BC_LEFT_oben'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='TRACER',
    GEO_TYPE=['POLYLINE', 'PLY_BC_LEFT_unten'],
    DIS_TYPE=['CONSTANT', 1.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='TRACER',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-10],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 283.15],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.45],
    TORTUOSITY=[1, 0.45],
    STORAGE=[1, 0.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 0.0017],
    DENSITY=[1, 2650.0],
    MASS_DISPERSION=[1, 0.0001, 0.00023951],
    HEAT_DISPERSION=[1, 1.0, 1.0],
    COMPOUND_DEPENDENT_DT=[1, 0.00025, 5e-05, 0.5],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2650.0],
    THERMAL=[
        ['EXPANSION:'],
        [1e-05],
        ['CAPACITY:'],
        [1, 1000],
        ['CONDUCTIVITY'],
        [1, 3.2],
    ],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='HEAD',
    DENSITY=[1, 999.7],
    VISCOSITY=[1, 0.0013],
    THERMAL=[
        ['CAPACITY'],
        [1, 0.004192],
        ['CONDUCTIVITY'],
        [1, 0.587],
    ],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='TRACER',
    MOBILE=1,
    DIFFUSION=[10, -0.88166, -1079.3],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='GROUNDWATER_FLOW',
    ELE_GAUSS_POINTS=3,
    LINEAR_SOLVER=[2, 6, 1e-10, 10000, 1.0, 1, 2],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='MASS_TRANSPORT',
    ELE_GAUSS_POINTS=3,
    LINEAR_SOLVER=[2, 6, 1e-10, 10000, 0.5, 1, 2],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='HEAT_TRANSPORT',
    ELE_GAUSS_POINTS=3,
    LINEAR_SOLVER=[2, 6, 1e-10, 10000, 1.0, 1, 2],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='GROUNDWATER_FLOW',
    TIME_STEPS=[300, 172.8],
    TIME_END=8.64e+39,
    TIME_START=0.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MASS_TRANSPORT',
    TIME_STEPS=[300, 172.8],
    TIME_END=8.64e+39,
    TIME_START=0.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='HEAT_TRANSPORT',
    TIME_STEPS=[300, 172.8],
    TIME_END=8.64e+39,
    TIME_START=0.0,
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['HEAD'],
        ['TRACER'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        ['STEPS'],
        [50],
    ],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['HEAD'],
        ['TRACER'],
        ['TEMPERATURE1'],
    ],
    GEO_TYPE=['POLYLINE', 'PLY_BC_RIGHT'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 50],
)
model.write_input()
model.run_model()
