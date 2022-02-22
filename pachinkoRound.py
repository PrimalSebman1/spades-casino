import numpy as np
def rounder(r):
  check = float(int(r))
  c = r - check
  if (c < 0.5):
    r = np.floor(r)
    r = int(r)
    return r
  else:
    r = np.ceil(r)
    r = int(r)
    return r
