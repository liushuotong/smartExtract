'''smartView
dataType_summary:
    +--------------------------------------------------------------------------------------------------------------+
    |      # domain_extract.py                                                                                     |
    |      # liushuotong SDUW 2024.4.24                                                                            |
    |      # version 1.0                                                                                           |
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
processingMethod_summary:                                                   +------------------+
        +------------------------+              +--------------+            | >user_protein_id |
        | based on 'DOMAIN' name |  ------->    | builb a file |  ------->  | domain_sequence  |
        +------------------------+              +--------------+            |  ......          |
                                                                            | >......          |
                  +---+                                                     +------------------+
                  |   |                                                              ./\.
                  |   |                                                              //\\
                  |   |                                                             //  \\
                 \\   //                                                           //    \\     
                  \\ //                                                           //      \\  
                   \V/                                                             |      |
                    V                                                              |      |
                                                                                   +      +
        +------------------------+              +------------------------+        /      /
        |                        |  +-------\\  |   domain combinate to  |  +----+      /
        |     'DOMAIN' name      |  |        \\ |   user_protein_id      |  |          /
        |         list           |  |        // |   throught 'results'   |  |         /
        |                        |  +-------//  |   with start and end   |  +--------+
        +------------------------+              +------------------------+

'''

# Use a set to store unique domains
unique_domains = set()
# Create a dictionary to store the split data
domain_data = {}

def extract_based_on_domain(results):
    """
    Extracts unique domains from the given results and splits the data based on the domains.

    Parameters:
    - results (list): A list of dictionaries representing the results.

    Returns:
    None
    """

    # Iterate through data to get all different domains
    for entry in results:
        features = entry.get('FEATURES', [])
        for feature in features:
            # Get domain
            domain = feature.get('DOMAIN', '')
            unique_domains.add(domain)

    # Create new dictionaries for different domains
    for domain in unique_domains:
        domain_data[domain] = []

    # Iterate through data to fill the split dictionaries
    for entry in results:
        # Get domain data
        features = entry.get('FEATURES', [])
        for feature in features:
            domain = feature.get('DOMAIN', '')
            domain_entry = {
                'USER_PROTEIN_ID': entry.get('USER_PROTEIN_ID', ''),
                'START': feature.get('START', ''),
                'END': feature.get('END', '')
            }
            domain_data[domain].append(domain_entry)


def split_fasta(sequences):
    """
    A function that splits the sequences based on domain data and writes them to separate files.
    
    Args:
        sequences (dict): A dictionary containing the sequences.
        
    Returns:
        None
    """
    PATH_ = input('Path to release the domain sequences: ')
    # Iterate through unique domains
    for domain in unique_domains:
        print(f"Processing domain: {domain}")
        # Iterate through keys in sequences
        file_name = domain.replace(':', '_')
        with open (PATH_ + file_name + '.fasta', 'a') as f:
            for entry in domain_data[domain]:
                # Get user_protein_id and start and end info
                user_protein_id = entry['USER_PROTEIN_ID']
                start = int(entry['START'])
                end = int(entry['END'])
                # Check if user_protein_id is in sequences
                if user_protein_id in sequences:
                    f.write('>' + entry['USER_PROTEIN_ID'] + '\n' + sequences[user_protein_id][start - 1:end] + '\n')
        print()

