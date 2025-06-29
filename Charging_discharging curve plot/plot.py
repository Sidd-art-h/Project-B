import matplotlib.pyplot as plt
import pandas as pd
#Load the csv files to the code
charge = pd.read_csv(r'Charging_discharging curve plot\battery_simulation_charging_output.csv')
discharge = pd.read_csv(r'Charging_discharging curve plot\battery_simulation_discharging_output.csv')

#Now let's start plotting....
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12))

# Voltage vs Time
ax1.plot(charge['time'], charge['voltage'], 'g-', label='Charging')
ax1.plot(discharge['time'], discharge['voltage'], 'r-', label='Discharging')
ax1.set_ylabel('Voltage (V)')
ax1.legend()
ax1.grid(True)

# Current vs Time
ax2.plot(charge['time'], charge['current'], 'g-', label='Charging (+20A)')
ax2.plot(discharge['time'], discharge['current'], 'r-', label='Discharging (-20A)')
ax2.set_ylabel('Current (A)')
ax2.legend()
ax2.grid(True)

# SOC vs Time
ax3.plot(charge['time'], charge['soc'], 'g-', label='Charging')
ax3.plot(discharge['time'], discharge['soc'], 'r-', label='Discharging')
ax3.set_xlabel('Time (s)')
ax3.set_ylabel('State of Charge (%)')
ax3.legend()
ax3.grid(True)

plt.tight_layout()
plt.savefig('battery_curves.png', dpi=300)
plt.show()
