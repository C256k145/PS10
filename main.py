from math import log2

attributes = {
    2  : "handicapped-infants: 2 (y,n)",
    3  : "water-project-cost-sharing: 2 (y,n) ",
    4  : "adoption-of-the-budget-resolution: 2 (y,n) ",
    5  : "physician-fee-freeze: 2 (y,n) ",
    6  : "el-salvador-aid: 2 (y,n) ",
    7  : "religious-groups-in-schools: 2 (y,n) ",
    8  : "anti-satellite-test-ban: 2 (y,n) ",
    9  : "aid-to-nicaraguan-contras: 2 (y,n) ",
    10 : "mx-missile: 2 (y,n)",
    11 : "immigration: 2 (y,n)",
    12 : "synfuels-corporation-cutback: 2 (y,n)",
    13 : "education-spending: 2 (y,n)",
    14 : "superfund-right-to-sue: 2 (y,n)",
    15 : "crime: 2 (y,n)",
    16 : "duty-free-exports: 2 (y,n)",
    17 : "export-administration-act-south-africa: 2 (y,n)"
}

table=[
    [0,0,1,1,0,1,1,0,0,0,0,0,0,1,1,1,1],
    [1,0,1,0,1,1,1,0,0,0,0,0,1,1,1,0,1],
    [0,1,1,1,0,0,0,1,1,1,0,1,0,0,0,1,1],
    [0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,1,1],
    [0,1,0,1,0,0,0,1,1,1,1,0,0,0,0,1,1],
    [0,1,0,1,0,0,0,1,1,1,0,1,0,0,0,1,1],
    [0,1,1,1,0,0,0,1,1,1,0,1,0,0,0,1,1],
    [1,1,0,0,1,1,0,1,1,1,0,0,1,1,1,0,1],
    [0,1,1,1,0,0,0,1,1,1,0,1,0,0,0,1,1],
    [1,0,1,0,1,1,1,0,0,0,0,0,1,1,1,0,0],
    [0,1,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1],
    [1,0,1,0,1,1,1,0,0,0,0,0,1,1,1,0,1],
    [0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,1,1],
    [1,0,1,0,1,1,1,0,0,0,0,0,1,1,1,0,0],
    [1,1,1,0,1,1,1,0,0,0,0,0,0,1,1,0,1],
    [1,0,1,0,1,1,1,0,0,0,1,0,1,1,1,0,0],
    [0,1,0,1,0,0,0,1,1,1,1,1,0,1,0,1,1],
    [0,1,0,1,0,0,0,1,1,1,0,0,0,0,0,0,1],
    [0,1,0,1,0,0,0,1,1,1,0,0,0,0,0,1,1],
    [0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,1],
    [0,1,1,1,0,0,0,1,1,0,0,0,0,0,1,0,1],
    [0,1,1,1,0,0,0,1,1,1,0,1,0,0,0,1,1],
    [1,1,1,0,1,1,1,0,0,0,1,0,1,1,1,0,0],
    [1,0,1,0,1,1,1,0,0,0,1,1,1,1,1,0,0],
    [1,0,1,0,1,1,1,0,0,0,1,1,1,1,1,0,1],
    [1,0,1,0,1,1,1,0,0,0,1,0,1,1,1,0,1],
    [1,0,1,0,1,1,1,0,0,0,1,0,1,1,1,0,1],
    [1,0,1,0,1,1,1,0,0,0,0,0,1,1,1,0,0],
    [0,1,1,1,0,0,0,1,1,1,0,1,0,0,0,0,1],
    [1,1,1,0,1,1,1,1,0,0,0,0,1,1,1,0,1],
    [1,0,1,0,1,1,1,1,0,0,0,1,1,1,1,0,1],
    [1,0,1,0,1,1,1,0,0,0,1,0,1,1,1,0,0],
    [0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,1,1],
    [1,1,1,1,1,0,0,1,1,1,1,1,0,0,1,0,1],
    [1,1,0,1,1,1,0,1,0,1,1,0,0,1,1,0,1],
    [0,1,0,1,0,0,1,1,1,1,1,1,0,0,1,1,1],
    [0,0,1,1,1,1,1,0,0,0,1,1,0,1,1,0,0],
    [0,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1],
    [0,1,1,1,0,1,1,0,0,0,1,1,0,1,1,0,1],
    [1,0,0,0,1,1,0,0,0,0,1,0,1,1,1,0,0],
    [1,0,0,0,1,1,1,0,0,0,1,0,1,1,1,0,1],
    [1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0],
    [0,0,0,1,0,1,1,0,0,0,1,1,1,1,1,0,1],
    [1,0,0,0,1,1,1,0,0,0,1,0,1,1,1,0,0],
    [1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0],
    [0,0,1,1,0,1,1,1,0,1,1,1,0,1,1,0,1],
    [0,1,0,1,0,0,0,1,1,1,1,0,0,0,0,1,1],
    [0,1,0,1,0,0,0,1,1,1,1,1,0,0,0,1,1],
    [0,1,0,1,0,0,0,1,0,1,1,1,0,0,0,1,1],
    [0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,1],
    [0,1,0,0,0,1,1,1,0,0,1,1,0,0,1,0,1],
    [0,1,1,1,0,0,1,1,1,1,1,0,0,0,0,0,1],
    [0,1,0,0,0,1,1,0,0,0,0,1,1,0,1,0,1],
    [0,1,0,1,0,1,1,1,0,0,0,1,0,0,1,0,1],
    [0,1,1,1,0,0,0,0,1,1,0,1,0,0,0,1,1],
    [1,0,1,0,1,1,1,0,0,0,0,0,1,1,1,0,1],
    [0,0,0,1,0,0,0,1,1,1,1,0,0,0,0,1,1],
    [0,1,0,1,0,0,0,1,1,1,0,1,0,0,0,1,1],
    [1,1,1,1,1,1,0,1,0,0,0,0,1,1,1,0,1],
    [0,0,1,1,0,0,0,0,1,1,1,1,0,0,0,1,1],
    [1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0],
    [1,0,0,0,1,1,1,0,0,0,1,0,1,0,1,0,1],
    [0,0,0,1,0,0,1,0,1,1,1,0,0,0,1,0,1],
    [1,0,0,0,1,1,1,0,0,0,1,0,1,1,1,0,1],
    [1,0,0,0,1,1,1,0,0,0,1,0,1,1,1,0,0],
    [1,0,1,0,1,1,1,0,0,0,1,1,1,1,0,0,1],
    [0,0,0,1,0,0,1,1,1,1,1,0,0,0,1,0,1],
    [0,1,0,1,0,0,1,1,1,1,0,0,0,0,0,1,1],
    [1,0,0,0,1,0,0,1,1,1,1,0,0,1,1,0,1],
    [1,0,0,0,1,1,1,1,1,1,1,0,1,1,1,0,1],
    [1,0,1,0,1,1,1,0,0,0,0,0,1,1,1,0,1],
    [0,0,0,0,0,0,0,1,1,1,1,0,1,1,1,1,1],
    [1,0,1,0,1,1,1,0,0,0,1,1,1,1,1,0,1],
    [0,0,0,1,0,0,0,1,1,1,1,0,0,1,0,1,1],
    [1,1,1,0,1,1,1,0,0,0,1,0,1,1,1,0,1],
    [0,0,1,1,0,0,1,0,1,1,1,1,0,1,0,1,1],
    [0,0,0,1,0,0,1,1,1,1,1,1,0,1,1,0,1],
    [1,0,1,0,1,1,1,0,0,0,0,0,1,1,1,0,0],
    [1,1,1,0,1,1,1,1,0,0,0,0,1,1,1,0,0],
    [1,0,1,0,1,1,1,0,0,0,1,0,1,1,1,0,0],
    [0,0,1,0,0,1,1,0,0,0,0,0,1,1,1,1,1],
    [0,0,0,0,0,1,1,1,0,0,0,0,1,1,1,0,1],
    [0,0,1,1,0,1,1,1,0,0,0,1,1,1,1,0,1],
    [1,0,1,0,1,1,1,1,0,0,0,0,1,1,1,0,1],
    [1,1,0,1,1,1,1,1,1,0,1,0,1,0,1,1,1],
    [1,1,0,1,1,1,1,1,1,0,1,1,1,0,1,1,1],
    [0,1,0,1,0,0,0,1,1,1,1,1,0,0,1,0,1],
    [0,0,0,0,0,1,1,0,0,0,1,1,1,1,1,0,1],
    [0,0,1,1,0,0,0,1,1,1,1,0,0,0,0,1,1],
    [1,0,0,1,1,0,0,1,1,1,1,0,0,0,1,1,1],
    [0,1,0,1,0,0,0,1,1,1,1,0,0,0,0,1,1],
    [0,0,0,1,0,0,0,1,1,1,1,1,0,0,0,1,1],
    [0,0,0,1,0,0,0,1,1,1,1,1,0,0,0,1,1],
    [0,0,1,1,0,0,0,1,1,1,1,1,0,0,0,1,1],
    [0,1,0,1,0,0,0,1,1,1,0,0,0,0,0,1,1],
    [0,0,0,0,0,0,1,1,1,1,0,1,0,0,1,1,1],
    [0,0,0,1,0,0,0,1,1,1,0,0,0,0,0,1,1],
    [0,0,0,1,0,0,0,1,1,1,0,0,0,0,1,1,1],
    [0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,1,1],
    [0,1,0,1,0,0,1,1,1,1,1,1,0,0,0,1,1],
    [0,1,0,1,0,0,0,1,1,1,1,0,0,0,0,1,1],
    [1,0,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1],
    [0,0,0,1,0,0,1,1,1,1,1,0,1,0,0,0,1],
    [1,0,0,0,1,1,1,0,0,0,1,0,1,0,1,0,1],
    [0,1,1,1,0,0,0,1,1,1,1,1,0,0,0,0,1],
    [0,0,0,1,0,0,1,1,1,1,0,0,0,0,0,1,1],
    [1,0,1,0,1,1,1,0,0,0,1,0,1,1,1,0,1],
    [0,0,0,1,0,0,0,1,1,1,0,1,0,0,0,1,1],
    [0,0,1,1,0,0,1,0,1,1,0,1,0,1,0,1,1],
    [1,1,1,0,1,1,1,0,0,0,1,0,1,1,1,0,1],
    [1,0,1,0,1,1,1,0,0,0,1,0,1,1,1,0,0],
    [0,0,1,1,0,0,0,0,1,1,0,1,0,0,1,1,1],
    [1,0,0,0,1,1,0,0,0,0,0,0,1,1,1,0,1],
    [0,0,0,1,0,0,1,1,1,1,0,1,0,0,1,1,1],
    [1,0,1,1,1,1,1,1,0,1,1,0,1,1,1,0,1],
    [1,0,1,0,1,1,1,0,0,0,0,0,1,1,1,0,1],
    [1,0,1,0,1,1,1,0,0,1,1,0,1,1,1,0,1],
    [1,0,1,0,1,1,1,0,0,0,1,0,1,1,1,0,1],
    [1,0,0,0,1,1,1,0,0,0,1,0,1,0,1,0,1],
    [0,0,0,1,0,0,0,1,1,1,0,0,0,0,0,1,1],
    [0,1,0,1,0,0,1,1,1,0,0,0,1,1,0,0,1],
    [1,0,0,0,1,1,1,1,0,0,1,0,0,0,1,1,1],
    [0,1,0,1,0,0,0,1,1,1,1,1,0,0,1,1,1],
    [0,1,0,1,0,0,0,0,1,1,1,0,0,0,0,1,1],
    [0,1,0,1,0,0,0,1,1,1,1,1,0,0,0,1,1],
    [1,0,1,0,1,1,1,0,0,0,0,0,1,1,1,0,0],
    [1,0,1,0,1,1,1,0,0,0,0,0,1,1,1,0,0],
    [0,1,1,1,0,0,1,1,1,1,0,0,0,0,0,1,1],
    [1,0,1,0,1,1,1,0,0,0,0,0,1,1,1,0,1],
    [0,1,0,1,0,0,0,1,1,1,1,0,0,0,0,0,1],
    [0,1,0,1,0,0,0,1,1,1,1,0,0,0,1,1,1],
    [1,0,0,0,1,1,0,0,0,0,0,0,1,0,1,0,0],
    [0,0,0,1,0,0,0,1,1,1,0,1,0,0,0,1,1],
    [0,1,0,1,0,0,0,1,1,1,0,0,0,0,0,0,1],
    [0,1,0,1,0,0,0,1,1,1,1,0,0,0,0,0,1],
    [0,1,0,1,0,0,0,1,1,1,1,0,0,0,0,0,1],
    [1,0,0,0,1,1,1,0,0,0,1,0,1,0,1,0,1],
    [1,1,0,0,0,0,0,1,1,1,1,0,0,0,1,0,1],
    [0,1,0,1,0,0,0,1,1,1,0,0,0,0,0,0,1],
    [0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,1,1],
    [1,1,0,0,1,1,0,1,0,0,1,0,0,0,1,1,1],
    [1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,1,0],
    [1,0,0,1,1,1,1,1,1,0,1,0,0,0,1,0,1],
    [1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,1],
    [1,0,0,0,1,1,1,0,0,0,1,0,1,1,1,0,0],
    [0,0,0,1,0,0,0,1,1,1,1,0,0,0,1,0,1],
    [1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,1],
    [0,0,0,1,0,0,1,1,1,1,1,1,0,0,0,1,1],
    [0,1,1,1,0,1,1,0,1,0,1,1,0,1,1,1,1],
    [0,1,0,1,0,0,1,1,1,0,1,1,0,1,1,1,1],
    [0,1,1,1,0,0,1,1,1,1,1,1,0,1,1,1,1],
    [1,0,0,1,1,1,1,0,0,0,1,0,1,1,1,1,1],
    [0,0,1,0,0,0,0,1,1,1,1,1,0,0,0,1,1],
    [0,0,1,1,0,0,1,1,1,1,1,0,0,1,1,1,1],
    [1,0,0,0,1,1,0,1,1,1,1,0,1,1,1,0,1],
    [1,0,0,0,1,1,1,1,0,0,1,0,1,1,1,0,1],
    [1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0],
    [1,0,0,0,1,1,1,0,0,0,1,0,1,1,1,0,0],
    [1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0],
    [1,0,0,0,1,1,1,0,0,0,1,0,1,1,1,0,0],
    [0,1,0,0,0,0,1,1,1,1,1,0,0,0,1,1,1],
    [1,0,0,0,1,1,1,0,0,0,1,0,1,1,1,1,0],
    [0,0,0,1,0,0,1,1,1,1,1,0,0,1,0,0,1],
    [0,1,1,1,0,0,0,1,1,1,1,0,0,0,0,1,1],
    [1,0,1,1,1,1,1,0,0,0,1,0,1,1,1,0,1],
    [1,0,1,0,1,1,1,1,1,0,0,1,1,1,1,1,1],
    [0,0,0,0,0,0,1,0,1,1,0,1,1,1,1,1,0],
    [0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,1,1],
    [0,0,1,1,0,0,1,0,1,1,1,0,0,1,1,0,1],
    [0,1,1,1,0,0,0,1,1,1,1,0,0,1,0,0,1],
    [1,0,1,0,1,1,1,0,0,0,0,1,1,1,1,0,0],
    [0,1,1,0,1,0,0,1,1,1,0,1,0,0,1,0,1],
    [1,0,1,0,1,1,1,0,0,0,0,0,1,1,1,0,1],
    [0,1,1,1,0,0,0,1,1,1,0,1,0,0,0,0,1],
    [1,0,1,0,1,1,1,0,0,0,1,0,1,1,1,0,0],
    [0,0,0,1,0,0,0,1,1,1,0,0,0,0,0,1,1],
    [0,1,0,1,0,0,0,1,1,1,0,0,0,0,0,1,1],
    [0,1,0,1,0,0,0,1,1,1,1,0,0,0,1,1,1],
    [1,1,0,0,1,1,1,0,0,0,0,1,1,1,1,0,0],
    [1,0,0,0,1,1,1,0,0,0,1,1,1,0,1,0,1],
    [1,0,0,0,1,1,0,1,0,1,1,0,0,0,1,0,1],
    [0,0,0,1,0,0,0,1,1,1,1,1,0,0,0,1,1],
    [1,0,0,0,1,1,1,1,0,0,1,0,1,0,1,1,1],
    [1,0,0,0,1,1,1,0,0,0,1,0,1,1,1,0,1],
    [1,1,0,0,1,1,1,0,0,0,1,0,1,1,1,0,0],
    [1,0,1,1,1,1,1,1,1,1,0,0,1,1,1,0,1],
    [0,0,1,0,0,0,1,1,0,1,0,1,0,0,0,1,1],
    [1,0,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1],
    [1,0,0,1,1,1,1,1,0,0,1,1,1,1,1,0,1],
    [1,1,0,1,1,0,0,0,1,1,1,0,0,0,1,1,1],
    [1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0],
    [1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0],
    [0,1,0,1,0,0,1,1,1,1,1,0,0,1,0,0,1],
    [0,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,1],
    [1,1,1,0,1,1,1,0,0,0,1,1,0,1,0,0,0],
    [1,1,1,0,1,1,1,0,0,0,0,1,0,1,1,0,1],
    [0,0,1,0,0,1,1,0,0,0,1,1,0,1,1,0,0],
    [0,0,1,1,0,0,1,1,1,0,1,0,0,0,0,1,1],
    [1,0,1,0,1,1,1,0,0,0,0,0,0,1,1,0,1],
    [1,0,1,0,1,1,1,0,0,0,0,0,1,1,1,0,1],
    [0,0,1,0,1,1,1,0,0,0,0,1,1,0,1,0,0],
    [1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,1],
    [1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,1],
    [0,1,1,1,0,1,1,0,1,1,1,1,0,0,0,0,1],
    [0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,0,1],
    [0,1,1,0,0,1,1,0,0,0,0,1,1,1,1,1,0],
    [0,1,1,0,0,0,0,0,1,1,0,1,0,0,0,1,0],
    [1,1,1,0,1,1,1,0,0,0,0,1,1,1,1,0,1],
    [0,1,1,1,0,1,1,0,1,0,0,1,0,1,0,1,1],
    [0,0,1,1,0,1,1,0,1,0,0,0,0,0,0,0,1],
    [1,0,1,0,1,1,1,0,0,0,1,1,1,1,1,0,0],
    [1,1,1,0,1,1,1,0,0,0,1,0,1,1,1,0,1],
    [1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,1],
    [0,1,0,1,0,1,1,0,0,1,1,0,0,1,1,0,1],
    [0,0,0,0,1,1,1,0,0,0,0,1,1,1,1,0,0],
    [1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0],
    [1,0,0,0,1,1,1,0,0,0,0,1,1,1,1,0,1],
    [0,1,0,1,0,0,1,1,1,1,1,1,0,0,0,0,1],
    [1,0,0,0,1,1,1,0,0,0,1,0,1,1,1,0,1],
    [0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,1],
    [1,1,1,0,1,1,1,0,0,0,1,0,0,1,1,0,1],
    [0,1,1,1,0,0,0,1,1,1,1,1,0,1,0,0,1],
    [0,1,1,1,0,0,0,1,1,0,1,0,0,0,0,0,1],
    [0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,0,1,0,0,1,1,0,1],
    [0,0,1,1,0,1,1,1,1,0,0,1,0,1,0,1,1],
    [0,0,0,1,0,0,1,1,1,1,0,1,0,0,0,1,1],
    [0,0,1,1,0,0,1,1,1,1,0,1,0,0,1,1,1],
    [0,1,0,1,0,0,0,1,1,1,1,0,0,0,0,1,1],
    [1,0,0,0,1,1,1,1,1,0,1,0,1,1,1,0,1],
    [1,0,0,1,1,1,1,0,0,1,1,0,1,1,1,0,1],
    [0,0,0,1,0,0,0,1,1,1,1,0,0,0,0,0,1],
]

def remainder(value):
    p_k = 0
    n_k = 0
    res = 0
    total = len(table)
    for i in range(len(table)):
        if table[i][value] == 1:
            p_k += 1
        else:
            n_k += 1
    for i in range(2):
        res += (p_k + n_k)/(total)*B(p_k/total)

    return res
    
def B(q):  
  if q==0 or q==1:
    return 0
  return -(q*log2(q)+(1-q)*log2(1-q))

classatt = range(17)
pos=[ sum([table[j][i]    for j in range(len(table))]) for i in classatt ] 
neg=[ sum([table[j][i]==0 for j in range(len(table))]) for i in classatt ] 


print(remainder(2))