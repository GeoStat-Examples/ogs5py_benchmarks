# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='ab1d_root',
    task_id='ab1d',
    output_dir='out',
)
model.msh.read_file('ab1d.msh')
model.gli.read_file('ab1d.gli')
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='GROUNDWATER_FLOW',
    NUM_TYPE='NEW',
    ELEMENT_MATRIX_OUTPUT=0,
    RELOAD=[2, 1],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    ELEMENT_MATRIX_OUTPUT=0,
    RELOAD=[2, 1],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    ELEMENT_MATRIX_OUTPUT=0,
    RELOAD=[2, 1],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    ELEMENT_MATRIX_OUTPUT=0,
    RELOAD=[2, 1],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    ELEMENT_MATRIX_OUTPUT=0,
    RELOAD=[2, 1],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    ELEMENT_MATRIX_OUTPUT=0,
    RELOAD=[2, 1],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    ELEMENT_MATRIX_OUTPUT=0,
    RELOAD=[2, 1],
)
model.rfd.read_file('ab1d.rfd')
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 10.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=['CONSTANT', 10.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='1-Ael',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 1.0],
    TIM_TYPE=['CURVE', 1],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='2-Bel',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 1.0],
    TIM_TYPE=['CURVE', 2],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='3-H',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 0.000199450916354453],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='4-Inrt',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='5-O',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 0.0100997255469342],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='6-Zz',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='1-Ael',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=['CONSTANT', 1.0],
    TIM_TYPE=['CURVE', 3],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='2-Bel',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=['CONSTANT', 1.0],
    TIM_TYPE=['CURVE', 4],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='3-H',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=['CONSTANT', 0.000199449988669848],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='4-Inrt',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='5-O',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=['CONSTANT', 0.0100997250739968],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='6-Zz',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 10.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='6-Zz',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=1,
    GEOMETRY_AREA=1.0,
    POROSITY=[15, 1.0],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1.157e-06],
    MASS_DISPERSION=[1, 0.0067, 0.00067],
    DENSITY=[1, 1800.0],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 1800.0],
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
    NAME='1-Ael',
    MOBILE=1,
    DIFFUSION=[9, 1e-10, 1.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='2-Bel',
    MOBILE=1,
    DIFFUSION=[9, 1e-10, 1.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='3-H',
    MOBILE=1,
    DIFFUSION=[9, 1e-10, 1.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='4-Inrt',
    MOBILE=1,
    DIFFUSION=[9, 1e-10, 1.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='5-O',
    MOBILE=1,
    DIFFUSION=[9, 1e-10, 1.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='6-Zz',
    MOBILE=1,
    DIFFUSION=[9, 1e-10, 1.0],
)
model.gem.add_block(
    main_key='GEM_PROPERTIES',
    GEM_THREADS=1,
    GEM_INIT_FILE='TestSolub-dat.lst',
    FLAG_CALCULATE_BOUNDARY_NODE=1,
    FLAG_POROSITY_CHANGE=1,
    MIN_POROSITY=1e-15,
    MAX_POROSITY=1.0,
    FLAG_COUPLING_HYDROLOGY=0,
    TEMPERATURE_GEM=298.15,
    TRANSPORT_B=1,
    KINETIC_GEM=[
        ['AB-solid', 1, 1, 0.0, 0.0, 0.0, 0.0, -7.69897, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 'H+', 0.0, 0.0, 0.0],
        [4, 10000.0],
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
    LINEAR_SOLVER=[2, 6, 1e-14, 1000, 1.0, 1, 2],
    ELE_GAUSS_POINTS=3,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='GROUNDWATER_FLOW',
    TIME_STEPS=[100000, 100.0],
    TIME_END=10000.0,
    TIME_START=0.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MASS_TRANSPORT',
    TIME_STEPS=[100000, 100.0],
    TIME_END=10000.0,
    TIME_START=0.0,
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['HEAD'],
        ['1-Ael'],
        ['2-Bel'],
        ['3-H'],
        ['4-Inrt'],
        ['5-O'],
        ['6-Zz'],
    ],
    ELE_VALUES=[
        ['POROSITY'],
        ['VELOCITY_X'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='VTK',
    TIM_TYPE=['STEPS', 10],
)
model.gem_init.add(
    name='TestSolub-dat',
    file_ext='.lst',
)
model.gem_init.read_file('TestSolub-dat.lst')
model.asc.add(
    name='ab1d_MASS_TRANSPORT_6-Zz_primary_value',
    file_ext='.asc',
)
model.asc.read_file('ab1d_MASS_TRANSPORT_6-Zz_primary_value.asc')
model.asc.add(
    name='ab1d_MASS_TRANSPORT_5-O_primary_value',
    file_ext='.asc',
)
model.asc.read_file('ab1d_MASS_TRANSPORT_5-O_primary_value.asc')
model.asc.add(
    name='ab1d_m_xDC_gem',
    file_ext='.asc',
)
model.asc.read_file('ab1d_m_xDC_gem.asc')
model.asc.add(
    name='ab1d_m_porosity_gem',
    file_ext='.asc',
)
model.asc.read_file('ab1d_m_porosity_gem.asc')
model.asc.add(
    name='ab1d_MASS_TRANSPORT_3-H_primary_value',
    file_ext='.asc',
)
model.asc.read_file('ab1d_MASS_TRANSPORT_3-H_primary_value.asc')
model.asc.add(
    name='ab1d_m_bIC_gem',
    file_ext='.asc',
)
model.asc.read_file('ab1d_m_bIC_gem.asc')
model.asc.add(
    name='ab1d_m_fluid_volume_gem',
    file_ext='.asc',
)
model.asc.read_file('ab1d_m_fluid_volume_gem.asc')
model.asc.add(
    name='ab1d_MASS_TRANSPORT_1-Ael_primary_value',
    file_ext='.asc',
)
model.asc.read_file('ab1d_MASS_TRANSPORT_1-Ael_primary_value.asc')
model.asc.add(
    name='ab1d_MASS_TRANSPORT_4-Inrt_primary_value',
    file_ext='.asc',
)
model.asc.read_file('ab1d_MASS_TRANSPORT_4-Inrt_primary_value.asc')
model.asc.add(
    name='ab1d_GROUNDWATER_FLOW_HEAD_primary_value',
    file_ext='.asc',
)
model.asc.read_file('ab1d_GROUNDWATER_FLOW_HEAD_primary_value.asc')
model.asc.add(
    name='ab1d_MASS_TRANSPORT_2-Bel_primary_value',
    file_ext='.asc',
)
model.asc.read_file('ab1d_MASS_TRANSPORT_2-Bel_primary_value.asc')
model.asc.add(
    name='ab1d_time_gem',
    file_ext='.asc',
)
model.asc.read_file('ab1d_time_gem.asc')
model.write_input()
model.run_model()
