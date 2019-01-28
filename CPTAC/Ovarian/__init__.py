

import pandas as pd
import numpy as np
import glob
import os
import textwrap
import webbrowser


def warning():
    print("\n","******PLEASE READ******")
    #TODO: What is the embargo date for the ovarian cancer data?
    warning = "WARNING: This data is under a publication embargo until July 1, 2019. CPTAC is a community resource project and data are made available rapidly after generation for community research use. The embargo allows exploring and utilizing the data, but the data may not be in a publication until June 1, 2019. Please see https://proteomics.cancer.gov/data-portal/about/data-use-agreement or enter embargo() to open the webpage for more details."
    wrapped_list = textwrap.wrap(warning)
    for line in wrapped_list:
        print(line)

def read_data(fileName):
    df = None
    f = fileName.split(os.sep)
    f = f[len(f) - 1]
    name = f.split(".")[0]
    print("Loading",name,"data...")
    if name != "clinical":
        df = pd.read_csv(fileName, sep="\t", index_col=0)
    else:
        df = pd.read_csv(fileName, sep="\t")
    df.name = name
    return df

dir_path = os.path.dirname(os.path.realpath(__file__))
data_directory = dir_path + os.sep + "Data" + os.sep
path = data_directory + os.sep + "*.*"
files = glob.glob(path)
data = {}
print("Loading Ovarian CPTAC data:")
for file in files:
    df = read_data(file)
    data[df.name] = df
warning()


def get_data():
    return data
def get_clinical():
    return data.get("clinical")

def get_cnv():
    return data.get("cnv")

def get_phosphoproteomics():
    return data.get("phosphoproteomics")

def get_proteomics():
    return data.get("proteomics")

def get_somatic_mutations():
    return data.get("somatic_19") #TODO: how to handle different somatic files?

def get_transcriptomics():
    return data.get("transcriptomics")


def embargo():
    """
    Parameters
    None

    Opens CPTAC embargo details in web browser

    Returns
    None
    """
    print("Opening embargo details in web browser...")
    webbrowser.open("https://proteomics.cancer.gov/data-portal/about/data-use-agreement")
def version():
    version = {}
    with open(dir_path + os.sep + ".." + os.sep + "version.py") as fp: #.. required to navigate up to CPTAC folder from Endometrial folder
    	exec(fp.read(), version)
    return(version['__version__'])
