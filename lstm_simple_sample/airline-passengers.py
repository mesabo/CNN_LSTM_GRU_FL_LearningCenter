
import matplotlib.pyplot as plt
import pandas as pd
 
 
file_path = "./data/airline-passengers.csv"

df = pd.read_csv(file_path)

timeseries = df[["Passengers"]].values.astype('float32')

def previewPassers(data):
    plt.plot(data)
    plt.show()
    

if __name__ == "__main__":
    previewPassers(timeseries)
