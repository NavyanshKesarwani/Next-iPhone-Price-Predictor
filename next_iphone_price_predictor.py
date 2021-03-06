import pandas
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
data = pandas.read_csv('data.csv')
plt.scatter(data['version'], data['price'])
model = LinearRegression()
model.fit(data[['version']], data[['price']])
print(model.predict([[30]]))

