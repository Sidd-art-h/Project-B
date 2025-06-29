The circuit model in Simulink is present in the custom_circuit.xls
It is a basic battery circuit with regular components you can modify it as per your desire
It records outputs like Voltage, Current, SOH along with time
The primary issue is the temperature regarding calculation of SOC of batteries so you can adjust the Temperature values in the model
The recorded outputs are stored in a structure out and
## for charging circuit, i have set the step output as 20A and for discharging i have set to -20 A
The aim is to note the values and plot a charging discharging curve
To plot charging discharging curve for any circuit at any temperature tweak the .slx file accordingly and run the csv_generator.m file
The code in the .m file is this :

 					voltage = out.Voltage.signals.values;
					current = out.Current.signals.values;
					soc     = out.SOC.signals.values;
					time    = out.tout;
					T = table(time, voltage, current, soc);
					writetable(T, 'battery_simulation_charging_output.csv');

After running for charging output , for the discharging.csv, run the simulation with step output -20A and change the last line of the .m file
 					writetable(T, 'battery_simulation_charging_output.csv');
                                                          to
                                        writetable(T, 'battery_simulation_discharging_output.csv');
and so both csv for the charging and discharging will get saved.
You can plot on Matlab itself without using the .csv files but i thought python is more flexible regarding plotting graphs so i exported the .csv files for better representation on python
 The battery of 100Ah gives a curve that is based off an ideal condition where :
      Zero internal resistance.
      Zero chemical hysteresis.
      Instant energy transfer. (Not possible)
Hence the circuit model can be improvised to meet real world requirements and then plot.py can be run to show the charging discharging curves....
 

