# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='h2_line_root',
    task_id='h2_line',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='PS_GLOBAL',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 195000],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='PS_GLOBAL',
    PRIMARY_VARIABLE='SATURATION2',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.gli.read_file('h2_line.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='PS_GLOBAL',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 195000],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='PS_GLOBAL',
    PRIMARY_VARIABLE='SATURATION2',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.99],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='PRESSURE1',
    DENSITY=[1, 1000.0],
    VISCOSITY=[1, 0.001],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='GAS',
    PCS_TYPE='SATURATION2',
    DENSITY=[1, 1000.0],
    VISCOSITY=[1, 0.001],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=1,
    POROSITY=[1, 0.3],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-10],
    PERMEABILITY_SATURATION=[
        [6, 0.0, 1.0, 2.0],
        [66, 0.0, 1.0, 2.0, 1e-09],
    ],
    CAPILLARY_PRESSURE=[6, 5000],
)
model.msh.read_file('h2_line.msh')
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='PRESSURE1',
    ELE_UPWINDING=[0.0, 1],
    ELE_MASS_LUMPING=1,
    LINEAR_SOLVER=[805, 6, 1e-10, 1000, 1, 2],
    NON_LINEAR_ITERATION=['PICARD', 'LMAX', 100, 0.0, 10.0, 0.0001],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['PRESSURE2'],
        ['PRESSURE_CAP'],
        ['SATURATION1'],
        ['SATURATION2'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='PVD',
    TIM_TYPE=[
        [1000],
        [4000],
        [7000],
        [10000],
    ],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='PS_GLOBAL',
    NUM_TYPE='dPcdSwGradSnw',
)
model.rfd.add_block(
    PROJECT=['BUCKLEY_LEVERETT', 'PROBLEM'],
)
model.rfd.add_block(
    RENUMBER=[2, -1],
)
model.rfd.add_block(
    CURVE=[
        [100, 15650.9144],
        [200, 11652.92196],
        [300, 9881.745574],
        [400, 8825.9144],
        [500, 8105.379979],
        [600, 7573.503565],
        [700, 7160.129457],
        [800, 6826.918182],
        [900, 6550.9144],
        [1000, 6317.423406],
        [1100, 6116.544253],
        [1200, 5941.329987],
        [1300, 5786.743239],
        [1400, 5649.030352],
        [1500, 5525.329245],
        [1600, 5413.4144],
        [1700, 5311.525682],
        [1800, 5218.250254],
        [1900, 5132.439167],
        [2000, 5053.147189],
        [2100, 4979.588602],
        [2200, 4911.104178],
        [2300, 4847.136152],
        [2400, 4787.208982],
        [2500, 4730.9144],
        [2600, 4677.899645],
        [2700, 4627.858125],
        [2800, 4580.521928],
        [2900, 4535.655766],
        [3000, 4493.052037],
        [3100, 4452.526773],
        [3200, 4413.916291],
        [3300, 4377.074404],
        [3400, 4341.870087],
        [3500, 4308.185515],
        [3600, 4275.9144],
        [3700, 4244.960577],
        [3800, 4215.236798],
        [3900, 4186.663699],
        [4000, 4159.168903],
        [4100, 4132.68625],
        [4200, 4107.155127],
        [4300, 4082.519885],
        [4400, 4058.729327],
        [4500, 4035.73626],
        [4600, 4013.497102],
        [4700, 3991.971534],
        [4800, 3971.122194],
        [4900, 3950.9144],
        [5000, 3931.315913],
        [5100, 3912.296715],
        [5200, 3893.82882],
        [5300, 3875.886098],
        [5400, 3858.444122],
        [5500, 3841.480025],
        [5600, 3824.972376],
        [5700, 3808.901067],
        [5800, 3793.247209],
        [5900, 3777.993035],
        [6000, 3763.121823],
        [6100, 3748.617811],
        [6200, 3734.466134],
        [6300, 3720.652752],
        [6400, 3707.1644],
        [6500, 3693.988527],
        [6600, 3681.113252],
        [6700, 3668.527315],
        [6800, 3656.220041],
        [6900, 3644.181295],
        [7000, 3632.401452],
        [7100, 3620.871363],
        [7200, 3609.582327],
        [7300, 3598.526059],
        [7400, 3587.694669],
        [7500, 3577.080635],
        [7600, 3566.676784],
        [7700, 3556.476269],
        [7800, 3546.472552],
        [7900, 3536.659385],
        [8000, 3527.030795],
        [8100, 3517.581067],
        [8200, 3508.304731],
        [8300, 3499.196549],
        [8400, 3490.251501],
        [8500, 3481.464775],
        [8600, 3472.831754],
        [8700, 3464.34801],
        [8800, 3456.009289],
        [8900, 3447.811506],
        [9000, 3439.750735],
        [9100, 3431.823202],
        [9200, 3424.025276],
        [9300, 3416.353463],
        [9400, 3408.804401],
        [9500, 3401.374851],
        [9600, 3394.061691],
        [9700, 3386.861915],
        [9800, 3379.772623],
        [9900, 3372.791018],
        [10000, 3365.9144],
    ],
)
model.st.add_block(
    main_key='SOURCE_TERM',
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='PS_GLOBAL',
    TIME_CONTROL=[
        ['PI_AUTO_STEP_SIZE'],
        [1, 0.0001, 1e-10, '10s'],
    ],
    TIME_END=10000.0,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
