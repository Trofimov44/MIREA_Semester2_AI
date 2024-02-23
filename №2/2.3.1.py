import numpy as np
import pandas as pd
point_1 = pd.array((0, 0, 0))
point_2 = pd.array((2, 3, 3))
square = np.square(point_1 - point_2)
distance = np.sum(square)
print(distance)
