# 告警规则列表

| 告警类型 | 默认告警级别 |告警内容      | 同一条告警的判定 |
| :----------------------------- | :----: | :----------------------------------------------------------- |:-----------------------------------------------------------  |
|    NeuronEX 数采驱动节点异常告警（包括南向、北向）    | 严重 |NeuronEX <code v-pre>{{实例名称}}</code> 驱动<code v-pre>{{驱动名称}}</code>异常。                                              | 同一个 NeuronEX 同一个驱动节点产生的告警 |
| NeuronEX 流处理引擎规则异常告警 | 严重 |NeuronEX <code v-pre>{{实例名称}}</code> 规则<code v-pre>{{规则名称}}</code>异常。 | 同一个 NeuronEX 同一条规则产生的告警 |
| NeuronEX 离线告警 | 严重 |NeuronEX <code v-pre>{{实例名称}}</code> 离线 | 同一个 NeuronEX |
| NeuronEX 重启告警 | 严重 |NeuronEX <code v-pre>{{实例名称}}</code> 重启 | 同一个 NeuronEX |
| 邮件发送失败告警 | 一般 |邮件发送失败， 请检查邮件服务器配置。 |  |
| Webhook 发送失败告警 | 一般 |Webhook 发送失败，Webhook 地址： <code v-pre>{{Webhook地址}}</code> |  |
| EMQX 规则异常 | 严重 |EMQX <code v-pre>{{实例名称}}</code> 规则 <code v-pre>{{规则名称}}</code> 异常 | 同一个 EMQX 集群 |
| EMQX 连接器异常 | 严重 |EMQX <code v-pre>{{实例名称}}</code> 连接器 <code v-pre>{{连接器名称}}</code> 异常 | 同一个 EMQX 集群 |