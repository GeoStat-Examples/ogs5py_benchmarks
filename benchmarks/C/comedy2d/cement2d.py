# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='cement2d_root',
    task_id='cement2d',
    output_dir='out',
)
model.msh.read_file('cement2d.msh')
model.gli.read_file('cement2d.gli')
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='GROUNDWATER_FLOW',
    NUM_TYPE='NEW',
    RELOAD=[3, 250],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    RELOAD=[3, 250],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    RELOAD=[3, 250],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    RELOAD=[3, 250],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    RELOAD=[3, 250],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    RELOAD=[3, 250],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    RELOAD=[3, 250],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    RELOAD=[3, 250],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    RELOAD=[3, 250],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    RELOAD=[3, 250],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POLYLINE', 'OUTLET'],
    DIS_TYPE=['CONSTANT', 10.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='1-C',
    GEO_TYPE=['POLYLINE', 'INLET_1'],
    DIS_TYPE=['CONSTANT', 0.00099674029573444],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='2-Ca',
    GEO_TYPE=['POLYLINE', 'INLET_1'],
    DIS_TYPE=['CONSTANT', 0.00199348059146888],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='3-Cl',
    GEO_TYPE=['POLYLINE', 'INLET_1'],
    DIS_TYPE=['CONSTANT', 19.9362013511029],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='4-H',
    GEO_TYPE=['POLYLINE', 'INLET_1'],
    DIS_TYPE=['CONSTANT', 0.00101064827675428],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='5-Na',
    GEO_TYPE=['POLYLINE', 'INLET_1'],
    DIS_TYPE=['CONSTANT', 19.9348059146889],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='6-O',
    GEO_TYPE=['POLYLINE', 'INLET_1'],
    DIS_TYPE=['CONSTANT', 0.0227326337437258],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='7-Oxa',
    GEO_TYPE=['POLYLINE', 'INLET_1'],
    DIS_TYPE=['CONSTANT', 0.00099674029573444],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='8-Si',
    GEO_TYPE=['POLYLINE', 'INLET_1'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='9-Zz',
    GEO_TYPE=['POLYLINE', 'INLET_1'],
    DIS_TYPE=['CONSTANT', 9.05437582453063e-14],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='1-C',
    GEO_TYPE=['POLYLINE', 'INLET_2'],
    DIS_TYPE=['CONSTANT', 9.86453094520442e-06],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='2-Ca',
    GEO_TYPE=['POLYLINE', 'INLET_2'],
    DIS_TYPE=['CONSTANT', 9.86453094519933e-06],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='3-Cl',
    GEO_TYPE=['POLYLINE', 'INLET_2'],
    DIS_TYPE=['CONSTANT', 1.68789503224731e-05],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='4-H',
    GEO_TYPE=['POLYLINE', 'INLET_2'],
    DIS_TYPE=['CONSTANT', 0.158035254545903],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='5-Na',
    GEO_TYPE=['POLYLINE', 'INLET_2'],
    DIS_TYPE=['CONSTANT', 789.16249249533],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='6-O',
    GEO_TYPE=['POLYLINE', 'INLET_2'],
    DIS_TYPE=['CONSTANT', 0.0198600359071739],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='7-Oxa',
    GEO_TYPE=['POLYLINE', 'INLET_2'],
    DIS_TYPE=['CONSTANT', 394.660154055751],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='8-Si',
    GEO_TYPE=['POLYLINE', 'INLET_2'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='9-Zz',
    GEO_TYPE=['POLYLINE', 'INLET_2'],
    DIS_TYPE=['CONSTANT', -4.19266058022328e-14],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POLYLINE', 'INLET_1'],
    DIS_TYPE=['CONSTANT', 5.7143e-10],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POLYLINE', 'INLET_2'],
    DIS_TYPE=['CONSTANT', 1.1429e-09],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[15, 0.3],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-05],
    MASS_DISPERSION=[1, 0.02, 0.02],
    DENSITY=[1, 1800.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[15, 0.19],
    TORTUOSITY=[1, 1.578949],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1.64e-06],
    MASS_DISPERSION=[1, 0.02, 0.02],
    DENSITY=[1, 1800.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[15, 0.3],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-05],
    MASS_DISPERSION=[1, 0.02, 0.02],
    DENSITY=[1, 1800.0],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 1800.0],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
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
    NAME='1-C',
    MOBILE=1,
    DIFFUSION=[1, 3.333333e-09],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='2-Ca',
    MOBILE=1,
    DIFFUSION=[1, 3.333333e-09],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='3-Cl',
    MOBILE=1,
    DIFFUSION=[1, 3.333333e-09],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='4-H',
    MOBILE=1,
    DIFFUSION=[1, 3.333333e-09],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='5-Na',
    MOBILE=1,
    DIFFUSION=[1, 3.333333e-09],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='6-O',
    MOBILE=1,
    DIFFUSION=[1, 3.333333e-09],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='7-Oxa',
    MOBILE=1,
    DIFFUSION=[1, 3.333333e-09],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='8-Si',
    MOBILE=1,
    DIFFUSION=[1, 3.333333e-09],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='9-Zz',
    MOBILE=0,
)
model.gem.add_block(
    main_key='GEM_PROPERTIES',
    GEM_THREADS=8,
)
model.gem.append_to_block(
    GEM_INIT_FILE='I1SetUp-dat.lst',
)
model.gem.append_to_block(
    FLAG_NODE_ELEMENT=0,
)
model.gem.append_to_block(
    FLAG_POROSITY_CHANGE=1,
)
model.gem.append_to_block(
    MIN_POROSITY=1e-06,
)
model.gem.append_to_block(
    MAX_POROSITY=1.0,
)
model.gem.append_to_block(
    FLAG_COUPLING_HYDROLOGY=1,
)
model.gem.append_to_block(
    TEMPERATURE_GEM=298.15,
)
model.gem.append_to_block(
    GEM_SMART=0,
)
model.gem.append_to_block(
    TRANSPORT_B=1,
)
model.gem.append_to_block(
    MAX_FAILED_NODES=50,
)
model.gem.append_to_block(
    MY_SMART_GEMS=-1e-30,
)
model.gem.append_to_block(
    KINETIC_GEM=[
        ['Portlandite', 1, 1, 0.0, 0.0, 0.0, 0.0, -5.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 'H+', 0.0, 0.0, 0.0],
        [3, 1000.0],
    ],
)
model.gem.append_to_block(
    KINETIC_GEM=[
        ['CaOxaHyd', 1, 1, 0.0, 0.0, 0.0, 0.0, -5.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 'H+', 0.0, 0.0, 0.0],
        [3, 1000.0],
    ],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='GROUNDWATER_FLOW',
    ELE_GAUSS_POINTS=3,
    LINEAR_SOLVER=[2, 6, 1e-14, 2000, 1.0, 1, 2],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='MASS_TRANSPORT',
    LINEAR_SOLVER=[2, 6, 1e-14, 2000, 1.0, 1, 2],
    ELE_GAUSS_POINTS=3,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='GROUNDWATER_FLOW',
    TIME_END=65.0,
    TIME_START=0.0,
    TIME_CONTROL=[
        ['SELF_ADAPTIVE'],
        [250, 1.05],
        [280, 0.8],
        ['MAX_TIME_STEP'],
        [10000000.0],
        ['MIN_TIME_STEP'],
        [1.0],
    ],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MASS_TRANSPORT',
    TIME_END=65.0,
    TIME_START=0.0,
    TIME_CONTROL=[
        ['SELF_ADAPTIVE'],
        [33, 1.05],
        [35, 0.8],
        ['MAX_TIME_STEP'],
        [10000000.0],
        ['MIN_TIME_STEP'],
        [1.0],
    ],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['HEAD'],
        ['1-C'],
        ['2-Ca'],
        ['3-Cl'],
        ['4-H'],
        ['5-Na'],
        ['6-O'],
        ['7-Oxa'],
        ['8-Si'],
        ['9-Zz'],
    ],
    ELE_VALUES=[
        ['POROSITY'],
        ['VELOCITY1_X'],
        ['VELOCITY1_Y'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='VTK',
    TIM_TYPE=['STEPS', 30],
)
model.gem_init.add(
    name='I1SetUp-dat',
    file_ext='.lst',
)
model.gem_init.read_file('I1SetUp-dat.lst')
model.asc.add(
    name='cement2d_MASS_TRANSPORT_3-Cl_primary_value',
    file_ext='.asc',
)
model.asc.read_file('cement2d_MASS_TRANSPORT_3-Cl_primary_value.asc')
model.asc.add(
    name='cement2d_MASS_TRANSPORT_9-Zz_primary_value',
    file_ext='.asc',
)
model.asc.read_file('cement2d_MASS_TRANSPORT_9-Zz_primary_value.asc')
model.asc.add(
    name='cement2d_MASS_TRANSPORT_8-Si_primary_value',
    file_ext='.asc',
)
model.asc.read_file('cement2d_MASS_TRANSPORT_8-Si_primary_value.asc')
model.asc.add(
    name='cement2d_MASS_TRANSPORT_1-C_primary_value',
    file_ext='.asc',
)
model.asc.read_file('cement2d_MASS_TRANSPORT_1-C_primary_value.asc')
model.asc.add(
    name='cement2d_m_xDC_gem',
    file_ext='.asc',
)
model.asc.read_file('cement2d_m_xDC_gem.asc')
model.asc.add(
    name='cement2d_time_gem',
    file_ext='.asc',
)
model.asc.read_file('cement2d_time_gem.asc')
model.asc.add(
    name='cement2d_m_porosity_gem',
    file_ext='.asc',
)
model.asc.read_file('cement2d_m_porosity_gem.asc')
model.asc.add(
    name='cement2d_MASS_TRANSPORT_7-Oxa_primary_value',
    file_ext='.asc',
)
model.asc.read_file('cement2d_MASS_TRANSPORT_7-Oxa_primary_value.asc')
model.asc.add(
    name='cement2d_MASS_TRANSPORT_2-Ca_primary_value',
    file_ext='.asc',
)
model.asc.read_file('cement2d_MASS_TRANSPORT_2-Ca_primary_value.asc')
model.asc.add(
    name='cement2d_m_fluid_volume_gem',
    file_ext='.asc',
)
model.asc.read_file('cement2d_m_fluid_volume_gem.asc')
model.asc.add(
    name='cement2d_m_bIC_gem',
    file_ext='.asc',
)
model.asc.read_file('cement2d_m_bIC_gem.asc')
model.asc.add(
    name='cement2d_MASS_TRANSPORT_6-O_primary_value',
    file_ext='.asc',
)
model.asc.read_file('cement2d_MASS_TRANSPORT_6-O_primary_value.asc')
model.asc.add(
    name='cement2d_GROUNDWATER_FLOW_HEAD_primary_value',
    file_ext='.asc',
)
model.asc.read_file('cement2d_GROUNDWATER_FLOW_HEAD_primary_value.asc')
model.asc.add(
    name='cement2d_MASS_TRANSPORT_5-Na_primary_value',
    file_ext='.asc',
)
model.asc.read_file('cement2d_MASS_TRANSPORT_5-Na_primary_value.asc')
model.asc.add(
    name='cement2d_MASS_TRANSPORT_4-H_primary_value',
    file_ext='.asc',
)
model.asc.read_file('cement2d_MASS_TRANSPORT_4-H_primary_value.asc')
model.write_input()
model.run_model()
