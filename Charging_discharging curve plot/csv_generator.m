
voltage = out.Voltage.signals.values;
current = out.Current.signals.values;
soc     = out.SOC.signals.values;
time    = out.tout;
T = table(time, voltage, current, soc);
writetable(T, 'battery_simulation_charging_output.csv');
