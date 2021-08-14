"""
Biopython program to generate a new PDB file containing only the 
specified chain or chains of an existing PDB entry.

"""

from Bio.PDB import * #PDBList, PDBIO, Select

class KeepChains(Select):
    """ Only accept the specified chains when saving. """
    def __init__(self, chain_letters):
        self.chain_letters = ch6ywd
    def accept_chain(self, chain):
        return (chain.get_id() in self.chain_letters)
    #Ref: https://stackoverflow.com/questions/11685716/how-to-extract-chains-from-a-pdb-file

####################################################
if __name__ == "__main__":
    
    #take input of pdb and chain specifications 
    
    pdb_id = str(input('\nPDB ID of target structure: '))
    keep_chains = str(input('\nLetter identifier(s) of chain(s) to keep,\
                            \nseparated by commas if multiple: '))
   
    pdb_id = pdb_id.strip().upper()
    pdb_id_lc = pdb_id.lower()
    keep_chains = keep_chains.strip().upper().split(",")
    
    # download pdb file to current dir
    pdbl = PDBList()
    pdbl.retrieve_pdb_file(pdb_id, pdir = '.', file_format = 'pdb')
    
    # load structure from pdb file
    parser = PDBParser(PERMISSIVE = True, QUIET = True)
    structure = parser.get_structure("{}","pdb{}.ent".format(pdb_id_lc,pdb_id_lc))
    
    ###############################################
    # select specific chains 
    # and export to new truncated pdb file
    ###############################################
    
    io = PDBIO()
    io.set_structure(structure)
    chains_id = "".join(keep_chains)
    io.save("{}_{}.pdb".format(pdb_id,chains_id), select=KeepChains(keep_chains))
    
   
    
    
    

