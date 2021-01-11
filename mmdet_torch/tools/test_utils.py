from pathlib import Path
import numpy as np
import os

p = Path('feature.npy')
# with p.open('ab') as f:
#     np.save(f, np.zeros(2))
#     np.save(f, np.ones(2))

with p.open('rb') as f:
    fsz = os.fstat(f.fileno()).st_size
    out = np.load(f)
    print(out)
    while f.tell() < fsz:
        print(np.load(f))
        # out = np.vstack((out, np.load(f)))

    # print(out)
    # print(out.shape)
