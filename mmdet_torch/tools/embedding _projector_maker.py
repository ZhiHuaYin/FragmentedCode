import pandas as pd

from pathlib import Path
import numpy as np
import os

p = Path('gt_labels.npy')
with p.open('rb') as f_a:
    fsz = os.fstat(f_a.fileno()).st_size
    out_a = np.load(f_a)
    while f_a.tell() < fsz:
        out_a = np.concatenate((out_a, np.load(f_a)))

a = np.array(out_a)
print(np.max(a))
print(np.min(a))
# 48523
print(a.shape)
a = pd.DataFrame(a)

with open("metadata.tsv", 'w') as write_data:
    write_data.write(a.to_csv(sep='\t', index=False, header=False))

  p = Path('feature.npy')
  with p.open('rb') as f_b:
      fsz = os.fstat(f_b.fileno()).st_size
      out_b = np.load(f_b)
      while f_b.tell() < fsz:
          out_b = np.concatenate((out_b, np.load(f_b)), axis=0)
#
  b = np.array(out_b)
  print(b.shape)
  b = pd.DataFrame(b)

  with open("data.tsv", 'w') as write_data:
      write_data.write(b.to_csv(sep='\t', index=False, header=False))