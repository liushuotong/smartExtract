from matplotlib import pyplot as plt
from matplotlib import colors as mcolors
'''smartView
dataType_summary:
+--------------------------------------------------------------------------------------------------------------+
|    # liushuotong SDUW 2024.4.24                                                                              |
|    # version 1.0                                                                                             |
+--------------------------------------------------------------------------------------------------------------+
|   sequences -> a dictionary containing the sequences                                                         |
|   example:                                                                                                   |
|   'id_name':'MSANIHUBILHLGHFJK'                                                                              |
+--------------------------------------------------------------------------------------------------------------+
|   len_dict -> a dictionary containing the sequence names as keys and their lengths as values                 |
|    example:                                                                                                  |
|   'id_name':'12'                                                                                             |
+--------------------------------------------------------------------------------------------------------------+
|   results -> a list of dictionaries, where each dictionary represents a protein and its associated features  |
|   example:                                                                                                   |
|   [{                                                                                                         |
|       'USER_PROTEIN_ID': 'transcript:TraesCSU02G058300.1',                                                   |
|       'SMART_PROTEIN_ID': 'uniprot|A0A1D5WM65|A0A1D5WM65_WHEAT',                                             |
|       'NUMBER_OF_FEATURES_FOUND': 2,                                                                         |
|       'FEATURES':[                                                                                           |
|           {                                                                                                  |
|               'DOMAIN': 'Pfam:Dimerisation',                                                                 |
|               'START': 36,                                                                                   |
|               'END': 84,                                                                                     |
|               'EVALUE': 9.3e-12,                                                                             |
|               'TYPE': 'PFAM',                                                                                |
|               'STATUS': 'visible|OK'                                                                         |
|           },{                                                                                                |
|               'DOMAIN': 'Pfam:Methyltransf_2',                                                               |
|               'START': 135,                                                                                  |
|               'END': 364,                                                                                    |
|               'EVALUE': 2.1e-60,                                                                             |
|              'TYPE': 'PFAM',                                                                                 |
|               'STATUS': 'visible|OK'                                                                         |
|           }]                                                                                                 |
|   },{                                                                                                        |
|               ......                                                                                         |
|   }]                                                                                                         |
+--------------------------------------------------------------------------------------------------------------+
|   unique_domains -> a set to store unique domains                                                            |
|   example: unique_domains.add('Pfam:Dimerisation')                                                           |
+--------------------------------------------------------------------------------------------------------------+
'''
def select_color(unique_domains):
    color_dict = {}
    i = 0
    xkcd_colors = list(mcolors.XKCD_COLORS.keys())
    for domain in unique_domains:
        color_dict[domain] = xkcd_colors[i]