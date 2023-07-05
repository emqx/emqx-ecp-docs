## Alarm List

See below for a list of alarms in ECP. 

| Alarm                              | Level  | Rule                                                         | Alarm Content                                                |
| :--------------------------------- | :----: | :----------------------------------------------------------- | :----------------------------------------------------------- |
| Neuron Service Offline             | Severe | Fails three consecutive connection tests                     | Neuron service {name} is offline, this alert will be sent only once. |
| Neuron Service Abnormal            | Severe | core_dumped <> 0, monitored continuously once <!--连续监控1次，不太确定什么意思--> | Neuron service {name} is abnormal, please check the core dump log. |
| Neuron Service Restarted           | Normal | 1. Running time is shorter than the monitoring period; <!--监控拉取时间--> <br/>2. Triggered once detected | Neuron service {name} has restarted.                         |
| Northbound Neuron Service Abnormal | Severe | 1. The sum of the number of disconnected northbound nodes and running northbound nodes exceeds the total number of northbound nodes; <!--看不懂--><br/>2. Triggered once detected | Northbound disconnection count is abnormal.                  |
| Southbound Neuron Service Abnormal | Severe | 1. The sum of the number of disconnected southbound nodes and running southbound nodes exceeds the total number of southbound nodes; <!--看不懂--><<br/>2. Triggered once detected | Southbound disconnection count is abnormal.                  |
| eKuiper Service Offline            | Severe | Fails three consecutive connection tests                     | eKuiper service {name} is offline, this alert will be sent only once. |
| eKuiper Service Sink Exception     | Severe | A rule in the sink reported an alarm.                        | Rule {rule name} has encountered a Sink exception.           |
| eKuiper Service Source Exception   | Severe | A rule in the source reported an alarm.                      | Rule {rule name} has encountered a data source exception.    |
| eKuiper Service OP Exception       | Severe | An operation-related rule reported an alarm.                 | Rule {rule name} has encountered an operational exception.   |
| EMQX Version Error                 | Severe | 1. The version of the cluster is older than "4.4.6"; <br/>2. Unable to retrieve the version of the cluster | EMQX {name} has a version error, the system is unable to retrieve the EMQX version or the EMQX version is older than 4.4.6. |
| EMQX Task Execution Failure        | Severe | The most recent EMQX task execution has failed               | EMQX {name}'s task named {task name} has failed.             |