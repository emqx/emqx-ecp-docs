# Sparkplug B 插件

Sparkplug B 是一种建立在 MQTT 3.1.1 基础上的工业物联网数据传输规范。Sparkplug B 在保证灵活性和效率的前提下，使 MQTT 网络具备状态感知和互操作性，为设备制造商和软件提供商提供了统一的数据共享方式。

ECP Edge 从设备采集到的数据可以通过 Sparkplug B 协议从边缘端传输到 Sparkplug B 应用中，用户也可以从应用程序向 ECP Edge 发送数据修改指令。Sparkplug B 是运行在 MQTT 之上的应用型协议，所以在 ECP Edge 中的设置与 MQTT 驱动相似。

## 参数

|  参数         | 说明                                                         |
| ------------- | ------------------------------------------------------------ |
| **客户端 ID** | MQTT 客户端 ID，连接的唯一标识                                 |
| **组 ID**  | Sparkplug B 协议中的最顶层逻辑分组，可以代表工厂或车间等实体     |
| **节点 ID**   | Sparkplug B 协议中的边缘节点唯一标识                           |
| **SSL**       | 是否启用 mqtt ssl，默认 false                                 |
| **服务器地址**      | MQTT Broker 主机                                             |
| **服务器端口**      | MQTT Broker 端口号                                           |
| **用户名**  | 连接到 Broker 时使用的用户名                                  |
| **密码**  | 连接到 Broker 时使用的密码                                    |
| **CA 证书**        | ca 文件，只在 ssl 值为 true 时启用                            |
| **客户端证书**      | cert 文件，只在 ssl 值为 true 时启用                          |
| **客户端私钥**       | key 文件，只在 ssl 值为 true 时启用                           |
| **私钥密码**   | key 文件密码，只有在 ssl 值为 true 时启用                     |

:::tip
以上参数中只有 `组 ID` 和 `节点 ID` 来源于 Sparkplug B 规范，其余均为 MQTT Broker 的连接参数，可以参阅 [MQTT 概览](../mqtt/mqtt.md)。
:::
