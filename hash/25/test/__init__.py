INPUT = [
    [
        ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],
        [2,3,4],	
    ],
    [
        ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],
        [2,3,5],    
    ],
    [
        ["XYZ", "XWY", "WXA"],
        [2,3,4],
    ]
];

OUTPUT = [
    ["AC", "ACDE", "BCFG", "CDE"],
    ["ACD", "AD", "ADE", "CD", "XYZ"],
    ["WX", "XY"],
]