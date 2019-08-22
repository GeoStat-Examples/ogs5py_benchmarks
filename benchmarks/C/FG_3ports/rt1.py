# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='rt1_root',
    task_id='rt1',
    output_dir='out',
)
model.msh.read_file('rt1.msh')
model.gli.read_file('rt1.gli')
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='GROUNDWATER_FLOW',
    NUM_TYPE='NEW',
    TIM_TYPE='STEADY',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    MEMORY_TYPE=1,
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    MEMORY_TYPE=1,
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    MEMORY_TYPE=1,
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    MEMORY_TYPE=1,
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    MEMORY_TYPE=1,
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    MEMORY_TYPE=1,
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POLYLINE', 'PLY_BC_RIGHT'],
    DIS_TYPE=['CONSTANT', 0.11],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Tracer',
    GEO_TYPE=['POLYLINE', 'PLY_S2'],
    EPSILON=0.0002,
    DIS_TYPE=['CONSTANT', 0.0087],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Tracer',
    GEO_TYPE=['POLYLINE', 'PLY_S1'],
    EPSILON=0.0002,
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Tracer',
    GEO_TYPE=['POLYLINE', 'PLY_S3'],
    EPSILON=0.0002,
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Tracer',
    GEO_TYPE=['POLYLINE', 'PLY_BC_LEFT_1'],
    EPSILON=1e-05,
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Tracer',
    GEO_TYPE=['POLYLINE', 'PLY_BC_LEFT_2'],
    EPSILON=1e-05,
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Tracer',
    GEO_TYPE=['POLYLINE', 'PLY_BC_LEFT_3'],
    EPSILON=1e-05,
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Tracer',
    GEO_TYPE=['POLYLINE', 'PLY_BC_LEFT_4'],
    EPSILON=1e-05,
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Toluene',
    GEO_TYPE=['POLYLINE', 'PLY_S2'],
    EPSILON=0.0002,
    DIS_TYPE=['CONSTANT', 0.0087],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Toluene',
    GEO_TYPE=['POLYLINE', 'PLY_S1'],
    EPSILON=0.0002,
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Toluene',
    GEO_TYPE=['POLYLINE', 'PLY_S3'],
    EPSILON=0.0002,
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Toluene',
    GEO_TYPE=['POLYLINE', 'PLY_BC_LEFT_1'],
    EPSILON=1e-05,
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Toluene',
    GEO_TYPE=['POLYLINE', 'PLY_BC_LEFT_2'],
    EPSILON=1e-05,
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Toluene',
    GEO_TYPE=['POLYLINE', 'PLY_BC_LEFT_3'],
    EPSILON=1e-05,
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Toluene',
    GEO_TYPE=['POLYLINE', 'PLY_BC_LEFT_4'],
    EPSILON=1e-05,
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Nitrate',
    GEO_TYPE=['POLYLINE', 'PLY_S2'],
    EPSILON=0.0002,
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Nitrate',
    GEO_TYPE=['POLYLINE', 'PLY_S1'],
    EPSILON=0.0002,
    DIS_TYPE=['CONSTANT', 0.62],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Nitrate',
    GEO_TYPE=['POLYLINE', 'PLY_S3'],
    EPSILON=0.0002,
    DIS_TYPE=['CONSTANT', 0.62],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Nitrate',
    GEO_TYPE=['POLYLINE', 'PLY_BC_LEFT_1'],
    EPSILON=1e-05,
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Nitrate',
    GEO_TYPE=['POLYLINE', 'PLY_BC_LEFT_2'],
    EPSILON=1e-05,
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Nitrate',
    GEO_TYPE=['POLYLINE', 'PLY_BC_LEFT_3'],
    EPSILON=1e-05,
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Nitrate',
    GEO_TYPE=['POLYLINE', 'PLY_BC_LEFT_4'],
    EPSILON=1e-05,
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Comp_C',
    GEO_TYPE=['POLYLINE', 'PLY_BC_LEFT'],
    EPSILON=1e-05,
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.11],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Tracer',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Toluene',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Nitrate',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0685],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Comp_C',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Aromaticum',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0001],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Reaction_Mark',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POLYLINE', 'PLY_S2'],
    DIS_TYPE=['CONSTANT_GEO', 9.67e-10],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POLYLINE', 'PLY_S1'],
    DIS_TYPE=['CONSTANT_GEO', 9.67e-10],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POLYLINE', 'PLY_S3'],
    DIS_TYPE=['CONSTANT_GEO', 9.67e-10],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=0.011,
    POROSITY=[1, 0.4],
    VOL_BIO=[1, 0.01],
    VOL_MAT=[1, 0.522],
    TORTUOSITY=[1, 1.0],
    STORAGE=[1, 0.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 0.00041095],
    MASS_DISPERSION=[1, 0.00076, 6e-05],
    DENSITY=[1, 2000.0],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2000.0],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2000.0],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='HEAD',
    DENSITY=[1, 1000.0],
    VISCOSITY=[1, 0.001],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Tracer',
    MOBILE=1,
    DIFFUSION=[1, 8.49e-10],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Toluene',
    MOBILE=1,
    DIFFUSION=[1, 8.49e-10],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Nitrate',
    MOBILE=1,
    DIFFUSION=[1, 9.98519e-10],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Comp_C',
    MOBILE=1,
    DIFFUSION=[1, 0.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Reaction_Mark',
    MOBILE=0,
    DIFFUSION=[1, 0.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Aromaticum',
    MOBILE=0,
    DIFFUSION=0,
    DECAY=[1, 8.10185e-09, 1.0],
)
model.krc.add_block(
    main_key='KINREACTIONDATA',
    SOLVER_TYPE=1,
    RELATIVE_ERROR=1e-06,
    MIN_TIMESTEP=1e-07,
    INITIAL_TIMESTEP=0.0001,
    BACTERIACAPACITY=100.0,
    NO_REACTIONS=['POLYLINE', 'PLY_BC_LEFT'],
    MIN_CONCENTRATION_REPLACE=[1, 1e-19, 0.0],
)
model.krc.add_block(
    main_key='REACTION',
    NAME='DoubleMonod',
    TYPE='monod',
    BACTERIANAME='Aromaticum',
    EQUATION=[1, 'Toluene', '+', 7.2, 'Nitrate', '=', 7, 'Comp_C'],
    RATECONSTANT=[7.87037e-06, 1.0],
    GROWTH=1,
    MONODTERMS=[
        ['Toluene', 0.023035, 1.0],
        ['Nitrate', 0.004340343, 1.0],
    ],
    INHIBITIONTERMS=[],
    PRODUCTIONSTOCH=[
        ['Toluene', -1.0],
        ['Nitrate', '-7.2.0'],
        ['Comp_C', 7.0],
        ['Reaction_Mark', 1],
    ],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='GROUNDWATER_FLOW',
    ELE_GAUSS_POINTS=3,
    LINEAR_SOLVER=[2, 6, 1e-12, 2000, 1.0, 1, 2],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='MASS_TRANSPORT',
    LINEAR_SOLVER=[2, 6, 1e-10, 2000, 1, 1, 2],
    ELE_GAUSS_POINTS=3,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='GROUNDWATER_FLOW',
    TIME_STEPS=[100, 50.0],
    TIME_END=86400000000.0,
    TIME_START=0.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MASS_TRANSPORT',
    TIME_STEPS=[100, 50.0],
    TIME_END=86400000000.0,
    TIME_START=0.0,
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['HEAD'],
        ['Tracer'],
        ['Toluene'],
        ['Nitrate'],
        ['Aromaticum'],
        ['Comp_C'],
        ['Reaction_Mark'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [50],
        [100],
        [5000],
    ],
)
model.write_input()
model.run_model()
