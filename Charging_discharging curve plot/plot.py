!pip install matplotlib
import matplotlib.pyplot as plt
import pandas as pd
charging_data = pd.read_csv('battery_simulation_charging_output.csv')
discharging_data = pd.read_csv('batter