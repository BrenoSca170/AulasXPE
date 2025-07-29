import pandas as pd
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]
y3 = [3, 6, 9, 12, 15]
plt.plot(x, y1,label='Série')
plt.plot(x, y2,label='Série 2')
plt.plot(x, y3,label='Série 3')






plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Gráfico de linhas')
plt.legend()
plt.show()
