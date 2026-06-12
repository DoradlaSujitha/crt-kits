"""import numpy as np
zero=np.array(10)
print(zero)
print(type(zero))
print("Dimension:",zero.ndim)
print("Memory:",zero.nbytes)
one=np.array([21,23,24,25,26,27,29,30])
print(one)
print(type(one))
print("Dimension:",one.ndim)
print("Memory:",one.nbytes)
two=np.array([[21,23],[24,25],[26,27],[29,30]])
print(two)
print(type(two))
print("Dimension:",two.ndim)
print("Memory:",two.nbytes)
three=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(three)
print(type(three))
print("Dimension:",three.ndim)
print("Memory:",three.nbytes)"""

#creation
"""import numpy as np
a=np.array([1,2,3,4,5])
z=np.zeros(6)
o=np.ones((2,3))
r=np.arange(0,10,2)
l=np.linspace(0,1,5)
rd=np.random.randint(1,100,6)
print(a)
print(z)
print(o)
print(r)
print(l)
print(rd)"""

# Vectorized Math
"""import numpy as np
a = np.array([1, 2, 3, 4, 5])
print("Original array:", a)
print("a + 10 =", a + 10)
print("a * 2 =", a * 2)
print("Square root =", np.sqrt(a))
print("Square =", np.square(a))
print("Clipped values =", np.clip(a, 2, 4))
"""

# Statistics
"""import numpy as np
a = np.array([1, 2, 3, 4, 5])
print("\nMean =", np.mean(a))
print("Median =", np.median(a))
print("Standard Deviation =", np.std(a))
print("25th Percentile =", np.percentile(a, 25))
print("50th Percentile =", np.percentile(a, 50))
print("75th Percentile =", np.percentile(a, 75))"""

#shape/reshape
"""import numpy as np
a = np.array([1, 2, 3, 4, 5])
print("reshape:",a.reshape(5,1))
print("shape:",a.shape)
print("type:",a.dtype)
print("astype:",a.astype(float))"""
