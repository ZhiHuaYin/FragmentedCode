import numpy as np
import pandas as pd

a = np.array([['Pman', 'Species'], ['Wartortle', 'Turtle'], ['Venusaur', 'Turtle'], ['Charmeleon', 'Flame']])
a = pd.DataFrame(a)


b = np.array([[0.1, 0.2, 0.5, 0.9], [0.2, 0.1, 5.0, 0.2], [0.4, 0.1, 7.0, 0.8]])
b = pd.DataFrame(b)

with open("metadata.tsv", 'w') as write_data:
    write_data.write(a.to_csv(sep='\t', index=False, header=False))

with open("data.tsv", 'w') as write_data:
    write_data.write(b.to_csv(sep='\t', index=False, header=False))
