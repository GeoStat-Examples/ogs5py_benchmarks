# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='h_us_quad_root',
    task_id='h_us_quad',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'BOTTOM'],
    DIS_TYPE=['CONSTANT', -21500.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'TOP'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.gli.read_file('h_us_quad.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', -21500],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='PRESSURE1',
    DENSITY=[1, 1000.0],
    VISCOSITY=[1, 0.001],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.38],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 4.46e-13],
    PERMEABILITY_SATURATION=[
        [0, 2],
        [0, 2],
    ],
    CAPILLARY_PRESSURE=[0, 1],
)
model.msh.read_file('h_us_quad.msh')
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='RICHARDS_FLOW',
    ELE_UPWINDING=0.5,
    ELE_MASS_LUMPING=1,
    ELE_GAUSS_POINTS=3,
    LINEAR_SOLVER=[3, 6, 1e-10, 1000, 1.0, 101, 4],
    NON_LINEAR_SOLVER=['PICARD', 0.001, 50, 0.0],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='RICHARDS_FLOW',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['SATURATION1'],
    ],
    GEO_TYPE='DOMAIN',
    TIM_TYPE=[
        [0.01],
        [0.1],
        [1.0],
        [180.0],
        [1800.0],
        [3600.0],
        [7200.0],
        [32400.0],
        [61200.0],
    ],
    DAT_TYPE='TECPLOT',
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='RICHARDS_FLOW',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['SATURATION1'],
    ],
    GEO_TYPE=['POLYLINE', 'OUT'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [0.01],
        [0.1],
        [1.0],
        [180.0],
        [1800.0],
        [3600.0],
        [7200.0],
        [32400.0],
        [61200.0],
    ],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='RICHARDS_FLOW',
    NUM_TYPE='NEW',
)
model.rfd.add_block(
    PROJECT=['NETZ', 'AUS', '1D-ELEMENTEN'],
)
model.rfd.add_block(
    CURVE=[
        [0.26315789, 44627.5611],
        [0.39473684, 26399.6732],
        [0.52631579, 15616.8683],
        [0.57894737, 12658.7874],
        [0.63157895, 10261.0136],
        [0.65789474, 9238.24221],
        [0.78947368, 5464.93174],
        [0.81578947, 4920.21206],
        [0.84210526, 4429.78757],
        [0.86842105, 3988.24638],
        [0.89473684, 3590.71602],
        [0.92105263, 3232.80969],
        [0.94894737, 2892.29884],
        [0.96052632, 2462.21599],
        [0.97368421, 2050.45507],
        [0.98684211, 1707.55369],
        [1.0, 1421.99634],
    ],
)
model.rfd.add_block(
    CURVE=[
        [0.26315789, 4.4323e-05],
        [0.39473684, 0.00026547],
        [0.52631579, 0.00159003],
        [0.57894737, 0.00325358],
        [0.63157895, 0.00665757],
        [0.65789474, 0.00952343],
        [0.78947368, 0.05704014],
        [0.81578947, 0.08159396],
        [0.84210526, 0.11671736],
        [0.86842105, 0.16696017],
        [0.89473684, 0.23883078],
        [0.92105263, 0.34163922],
        [0.94894737, 0.49931406],
        [0.96052632, 0.58449912],
        [0.97368421, 0.69907308],
        [0.98684211, 0.8361059],
        [1.0, 1.0],
    ],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'BOTTOM'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='RICHARDS_FLOW',
    TIME_STEPS=[
        [100, 10],
        [1000, 100],
    ],
    TIME_END=61200.0,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
