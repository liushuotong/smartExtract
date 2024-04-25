# smartView
a tool to visualize the data coming from smart online database

## Author info

liushuotong SDUW 2024

<https://github.com/liushuotong>

## Invironment

- python version: 3.11.6

## Tips

**"smart" is not cleaver!!!**

"smart" means **Simple Modular Architecture Reseach Tools**.

## Example

```bash
smartView -h/--help       # show help message
smartView -v/--view       # process data and show result
smartView -c/--config     # show config message
```

## Fuction list

```Python
def show_help()
    """
    Displays the help message for smartView.

    This function prints a message that provides information about smartView, the author, the Python version used, and a disclaimer about the term "smart". It also provides instructions on how to use smartView by specifying the command line arguments. Finally, it prompts the user to press enter to exit.

    Parameters:
        None

    Returns:
        None
    """
def config_message()
    """
    Displays the configuration message for smartView.

    This function prints a message that provides information about the configuration of smartView, the author, the version, and the GitHub repository. It prompts the user to press enter to exit.

    Parameters:
        None

    Returns:
        None
    """
def process()

def extract_based_on_domain(results)
    """
    Extracts unique domains from the given results and splits the data based on the domains.

    Parameters:
    - results (list): A list of dictionaries representing the results.

    Returns:
    None
    """
def split_fasta(sequences)
    """
    A function that splits the sequences based on domain data and writes them to separate files.
    
    Args:
        sequences (dict): A dictionary containing the sequences.
        
    Returns:
        None
    """
def fasta_len(sequences_dict):
    """
    Calculate the length of each sequence in a FASTA file and return a dictionary with the sequence names as keys and their lengths as values.

    Args:
        sequences_dict (dict): A dictionary containing the sequences, where the keys are the sequence names and the values are the sequences.

    Returns:
        dict: A dictionary containing the sequence names as keys and their lengths as values.
    """
def parse_smart_results(text)
    """
    Parses the SMART results from a given text and organizes the matching results into data structures.

    Args:
        text (str): The text containing the SMART results.

    Returns:
        list: A list of dictionaries, where each dictionary represents a protein and its associated features. The dictionary has the following structure:
            - "USER_PROTEIN_ID" (str): The user protein ID.
            - "SMART_PROTEIN_ID" (str): The SMART protein ID.
            - "NUMBER_OF_FEATURES_FOUND" (int): The number of features found for the protein.
            - "FEATURES" (list): A list of dictionaries, where each dictionary represents a feature and its associated information. The dictionary has the following structure:
                - "DOMAIN" (str): The domain of the feature.
                - "START" (int): The start position of the feature.
                - "END" (int): The end position of the feature.
                - "EVALUE" (float): The e-value of the feature.
                - "TYPE" (str): The type of the feature.
                - "STATUS" (str): The status of the feature.

    Raises:
        None
    """
```
