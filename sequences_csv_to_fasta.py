import pandas as pd

NGS_file = str(input('Name of csv file containing NGS sequence data => ")).strip()
NGS_data = pd.read_csv(NGS_file, header=0)
print(NGS_data)

for i in range(len(NGS_data['seq'])):
    with open('ngs_seq_{}.fasta'.format(i), 'w') as save_file:  
        save_file.write('>NGS_seq_{}\n{}\n'.format(i,NGS_data['seq'][i]))
