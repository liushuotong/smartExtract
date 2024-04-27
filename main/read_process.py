#! /usr/bin python
# -*- coding: utf-8 -*-
import re
'''
read_process.py version 1.1
liushutong SDUW 2024.4.27

python version: 3.11.6

in this version
smartViwe will have tha ability to indentify different transcripts
'''

def read_fasta(file_path):
    """
    same as version 1.0
    Reads a FASTA file and returns a dictionary containing the sequences.

    Args:
        file_path (str): The path to the FASTA file.

    Returns:
        dict: A dictionary where the keys are the sequence names and the values are the sequences.

    """
    # Dictionary to store sequences
    sequences = {}

    # Open the file for reading
    with open(file_path, 'r') as f:
        # Variables to store current sequence name and sequence
        sequence_name = ''
        sequence = ''

        # Iterate through each line in the file
        for line in f:
            # Strip any leading/trailing whitespace
            line = line.strip()

            # Check if the line starts with '>'
            if line.startswith('>'):
                # If a sequence has been read, add it to the dictionary
                if sequence_name:
                    sequences[sequence_name] = sequence
                # Update sequence name for the new sequence
                sequence_name = line[1:]
                # Reset sequence string
                sequence = ''
            else:
                # If line doesn't start with '>', append it to the current sequence
                sequence += line

        # Add the last sequence (if any) to the dictionary
        if sequence_name:
            sequences[sequence_name] = sequence

    # Return the dictionary containing all sequences
    return sequences

def fasta_len(sequences_dict):
    """
    Calculate the length of each sequence in a FASTA file and return a dictionary with the sequence names as keys and their lengths as values.

    Args:
        sequences_dict (dict): A dictionary containing the sequences, where the keys are the sequence names and the values are the sequences.

    Returns:
        dict: A dictionary containing the sequence names as keys and their lengths as values.
    """
    # Dictionary to store sequence lengths
    len_dict = {}

    # Iterate through each key-value pair in the input dictionary
    for key, value in sequences_dict.items():
        # Calculate the length of the sequence and store it in the length dictionary
        len_dict[key] = len(value)

    # Return the dictionary containing sequence lengths
    return len_dict

def smart_txt_read(smart_txt_location):
    """
    Reads a SMART text file and extracts protein data and features.

    Args:
        smart_txt_location (str): The location of the SMART text file.

    Returns:
        list: A list of dictionaries containing parsed protein data.

    """
    with open(smart_txt_location, 'r') as f:
        smart = f.read()
    
    # Define the regular expression pattern to match "NOT_MATCH"
    pattern_not_match_check = r'NO_MATCH:([\w\s.]+)'

    # Use the regular expression to find a match in the text
    match = re.search(pattern_not_match_check, smart)

    # Extract the matched string and split it into a list
    if match:
        not_match_str = match.group(1).strip()
        not_match_list = not_match_str.split(', ')
    else:
        not_match_list = []

    # Warning if not_match_list is not empty
    if len(not_match_list) != 0:
        print("Warning: Below protein ID(s) didn't match the domains.")
        for i in not_match_list:
            print(i)
    else:
        print("All proteins matched the domains.")

    pattern = r'USER_PROTEIN_ID = ([\S\s]+?)\nSMART_PROTEIN_ID = (\S+)\nNUMBER_OF_FEATURES_FOUND=(\d+)\n\n(.*?)\n\n-- FINISHED --'
    
    # Matching text with raw regular expressions
    matches = re.findall(pattern, smart, re.DOTALL)

    # Organize matching results into data structures
    results = []
    for match in matches:
        user_protein_id = match[0]
        smart_protein_id = match[1]
        number_of_features_found = int(match[2])
        features_text = match[3]

        # Define feature extraction pattern
        feature_pattern = r'DOMAIN=(\S+)\nSTART=(\d+)\nEND=(\d+)\nEVALUE=(\S+)\nTYPE=(\S+)\nSTATUS=(\S+)'
        features = re.findall(feature_pattern, features_text)

        # Check that the number of features matched is consistent with NUMBER_OF_FEATURES_FOUND
        if len(features) == number_of_features_found:
            protein_data = {
                "USER_PROTEIN_ID": user_protein_id,
                "SMART_PROTEIN_ID": smart_protein_id,
                "NUMBER_OF_FEATURES_FOUND": number_of_features_found,
                "FEATURES": []
            }
            for feature in features:
                protein_data["FEATURES"].append({
                    "DOMAIN": feature[0],
                    "START": int(feature[1]),
                    "END": int(feature[2]),
                    "EVALUE": float(feature[3]),
                    "TYPE": feature[4],
                    "STATUS": feature[5]
                })
            results.append(protein_data)
        else:
            print(f"Warning: Number of features found ({len(features)}) does not match NUMBER_OF_FEATURES_FOUND ({number_of_features_found}) for protein ID {user_protein_id}")

    return results