# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='2D1P_transport_root',
    task_id='2D1P_transport',
    output_dir='out',
)
model.msh.read_file('2D1P_transport.msh')
model.gli.read_file('2D1P_transport.gli')
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
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POLYLINE', 'L_BC'],
    DIS_TYPE=['CONSTANT', 10],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Tracer1',
    GEO_TYPE=['POLYLINE', 'BCTracer1'],
    DIS_TYPE=['CONSTANT', 1],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Tracer1',
    GEO_TYPE=['POLYLINE', 'BCTracer2'],
    DIS_TYPE=['CONSTANT', 1],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Tracer1',
    GEO_TYPE=['POLYLINE', 'BCWater3'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Tracer1',
    GEO_TYPE=['POLYLINE', 'BCWater2'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Tracer1',
    GEO_TYPE=['POLYLINE', 'BCWater1'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['RESTART', '_ic_heads.dat'],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Tracer1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-10],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POLYLINE', 'R_BC'],
    DIS_TYPE=['CONSTANT', -1.15741e-05],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.1],
    POROSITY_DISTRIBUTION='_het_n.dat',
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1.0],
    PERMEABILITY_DISTRIBUTION='_het_k.dat',
    MASS_DISPERSION=[1, 0.5, 0.05],
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
    NAME='Tracer1',
    MOBILE=1,
    DIFFUSION=[1, 1e-09],
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
    TIME_STEPS=[100, 21600],
    TIME_END=20000000000.0,
    TIME_START=0.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MASS_TRANSPORT',
    TIME_STEPS=[100, 21600],
    TIME_END=20000000000.0,
    TIME_START=0.0,
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['HEAD'],
        ['Tracer1'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 100],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES='Tracer1',
    GEO_TYPE=['POINT', 'POINT10'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES='Tracer1',
    GEO_TYPE=['POINT', 'POINT11'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.mpd.add(
    name='_het_k',
    file_ext='.dat',
)
model.mpd.read_file('_het_k.dat')
model.mpd.add(
    name='_het_n',
    file_ext='.dat',
)
model.mpd.read_file('_het_n.dat')
model.rfr.add(
    name='_ic_heads',
    file_ext='.dat',
)
model.rfr.read_file('_ic_heads.dat')
model.write_input()
model.run_model()
