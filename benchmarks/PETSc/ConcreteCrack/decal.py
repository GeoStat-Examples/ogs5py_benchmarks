# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='decal_root',
    task_id='decal',
    output_dir='out',
)
model.msh.read_file('decal.msh')
model.gli.read_file('decal.gli')
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='GROUNDWATER_FLOW',
    NUM_TYPE='NEW',
    RELOAD=[1, 1000],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    RELOAD=[1, 1000],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    RELOAD=[1, 1000],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    RELOAD=[1, 1000],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    RELOAD=[1, 1000],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    RELOAD=[1, 1000],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    RELOAD=[1, 1000],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    RELOAD=[1, 1000],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    RELOAD=[1, 1000],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    RELOAD=[1, 1000],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    RELOAD=[1, 1000],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    RELOAD=[1, 1000],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    RELOAD=[1, 1000],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    RELOAD=[1, 1000],
)
model.cct.add_block(
    main_key='COMMUNICATION_TABLE',
    MYRANK=0,
    NNEIGHBORS=1,
    NEIGHBOR=[
        [1],
        [63],
        [11, 449],
        [11, 573],
        [138, 566],
        [138, 576],
        [139, 577],
        [139, 579],
        [139, 588],
        [140, 589],
        [140, 591],
        [140, 600],
        [141, 601],
        [141, 603],
        [141, 612],
        [142, 613],
        [142, 615],
        [192, 574],
        [192, 576],
        [192, 579],
        [195, 586],
        [195, 588],
        [195, 591],
        [198, 598],
        [198, 600],
        [198, 603],
        [201, 610],
        [201, 612],
        [201, 615],
        [203, 567],
        [203, 570],
        [203, 571],
        [203, 573],
        [391, 566],
        [403, 574],
        [403, 577],
        [403, 579],
        [406, 566],
        [406, 574],
        [406, 576],
        [415, 586],
        [415, 589],
        [415, 591],
        [418, 577],
        [418, 586],
        [418, 588],
        [427, 598],
        [427, 601],
        [427, 603],
        [430, 589],
        [430, 598],
        [430, 600],
        [439, 610],
        [439, 613],
        [439, 615],
        [442, 601],
        [442, 610],
        [442, 612],
        [444, 567],
        [445, 449],
        [445, 570],
        [445, 573],
        [447, 492],
        [447, 566],
        [447, 567],
    ],
)
model.cct.add_block(
    main_key='COMMUNICATION_TABLE',
    MYRANK=1,
)
model.cct.append_to_block(
    NNEIGHBORS=2,
)
model.cct.append_to_block(
    NEIGHBOR=[
        [0],
        [63],
        [449, 11],
        [449, 445],
        [492, 447],
        [566, 138],
        [566, 391],
        [566, 406],
        [566, 447],
        [567, 203],
        [567, 444],
        [567, 447],
        [570, 203],
        [570, 445],
        [571, 203],
        [573, 11],
        [573, 203],
        [573, 445],
        [574, 192],
        [574, 403],
        [574, 406],
        [576, 138],
        [576, 192],
        [576, 406],
        [577, 139],
        [577, 403],
        [577, 418],
        [579, 139],
        [579, 192],
        [579, 403],
        [586, 195],
        [586, 415],
        [586, 418],
        [588, 139],
        [588, 195],
        [588, 418],
        [589, 140],
        [589, 415],
        [589, 430],
        [591, 140],
        [591, 195],
        [591, 415],
        [598, 198],
        [598, 427],
        [598, 430],
        [600, 140],
        [600, 198],
        [600, 430],
        [601, 141],
        [601, 427],
        [601, 442],
        [603, 141],
        [603, 198],
        [603, 427],
        [610, 201],
        [610, 439],
        [610, 442],
        [612, 141],
        [612, 201],
        [612, 442],
        [613, 142],
        [613, 439],
        [615, 142],
        [615, 201],
        [615, 439],
    ],
)
model.cct.append_to_block(
    NEIGHBOR=[
        [2],
        [61],
        [457, 883],
        [457, 1004],
        [862, 916],
        [862, 1004],
        [862, 1005],
        [863, 883],
        [863, 916],
        [863, 1004],
        [864, 914],
        [864, 1005],
        [864, 1012],
        [865, 914],
        [865, 916],
        [865, 1005],
        [866, 919],
        [866, 1012],
        [866, 1013],
        [867, 914],
        [867, 919],
        [867, 1012],
        [868, 917],
        [868, 1013],
        [868, 1020],
        [869, 917],
        [869, 919],
        [869, 1013],
        [870, 922],
        [870, 1020],
        [870, 1021],
        [871, 917],
        [871, 922],
        [871, 1020],
        [872, 920],
        [872, 1021],
        [872, 1028],
        [873, 920],
        [873, 922],
        [873, 1021],
        [874, 925],
        [874, 1028],
        [874, 1029],
        [875, 920],
        [875, 925],
        [875, 1028],
        [876, 923],
        [876, 1029],
        [876, 1036],
        [877, 923],
        [877, 925],
        [877, 1029],
        [878, 928],
        [878, 1036],
        [878, 1037],
        [879, 923],
        [879, 928],
        [879, 1036],
        [880, 926],
        [880, 1037],
        [881, 926],
        [881, 928],
        [881, 1037],
    ],
)
model.cct.add_block(
    main_key='COMMUNICATION_TABLE',
    MYRANK=2,
)
model.cct.append_to_block(
    NNEIGHBORS=2,
)
model.cct.append_to_block(
    NEIGHBOR=[
        [1],
        [61],
        [883, 457],
        [883, 863],
        [914, 864],
        [914, 865],
        [914, 867],
        [916, 862],
        [916, 863],
        [916, 865],
        [917, 868],
        [917, 869],
        [917, 871],
        [919, 866],
        [919, 867],
        [919, 869],
        [920, 872],
        [920, 873],
        [920, 875],
        [922, 870],
        [922, 871],
        [922, 873],
        [923, 876],
        [923, 877],
        [923, 879],
        [925, 874],
        [925, 875],
        [925, 877],
        [926, 880],
        [926, 881],
        [928, 878],
        [928, 879],
        [928, 881],
        [1004, 457],
        [1004, 862],
        [1004, 863],
        [1005, 862],
        [1005, 864],
        [1005, 865],
        [1012, 864],
        [1012, 866],
        [1012, 867],
        [1013, 866],
        [1013, 868],
        [1013, 869],
        [1020, 868],
        [1020, 870],
        [1020, 871],
        [1021, 870],
        [1021, 872],
        [1021, 873],
        [1028, 872],
        [1028, 874],
        [1028, 875],
        [1029, 874],
        [1029, 876],
        [1029, 877],
        [1036, 876],
        [1036, 878],
        [1036, 879],
        [1037, 878],
        [1037, 880],
        [1037, 881],
    ],
)
model.cct.append_to_block(
    NEIGHBOR=[
        [3],
        [61],
        [993, 1444],
        [993, 1447],
        [993, 1456],
        [994, 1449],
        [994, 1450],
        [995, 1446],
        [995, 1447],
        [995, 1450],
        [996, 1451],
        [996, 1454],
        [996, 1462],
        [997, 1453],
        [997, 1454],
        [997, 1456],
        [998, 1457],
        [998, 1460],
        [998, 1468],
        [999, 1459],
        [999, 1460],
        [999, 1462],
        [1000, 1463],
        [1000, 1466],
        [1000, 1474],
        [1001, 1465],
        [1001, 1466],
        [1001, 1468],
        [1002, 1469],
        [1002, 1472],
        [1003, 1471],
        [1003, 1472],
        [1003, 1474],
        [1293, 1446],
        [1293, 1449],
        [1293, 1450],
        [1297, 1444],
        [1297, 1446],
        [1297, 1447],
        [1300, 1444],
        [1300, 1453],
        [1300, 1456],
        [1303, 1451],
        [1303, 1453],
        [1303, 1454],
        [1306, 1451],
        [1306, 1459],
        [1306, 1462],
        [1309, 1457],
        [1309, 1459],
        [1309, 1460],
        [1312, 1457],
        [1312, 1465],
        [1312, 1468],
        [1315, 1463],
        [1315, 1465],
        [1315, 1466],
        [1318, 1463],
        [1318, 1471],
        [1318, 1474],
        [1321, 1469],
        [1321, 1471],
        [1321, 1472],
    ],
)
model.cct.add_block(
    main_key='COMMUNICATION_TABLE',
    MYRANK=3,
    NNEIGHBORS=1,
    NEIGHBOR=[
        [2],
        [61],
        [1444, 993],
        [1444, 1297],
        [1444, 1300],
        [1446, 995],
        [1446, 1293],
        [1446, 1297],
        [1447, 993],
        [1447, 995],
        [1447, 1297],
        [1449, 994],
        [1449, 1293],
        [1450, 994],
        [1450, 995],
        [1450, 1293],
        [1451, 996],
        [1451, 1303],
        [1451, 1306],
        [1453, 997],
        [1453, 1300],
        [1453, 1303],
        [1454, 996],
        [1454, 997],
        [1454, 1303],
        [1456, 993],
        [1456, 997],
        [1456, 1300],
        [1457, 998],
        [1457, 1309],
        [1457, 1312],
        [1459, 999],
        [1459, 1306],
        [1459, 1309],
        [1460, 998],
        [1460, 999],
        [1460, 1309],
        [1462, 996],
        [1462, 999],
        [1462, 1306],
        [1463, 1000],
        [1463, 1315],
        [1463, 1318],
        [1465, 1001],
        [1465, 1312],
        [1465, 1315],
        [1466, 1000],
        [1466, 1001],
        [1466, 1315],
        [1468, 998],
        [1468, 1001],
        [1468, 1312],
        [1469, 1002],
        [1469, 1321],
        [1471, 1003],
        [1471, 1318],
        [1471, 1321],
        [1472, 1002],
        [1472, 1003],
        [1472, 1321],
        [1474, 1000],
        [1474, 1003],
        [1474, 1318],
    ],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POLYLINE', 'UPPER_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 10.105],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POLYLINE', 'LOWER_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 10.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='1-Al',
    GEO_TYPE=['POLYLINE', 'UPPER_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 9.99971113325135e-08],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='2-C',
    GEO_TYPE=['POLYLINE', 'UPPER_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 9.99971143136683e-08],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='3-Ca',
    GEO_TYPE=['POLYLINE', 'UPPER_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 9.99971129176716e-08],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='4-Cl',
    GEO_TYPE=['POLYLINE', 'UPPER_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 0.0171102542463709],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='5-H',
    GEO_TYPE=['POLYLINE', 'UPPER_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 0.996970725474602],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='6-Mg',
    GEO_TYPE=['POLYLINE', 'UPPER_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 9.99971123536509e-08],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='7-N',
    GEO_TYPE=['POLYLINE', 'UPPER_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 0.996971229734092],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='8-Na',
    GEO_TYPE=['POLYLINE', 'UPPER_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 0.0171102542463709],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='9-O',
    GEO_TYPE=['POLYLINE', 'UPPER_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 3.5385586833804],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='10-S',
    GEO_TYPE=['POLYLINE', 'UPPER_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 9.99971113084322e-08],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='11-Si',
    GEO_TYPE=['POLYLINE', 'UPPER_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 9.99970976287577e-08],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='12-Sn',
    GEO_TYPE=['POLYLINE', 'UPPER_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='13-Zz',
    GEO_TYPE=['POLYLINE', 'UPPER_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 1.60955109767583e-14],
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
    PRIMARY_VARIABLE='1-Al',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 302.400344162658],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='2-C',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 166.950190006468],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='3-Ca',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 3894.45443228924],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='4-Cl',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1.00000113810403e-05],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='5-H',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 23810.6270989398],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='6-Mg',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 121.450137008233],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='7-N',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 2.00000227620806e-05],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='8-Na',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1.00000113810403e-05],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='9-O',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 19304.0969562231],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='10-S',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 131.250143611302],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='11-Si',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1100.75125276801],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='12-Sn',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 43208.6791759159],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='13-Zz',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='1-Al',
    GEO_TYPE=['SURFACE', 'SURF_1'],
    DIS_TYPE=['CONSTANT', 0.00741123079164733],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='2-C',
    GEO_TYPE=['SURFACE', 'SURF_1'],
    DIS_TYPE=['CONSTANT', 0.00662539884184819],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='3-Ca',
    GEO_TYPE=['SURFACE', 'SURF_1'],
    DIS_TYPE=['CONSTANT', 20.519164911863],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='4-Cl',
    GEO_TYPE=['SURFACE', 'SURF_1'],
    DIS_TYPE=['CONSTANT', 0.000411753275500439],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='5-H',
    GEO_TYPE=['SURFACE', 'SURF_1'],
    DIS_TYPE=['CONSTANT', 110739.503488593],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='6-Mg',
    GEO_TYPE=['SURFACE', 'SURF_1'],
    DIS_TYPE=['CONSTANT', 1.21414581851422e-05],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='7-N',
    GEO_TYPE=['SURFACE', 'SURF_1'],
    DIS_TYPE=['CONSTANT', 0.000823506551000878],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='8-Na',
    GEO_TYPE=['SURFACE', 'SURF_1'],
    DIS_TYPE=['CONSTANT', 0.000411753275500439],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='9-O',
    GEO_TYPE=['SURFACE', 'SURF_1'],
    DIS_TYPE=['CONSTANT', 55390.9858607139],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='10-S',
    GEO_TYPE=['SURFACE', 'SURF_1'],
    DIS_TYPE=['CONSTANT', 0.0248103673751612],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='11-Si',
    GEO_TYPE=['SURFACE', 'SURF_1'],
    DIS_TYPE=['CONSTANT', 0.0337993230746222],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='12-Sn',
    GEO_TYPE=['SURFACE', 'SURF_1'],
    DIS_TYPE=['CONSTANT', 4.11753275500439e-06],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='13-Zz',
    GEO_TYPE=['SURFACE', 'SURF_1'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='1-Al',
    GEO_TYPE=['SURFACE', 'TOP'],
    DIS_TYPE=['CONSTANT', 3.00001315815077e-08],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='2-C',
    GEO_TYPE=['SURFACE', 'TOP'],
    DIS_TYPE=['CONSTANT', 3.00001315815077e-08],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='3-Ca',
    GEO_TYPE=['SURFACE', 'TOP'],
    DIS_TYPE=['CONSTANT', 6.15002700420922],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='4-Cl',
    GEO_TYPE=['SURFACE', 'TOP'],
    DIS_TYPE=['CONSTANT', 5.13324691710837e-10],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='5-H',
    GEO_TYPE=['SURFACE', 'TOP'],
    DIS_TYPE=['CONSTANT', 33219.3197926609],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='6-Mg',
    GEO_TYPE=['SURFACE', 'TOP'],
    DIS_TYPE=['CONSTANT', 3.00001315815077e-08],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='7-N',
    GEO_TYPE=['SURFACE', 'TOP'],
    DIS_TYPE=['CONSTANT', 3.00001315815077e-08],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='8-Na',
    GEO_TYPE=['SURFACE', 'TOP'],
    DIS_TYPE=['CONSTANT', 5.13324691710837e-10],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='9-O',
    GEO_TYPE=['SURFACE', 'TOP'],
    DIS_TYPE=['CONSTANT', 16615.9742224153],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='10-S',
    GEO_TYPE=['SURFACE', 'TOP'],
    DIS_TYPE=['CONSTANT', 3.00001315815077e-08],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='11-Si',
    GEO_TYPE=['SURFACE', 'TOP'],
    DIS_TYPE=['CONSTANT', 3.00001315815077e-08],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='12-Sn',
    GEO_TYPE=['SURFACE', 'TOP'],
    DIS_TYPE=['CONSTANT', 42975.1884905098],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='13-Zz',
    GEO_TYPE=['SURFACE', 'TOP'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='1-Al',
    GEO_TYPE=['POLYLINE', 'UPPER_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 2.99991463962411e-08],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='2-C',
    GEO_TYPE=['POLYLINE', 'UPPER_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 2.99991463962411e-08],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='3-Ca',
    GEO_TYPE=['POLYLINE', 'UPPER_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 2.99991463962411e-08],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='4-Cl',
    GEO_TYPE=['POLYLINE', 'UPPER_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 0.00513307834453998],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='5-H',
    GEO_TYPE=['POLYLINE', 'UPPER_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 33206.2283327352],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='6-Mg',
    GEO_TYPE=['POLYLINE', 'UPPER_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 2.99991463962411e-08],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='7-N',
    GEO_TYPE=['POLYLINE', 'UPPER_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 0.299091489570524],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='8-Na',
    GEO_TYPE=['POLYLINE', 'UPPER_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 0.00513307834453998],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='9-O',
    GEO_TYPE=['POLYLINE', 'UPPER_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 16604.0261887317],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='10-S',
    GEO_TYPE=['POLYLINE', 'UPPER_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 2.99991463962411e-08],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='11-Si',
    GEO_TYPE=['POLYLINE', 'UPPER_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 2.99991463962411e-08],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='12-Sn',
    GEO_TYPE=['POLYLINE', 'UPPER_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 42973.7772126154],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='13-Zz',
    GEO_TYPE=['POLYLINE', 'UPPER_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[15, 0.3],
    TORTUOSITY=[1, 0.0383],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-09],
    PERMEABILITY_FUNCTION_POROSITY=[4, 0.3, 1e-09],
    MASS_DISPERSION=[1, 1e-05, 1e-06],
    DENSITY=[1, 1800.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[15, 0.097],
    TORTUOSITY=[1, 0.0383],
    PERMEABILITY_TENSOR=['ISOTROPIC', 5e-11],
    PERMEABILITY_FUNCTION_POROSITY=[4, 0.097, 5e-11],
    MASS_DISPERSION=[1, 1e-05, 1e-06],
    DENSITY=[1, 1800.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=1,
    GEOMETRY_AREA=0.0005,
    POROSITY=[15, 1.0],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 0.41],
    PERMEABILITY_FUNCTION_POROSITY=[4, 1.0, 0.41],
    MASS_DISPERSION=[1, 1e-05, 1e-06],
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
    NAME='1-Al',
    MOBILE=1,
    DIFFUSION=[8, 1e-09, 2.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='2-C',
    MOBILE=1,
    DIFFUSION=[8, 1e-09, 2.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='3-Ca',
    MOBILE=1,
    DIFFUSION=[8, 1e-09, 2.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='4-Cl',
    MOBILE=1,
    DIFFUSION=[8, 1e-09, 2.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='5-H',
    MOBILE=1,
    DIFFUSION=[8, 1e-09, 2.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='6-Mg',
    MOBILE=1,
    DIFFUSION=[8, 1e-09, 2.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='7-N',
    MOBILE=1,
    DIFFUSION=[8, 1e-09, 2.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='8-Na',
    MOBILE=1,
    DIFFUSION=[8, 1e-09, 2.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='9-O',
    MOBILE=1,
    DIFFUSION=[8, 1e-09, 2.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='10-S',
    MOBILE=1,
    DIFFUSION=[8, 1e-09, 2.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='11-Si',
    MOBILE=1,
    DIFFUSION=[8, 1e-09, 2.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='12-Sn',
    MOBILE=1,
    DIFFUSION=[8, 1e-09, 2.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='13-Zz',
    MOBILE=1,
    DIFFUSION=[8, 1e-09, 2.0],
)
model.gem.add_block(
    main_key='GEM_PROPERTIES',
    FLAG_DISABLE_GEM=0,
    GEM_THREADS=4,
    GEM_INIT_FILE='cement_bc-dat.lst',
    FLAG_POROSITY_CHANGE=1,
    MIN_POROSITY=1e-06,
    MAX_POROSITY=1.0,
    FLAG_COUPLING_HYDROLOGY=0,
    TEMPERATURE_GEM=298.15,
    MY_SMART_GEMS=-1e-30,
    MAX_FAILED_NODES=5,
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='GROUNDWATER_FLOW',
    ELE_GAUSS_POINTS=3,
    LINEAR_SOLVER=['petsc', 'preonly', 'tfs', 1e-12, 10000, 1.0],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='MASS_TRANSPORT',
    LINEAR_SOLVER=['petsc', 'bcgs', 'bjacobi', 1e-14, 2000, 1.0],
    ELE_GAUSS_POINTS=3,
    FEM_FCT=[1, 0],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='GROUNDWATER_FLOW',
    TIME_END=10.0,
    TIME_START=0.0,
    TIME_CONTROL=[
        ['SELF_ADAPTIVE'],
        [10000, 1.1],
        [10003, 0.8],
        ['MAX_TIME_STEP'],
        [100000.0],
        ['MIN_TIME_STEP'],
        [1.0],
    ],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MASS_TRANSPORT',
    TIME_END=10.0,
    TIME_START=0.0,
    TIME_CONTROL=[
        ['SELF_ADAPTIVE'],
        [230, 1.1],
        [250, 0.8],
        ['MAX_TIME_STEP'],
        [100000.0],
        ['MIN_TIME_STEP'],
        [1.0],
    ],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['1-Al'],
        ['2-C'],
        ['3-Ca'],
        ['4-Cl'],
        ['5-H'],
        ['6-Mg'],
        ['7-N'],
        ['8-Na'],
        ['9-O'],
        ['10-S'],
        ['11-Si'],
        ['12-Sn'],
        ['13-Zz'],
        ['HEAD'],
    ],
    ELE_VALUES=[
        ['POROSITY'],
        ['PERMEABILITY'],
        ['VELOCITY1_X'],
        ['VELOCITY1_Y'],
        ['VELOCITY1_Z'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='VTK',
    TIM_TYPE=['STEPS', 1],
)
model.gem_init.add(
    name='cement_bc-dat',
    file_ext='.lst',
)
model.gem_init.read_file('cement_bc-dat.lst')
model.write_input()
model.run_model()
