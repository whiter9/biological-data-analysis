# -*- coding: utf-8 -*-
"""
Biopython program to iteratively run NCBI BLAST query on a set of input protein sequences

Ref: https://biopython-tutorial.readthedocs.io/en/latest/notebooks/07%20-%20Blast.html

"""

from Bio import SeqIO
from Bio.Blast import NCBIWWW, NCBIXML
import pandas as pd


if __name__ == "__main__":
    
    #################################################################
    # READ SEQUENCE INPUT
    #################################################################
    
    """
    file = str(input("Name of input FASTA file: ")).strip()
    print("\nProcessing {}...\n".format(file))
    pdb_id = file[:6]
    print(pdb_id)
    
    seq_data = next(SeqIO.parse(open(file), 'fasta'))
    sequence = seq_data.seq
    print(sequence)
    """
    seq_prefix = "3E2H"
    fold_data = pd.read_csv('3E2H_NGS_filtered.csv', header=0)
    
    ##################################################################
    # BLAST SEQUENCES
    #################################################################
    for i in range(len(fold_data['seq'])):
        sequence = fold_data['seq'][i]
        results = NCBIWWW.qblast("blastp", "nr", sequence)
        
        with open('{}.{}_blast_results.xml'.format(seq_prefix,i), 'w') as save_file: 
          blast_results = results.read() 
          save_file.write(blast_results)
    
    #################################################################
    # PARSE RESULTS
    #################################################################
    top_match = []
    e_value = []
    e_nearest_match = []
    
    for i in range(len(fold_data['seq'])):        
        record = NCBIXML.read(open("{}.{}_blast_results.xml".format(seq_prefix,i)))
        
        if record.alignments:
            #Print results:
            #for i in range(len(record.alignments)):
            #   align = record.alignments[i]
            #for hsp in align.hsps:
            #   print("match {}: {} | {}".format(i,align.hit_id,hsp.expect))
            
            match1 = record.alignments[0].hit_id
            e1 = record.alignments[0].hsps[0].expect
            if len(record.alignments)>1 and record.alignments[1].hsps:
                e2 = record.alignments[1].hsps[0].expect
            else: e2 = -1
          
            top_match.append(match1)
            e_value.append(e1)
            e_nearest_match.append(e2)
       
        else:
            print("Record not accessible for sequence {}.{}: {}".format(seq_prefix,i,fold_data['seq'][i]))
            top_match.append('None')
            e_value.append(-1)
            e_nearest_match.append(-1)            
        
    final_res = {}
    final_res['Sequence'] = fold_data['seq']
    final_res['Top match'] = top_match
    final_res['E-value'] = e_value
    final_res['E-value for next-best match'] = e_nearest_match
    
    res = pd.DataFrame(data=final_res)
    res
    
    res.to_csv('3E2H_blast_results.csv')
