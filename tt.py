import numpy as np

p = np.ones([100, 3, 512, 512],dtype=np.float16)
print(p.nbytes, p.shape,p.dtype)
a = np.ones([1464100, 3, 32, 32])
print(a.nbytes,a.shape)


