"""
Biopython program to download a batch of PDB files 
in .pdb format, given a list of PDB IDs

"""

from Bio.PDB import * #PDBList

# PDBs to download:
ids = "6EGP,6UCX,6UD9,6UDW,6UDZ,6UDR,6UFA,6UF8,6UF7,6UF9,6UG2,6UFU,6YPI,6YQY,6YQX,7A8S,6W90,7OCM,6TJG,6QSE,6QSD,6QSG,6REM,6REO,6RLI,6RLH,7JRQ,7JRH,7AWZ,7AWY,6MCD,6W3W,6Y7P".lower().split(",")
print(ids)

####################################################
#if __name__ == "__main__":
    