# Nop action

该 action 是一个空操作目标，所有发送到此的结果将被忽略。如果指定 `log` 属性为 `true`，那么结果将会保存到日志文件，日志文件缺省保存在  `$eKuiper_install/log/stream.log`。

如希望使用 Nop Sink 连接器，点击 **数据流处理** -> **规则** -> **新建规则**，在 **动作** 区域，点击**添加**，**Sink** 选择 **nop**。

| 属性名称 | 是否可选 | 说明                                                   |
|------|------|------------------------------------------------------|
| log  | true | true/false - 是否将结果打印到日志。缺省为 `false`，这种情况下将不会打印到日志文件。 |

