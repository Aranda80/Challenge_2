# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
from pathlib import Path

def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(data,output_path):
    """Creates a csv file that will hold the qualifying loans information in the path inputted
    by the user in the save_qualifying_loans function"""
    
    header = ["Lender","Max Loan Amount","Max LTV","Max DTI","Min Credit Score","Interest Rate"]

    with open(Path(output_path), "w", newline='') as csvfile:
         csvwriter = csv.writer(csvfile, delimiter=',')
         csvwriter.writerow(header)
         csvwriter.writerows(data)