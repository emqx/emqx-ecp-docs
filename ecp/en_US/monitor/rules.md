# Alarm List

See below for a list of alarms in ECP. 

| Alarm Type                                                   | Default Severity Level | Alarm Message                                                | Identical Alarm  Criteria                          |
| ------------------------------------------------------------ | :--------------------: | :----------------------------------------------------------- | :------------------------------------------------- |
| Email send failed alarm                                      |         Normal         | Email sending failed,  please check mail server configuration. |                                                    |
| Webhook send failed alarm                                    |         Normal         | Webhook sending failed, Webhook address: <code v-pre>{{address}}</code> |                                                    |
| NeuronEX data collection driver exception alarm (including south and north) |        Critical        | NeuronEX <code v-pre>{{instance name}}</code> Driver <code v-pre>{{driver name}}</code> exception | From the same driver on the same NeuronEX instance |
| NeuronEX data processing rule exception alarm                |        Critical        | NeuronEX <code v-pre>{{instance name}}</code> Rule <code v-pre>{{rule name}}</code> exception. | From the same rule on the same NeuronEX instance   |
| NeuronEX offline alarm                                       |        Critical        | NeuronEX <code v-pre>{{instance name}}</code> Offline        | From the same NeuronEX instance                    |
| NeuronEX restart alarm                                       |        Critical        | NeuronEX <code v-pre>{{instance name}}</code> Restarted      | From the same NeuronEX instance                    |
| EMQX rule alarm                                              |        Critical        | EMQX <code v-pre>{{instance name}}</code> Rule <code v-pre>{{rule name}}</code> alarm. | From the same EMQX cluster                         |
| EMQX connector alarm                                         |        Critical        | EMQX <code v-pre>{{instance name}}</code> Connector <code v-pre>{{connector name}}</code> | From the same EMQX cluster                         |