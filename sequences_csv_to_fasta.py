import pandas as pd

fold = '4H'
_4H = pd.read_csv('4H_NGS_filtered.csv', header=0)
print(_4H)

with open('4H_sequences.txt', 'w') as save_file:  
    for i in range(len(_4H['seq'])):
        save_file.write('>{}.{}\n{}\n'.format(fold,i,_4H['seq'][i]))
