# Alarm List

## ECP Alarm Rules

| Alarm Type                                                   | Default Severity Level | Alarm Message                                                |
| ------------------------------------------------------------ | :--------------------: | :----------------------------------------------------------- |
| Email send failed alarm                                      |         Normal         | Email sending failed,  please check mail server configuration | 
| Webhook send failed alarm                                    |         Normal         | Webhook sending failed, Webhook address: <code v-pre>{{address}}</code> |

## Edge Alarm Rules

| Alarm Type                                                   | Default Severity Level | Alarm Message                                                | Identical Alarm  Criteria                          |
| ------------------------------------------------------------ | :--------------------: | :----------------------------------------------------------- | :------------------------------------------------- |
| Email send failed alarm                                      |         Normal         | Email sending failed,  please check mail server configuration |                                                    |
| Webhook send failed alarm                                    |         Normal         | Webhook sending failed, Webhook address: <code v-pre>{{address}}</code> |                                                    |
| NeuronEX data collection driver exception alarm (including south and north) |        Critical        | NeuronEX <code v-pre>{{instance name}}</code> Driver <code v-pre>{{driver name}}</code> exception | From the same driver on the same NeuronEX instance |
| NeuronEX data processing rule exception alarm                |        Critical        | NeuronEX <code v-pre>{{instance name}}</code> Rule <code v-pre>{{rule name}}</code> exception | From the same rule on the same NeuronEX instance   |
| NeuronEX offline alarm                                       |        Critical        | NeuronEX <code v-pre>{{instance name}}</code> Offline        | From the same NeuronEX instance                    |
| NeuronEX restart alarm                                       |        Critical        | NeuronEX <code v-pre>{{instance name}}</code> Restarted      | From the same NeuronEX instance                    |


## Cluster Alarm Rules

| Alarm Type                                                   | Default Severity Level | Alarm Message                                                | Identical Alarm  Criteria                          |
| ------------------------------------------------------------ | :--------------------: | :----------------------------------------------------------- | :------------------------------------------------- |
| EMQX CPU Usage Alarm | Critical/Normal |EMQX <code v-pre>{{cluster name}}</code> (Node <code v-pre>{{node name}}</code>) CPU usage exceeds <code v-pre>{{threshold value}}</code>| From the same EMQX cluster |
| EMQX Memory Usage Alarm | Critical/Normal |EMQX <code v-pre>{{cluster name}}</code> (Node <code v-pre>{{node name}}</code>) memory usage exceeds <code v-pre>{{threshold value}}</code> | From the same EMQX cluster |
| EMQX CPU Load Alarm | Critical/Normal |EMQX <code v-pre>{{cluster name}}</code> (Node <code v-pre>{{node name}}</code>) CPU load exceeds <code v-pre>{{threshold value}}</code> | From the same EMQX cluster |
| EMQX Cluster Status Exception | Critical |EMQX <code v-pre>{{cluster name}}</code> is in abnormal cluster status | From the same EMQX cluster |
| EMQX License Expiration Alarm | Critical/Normal |EMQX <code v-pre>{{cluster name}}</code> license is about to expire in <code v-pre>{{threshold value}}</code> days | From the same EMQX cluster |
| EMQX License Usage Alarm | Critical/Normal |EMQX <code v-pre>{{cluster name}}</code> license usage exceeds <code v-pre>{{threshold value}}</code> | From the same EMQX cluster |
| EMQX Cluster Node Exception | Critical |EMQX <code v-pre>{{cluster name}}</code> has nodes in abnormal status | From the same EMQX cluster |
| EMQX Rule Exception | Critical |EMQX <code v-pre>{{cluster name}}</code> rule bridge <code v-pre>{{rule type}}</code>:<code v-pre>{{rule name}}</code> is in abnormal status | From the same EMQX cluster |
| EMQX Authentication Resource Exception | Critical |EMQX <code v-pre>{{cluster name}}</code> authentication resource <code v-pre>{{resource name}}</code> is in abnormal status | From the same EMQX cluster |
| EMQX ACL Authorization Resource Exception | Critical |EMQX <code v-pre>{{cluster name}}</code> authorization resource <code v-pre>{{resource name}}</code> is in abnormal status | From the same EMQX cluster |
| EMQX Rule Execution Rate Alarm | Normal |EMQX <code v-pre>{{cluster name}}</code> rule <code v-pre>{{rule name}}</code> execution rate change exceeds <code v-pre>{{threshold value}}</code> | From the same EMQX cluster |
| EMQX Rule Execution Failure Alarm | Normal |EMQX <code v-pre>{{cluster name}}</code> rule <code v-pre>{{rule name}}</code> execution failure increasement exceeds <code v-pre>{{threshold value}}</code> | From the same EMQX cluster |
| EMQX Rule Action Failure Alarm | Normal |EMQX <code v-pre>{{cluster name}}</code> rule <code v-pre>{{rule name}}</code> action failure increasement exceeds <code v-pre>{{threshold value}}</code> | From the same EMQX cluster |
| EMQX Connection Auth Exception | Normal |EMQX <code v-pre>{{cluster name}}</code> connection auth failure increasement exceeds <code v-pre>{{threshold value}}</code> | From the same EMQX cluster |
| EMQX Publish Auth Exception | Normal |EMQX <code v-pre>{{cluster name}}</code> Publish Auth Exception <code v-pre>{{threshold value}}</code> | From the same EMQX cluster |
| EMQX Subscription Auth Exception | Normal |EMQX <code v-pre>{{cluster name}}</code> subscription auth failure increasement exceeds <code v-pre>{{threshold value}}</code> | From the same EMQX cluster |