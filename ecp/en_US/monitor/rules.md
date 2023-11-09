## Alarm List

See below for a list of alarms in ECP. 

| Alarm                                                        | Level  | Rule                                                         | Alarm Content                                                |
| :----------------------------------------------------------- | :----: | :----------------------------------------------------------- | :----------------------------------------------------------- |
| NeuronEX Service Offline                                     | Severe | Fails three consecutive connection tests                     | NeuronEX service {name} is offline, this alert will be sent only once. |
| NeuronEX Data Acquisition Function Exception Alarms          | Severe | core_dumped <> 0, monitored continuously once.               | NeuronEX service {name} is abnormal, please check the core dump log. |
| NeuronEX Service Restarted                                   | Normal | 1. Running time is shorter than the monitoring period; <br/>2. Triggered once detected | NeuronEX service {name} has restarted.                       |
| NeuronEX Northbound Data Acquisition Function Abnormality    | Severe | 1. The sum of the number of disconnected northbound nodes and running northbound nodes exceeds the total number of northbound nodes<br/>2. Triggered once detected | Northbound disconnection count is abnormal.                  |
| NeuronEX Southbound Data Acquisition Function Abnormality    | Severe | 1. The sum of the number of disconnected southbound nodes and running southbound nodes exceeds the total number of southbound nodes;<<br/>2. Triggered once detected | Southbound disconnection count is abnormal.                  |
| NeuronEX Data Processing Function Sink Abnormal              | Severe | A rule in the sink reported an alarm.                        | Rule {rule name} has encountered a Sink exception.           |
| NeuronEX data processing function Source exception occurs.   | Severe | A rule in the source reported an alarm.                      | Rule {rule name} has encountered a data source exception.    |
| NeuronEX data processing function occurs with an OP exception. | Severe | An operation-related rule reported an alarm.                 | Rule {rule name} has encountered an operational exception.   |



