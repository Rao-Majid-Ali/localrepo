import numpy as np

# print(np.__version__)
# np.show_config()

# z = np.zeros(10)
# z[5] = 1
# print(z)

# f =  np.eye(5,5)
# f[:,0:]=1
# f[1:4,1:-1]=0
# print(f)

# z = np.linspace(0,1,25).reshape(5,5)


# print(z)

a = np.random.random((5,3))
b = np.random.random((3,2))

c = np.dot(a, b)

print(c)
