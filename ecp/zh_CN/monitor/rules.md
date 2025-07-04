# 告警规则列表

## ECP 通用告警规则
| 告警类型 | 默认告警级别 |告警内容      | 
| :----------------------------- | :----: | :----------------------------------------------------------- |
|    邮件发送失败告警    | 一般 |邮件发送失败， 请检查邮件服务器配置。                                              |
| Webhook 发送失败告警 | 一般 |Webhook 发送失败，Webhook 地址： <code v-pre>{{Webhook地址}}</code> |

## 边缘服务告警规则
| 告警类型 | 默认告警级别 |告警内容      | 同一条告警的判定 |
| :----------------------------- | :----: | :----------------------------------------------------------- |:-----------------------------------------------------------  |
| NeuronEX 数采驱动节点异常告警（包括南向、北向） | 严重 |NeuronEX <code v-pre>{{实例名称}}</code> 驱动<code v-pre>{{驱动名称}}</code>异常。 | 同一个 NeuronEX 同一个驱动节点产生的告警 |
| NeuronEX 流处理引擎规则异常告警 | 严重 |NeuronEX <code v-pre>{{实例名称}}</code> 规则<code v-pre>{{规则名称}}</code>异常。 | 同一个 NeuronEX 同一条规则产生的告警 |
| NeuronEX 离线告警 | 严重 |NeuronEX <code v-pre>{{实例名称}}</code> 离线 | 同一个 NeuronEX |
| NeuronEX 重启告警 | 严重 |NeuronEX <code v-pre>{{实例名称}}</code> 重启 | 同一个 NeuronEX |
| EMQX 规则异常 | 严重 |EMQX <code v-pre>{{实例名称}}</code> 规则 <code v-pre>{{规则名称}}</code> 异常 | 同一个 EMQX 集群 |
| EMQX 连接器异常 | 严重 |EMQX <code v-pre>{{实例名称}}</code> 连接器 <code v-pre>{{连接器名称}}</code> 异常 | 同一个 EMQX 集群 |

## 云端集群告警规则
| 告警类型 | 默认告警级别 |告警内容      | 同一条告警的判定 |
| :----------------------------- | :----: | :----------------------------------------------------------- |:-----------------------------------------------------------  |
| EMQX CPU 使用率告警 | 严重/一般 |EMQX <code v-pre>{{集群名称}}</code>（节点 <code v-pre>{{节点名称}}</code>）CPU 使用率超过 <code v-pre>{{阈值数值}}</code>| 同一个 EMQX 集群 |
| EMQX 内存使用率告警 | 严重/一般 |EMQX <code v-pre>{{集群名称}}</code>（节点 <code v-pre>{{节点名称}}</code>）内存使用率超过 <code v-pre>{{阈值数值}}</code> | 同一个 EMQX 集群 |
| EMQX CPU 负载告警 | 严重/一般 |EMQX <code v-pre>{{集群名称}}</code>（节点 <code v-pre>{{节点名称}}</code>）CPU 负载超过 <code v-pre>{{阈值数值}}</code> | 同一个 EMQX 集群 |
| EMQX 集群状态异常 | 严重 |EMQX <code v-pre>{{集群名称}}</code> 集群状态异常 | 同一个 EMQX 集群 |
| EMQX 许可证即将过期 | 严重/一般 |EMQX <code v-pre>{{集群名称}}</code> 许可证即将在 <code v-pre>{{阈值数值}}</code> 天内过期 | 同一个 EMQX 集群 |
| EMQX 许可证使用量告警 | 严重/一般 |EMQX <code v-pre>{{集群名称}}</code> 许可证使用量超过 <code v-pre>{{阈值数值}}</code> | 同一个 EMQX 集群 |
| EMQX 集群节点异常 | 严重 |EMQX <code v-pre>{{集群名称}}</code> 部分节点异常 | 同一个 EMQX 集群 |
| EMQX 规则异常 | 严重 |EMQX <code v-pre>{{集群名称}}</code> 规则桥接 <code v-pre>{{规则类型}}</code>:<code v-pre>{{规则名称}}</code> 异常 | 同一个 EMQX 集群 |
| EMQX 连接认证数据源异常 | 严重 |EMQX <code v-pre>{{集群名称}}</code> 连接认证数据源 <code v-pre>{{数据源名称}}</code> 异常 | 同一个 EMQX 集群 |
| EMQX ACL 授权数据源异常 | 严重 |EMQX <code v-pre>{{集群名称}}</code> ACL 授权数据源 <code v-pre>{{数据源名称}}</code> 异常 | 同一个 EMQX 集群 |
| EMQX 规则执行速率变化告警 | 一般 |EMQX <code v-pre>{{集群名称}}</code> 规则 <code v-pre>{{规则名称}}</code> 执行速率变化超过 <code v-pre>{{阈值数值}}</code> | 同一个 EMQX 集群 |
| EMQX 规则执行失败突增告警 | 一般 |EMQX <code v-pre>{{集群名称}}</code> 规则 <code v-pre>{{规则名称}}</code> 执行失败突增超过 <code v-pre>{{阈值数值}}</code> | 同一个 EMQX 集群 |
| EMQX 规则动作失败突增告警 | 一般 |EMQX <code v-pre>{{集群名称}}</code> 规则 <code v-pre>{{规则名称}}</code> 动作失败突增超过 <code v-pre>{{阈值数值}}</code> | 同一个 EMQX 集群 |
| EMQX 连接认证失败突增告警 | 一般 |EMQX <code v-pre>{{集群名称}}</code> 连接认证失败突增超过 <code v-pre>{{阈值数值}}</code> | 同一个 EMQX 集群 |
| EMQX 消息发布认证失败突增告警 | 一般 |EMQX <code v-pre>{{集群名称}}</code> 消息发布认证失败突增超过 <code v-pre>{{阈值数值}}</code> | 同一个 EMQX 集群 |
| EMQX 消息订阅认证失败突增告警 | 一般 |EMQX <code v-pre>{{集群名称}}</code> 消息订阅认证失败突增超过 <code v-pre>{{阈值数值}}</code> | 同一个 EMQX 集群 |