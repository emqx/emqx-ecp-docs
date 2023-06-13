# 模块列表

## 南向插件模块

### 全球标准

| 协议名称                                                      | 连接    | 类型  | 是否可用      | 备注                           |
| ------------------------------------------------------------ | ------ | ---- | ------------ | -------------------------------- |
| <div style="width:220pt">Modbus TCP</div>              | 以太网  | 开源 | 是            |  |
| <div style="width:220pt">Modbus RTU</div>              | 串口    | 开源 | 是           |  |
| <div style="width:220pt">Modbus RTU over TCP</div>     | 以太网  | 开源 | 是            |  |
| <div style="width:220pt">OPC UA</div>                  | 以太网  | 商业 | 是            |  |
| <div style="width:220pt">CIP Ethernet/IP</div>         | 以太网  | 商业 | 是             | <div style="width:110pt">CIP –通用工业协议</div> |

### PLC 驱动

| 协议名称                                                      | 连接    | 类型  | 是否可用      | 备注                           |
| ------------------------------------------------------------ | ------ | ---- | ------------ | -------------------------------- |
| <div style="width:220pt">Siemens 3964R/RK512</div>                                          | 串口    | 商业 | 仅 V1.x 可用  | <div style="width:110pt">用于 S5 和 S7</div> |
| <div style="width:220pt">Siemens Industrial Ethernet ISO for S7-200/300/400/1200/1500</div> | 以太网  | 商业 | 是            | |
| <div style="width:220pt">Siemens Fetch Write for S7-300/400 and CP443 module</div>          | 以太网  | 商业 | 是  | |
| <div style="width:220pt">Allen-Bradley DF1 half-duplex</div>                       | 串口    | 商业 | 是  | <div style="width:110pt">用于 PLC2 和 PLC5</div>                |
| <div style="width:220pt">Allen-Bradley CIP EtherNet/IP</div>                                | 以太网  | 商业 | 是            | <div style="width:110pt">CIP – 通用工业协议</div> |
| <div style="width:220pt">Schneider PLC Modbus RTU</div>                                     | 串口    | 商业 | 是  | |
| <div style="width:220pt">Schneider PLC Modbus TCP</div>                                     | 以太网  | 商业 | 是  | |
| <div style="width:220pt">Schneider Telemecanique UNI-TE</div>                               | 串口    | 商业 | 仅 V1.x 可用  | |
| <div style="width:220pt">ABB SattControl Comli</div>                                        | 串口    | 商业 | 是  | |
| <div style="width:220pt">Omron Host Link</div>                                              | 串口    | 商业 | 仅 V1.x 可用  | <div style="width:110pt">用于单连接和多连接</div> |
| <div style="width:220pt">Omron FINS on Host Link</div>                                      | 串口    | 商业 | 仅 V1.x 可用  | |
| <div style="width:220pt">Omron FINS on TCP</div>                                            | 以太网  | 商业 | 是            | |
| <div style="width:220pt">Omron FINS on UDP</div>                                            | 以太网  | 商业 | 是            | |
| <div style="width:220pt">Mitsubishi MC Protocol for Q series and C24 module</div>           | 串口    | 商业 | 仅 V1.x 可用  | |
| <div style="width:220pt">Mitsubishi MC Protocol for Q series and E71 module</div>           | 以太网  | 商业 | 是            | <div style="width:110pt">3E frame</div> |
| <div style="width:220pt">Mitsubishi FX Series</div>                                         | 串口    | 商业 | 仅 V1.x 可用  | |
| <div style="width:220pt">Mitsubishi FX3U-ENET-ADP</div>                                     | 以太网  | 商业 | 是            | <div style="width:110pt">1E frame</div>   |
| <div style="width:220pt">Mitsubishi 232ADP/485BD: Serial/RS485</div>                        | 串口    | 商业 | 否           | |
| <div style="width:220pt">Panasonic FP series MEWTOCOL-COM</div>                             | 串口    | 商业 | 否            | |
| <div style="width:220pt">Panasonic FP series MEWTOCOL-COM</div>                             | 以太网  | 商业 | 是            | |
| <div style="width:220pt">Panasonic FP series MEWTOCOL-DAT</div>                             | 以太网  | 商业 | 否            | |
| <div style="width:220pt">Beckhoff ADS/AMS TCPIP</div>                                       | 以太网  | 商业 | 是            | |
| <div style="width:220pt">Keyence CIP Ethernet/IP</div>                                      | 以太网  | 商业 | 是            | <div style="width:110pt">CIP – 通用工业协议</div> |
| <div style="width:220pt">Keyence MC Protocol</div>                                          | 以太网  | 商业 | 是            | <div style="width:110pt">三菱 MC 协议</div> |
| <div style="width:220pt">Delta DVP communication protocol</div>                             | 串口    | 商业 | 否            | |
| <div style="width:220pt">Delta Modbus TCP</div>                                             | 以太网  | 商业 | 是            | |
| <div style="width:220pt">Delta CIP Ethernet/IP</div>                                        | 以太网  | 商业 | 是            | <div style="width:110pt">CIP – 通用工业协议</div> |
| <div style="width:220pt">Fatek FACON serial</div>                                           | 串口    | 商业 | 否            | |
| <div style="width:220pt">Fatek FACON ethernet</div>                                         | 以太网  | 商业 | 否            | |
| <div style="width:220pt">GE FANUC 90-30 SNPX</div>                                          | 串口    | 商业 | 否            | |
| <div style="width:220pt">GE FANUC 90-30 Ethernet SRTP</div>                                 | 以太网  | 商业 | 否            | |

### 电力

| 协议名称             | 连接    | 类型       | 是否可用   | 备注     |
| ------------------- | ------ | --------- | --------- | ---------- |
| <div style="width:220pt">DL/T645-1997</div>          | 串口    | 商业       | 是       | <div style="width:110pt">中国电力仪表标准</div>  |
| <div style="width:220pt">DL/T645-2007</div>          | 串口    | 商业       | 是       | <div style="width:110pt">中国电力仪表标准</div>  |
| <div style="width:220pt">IEC 60870-5-101</div>     | 串口     | 商业      | 否         | |
| <div style="width:220pt">IEC 60870-5-102</div>     | 串口     | 商业      | 否         | |
| <div style="width:220pt">IEC 60870-5-103</div>     | 串口     | 商业      | 否         | |
| <div style="width:220pt">IEC 60870-5-104</div>     | 以太网  | 商业       | 是        | |
| <div style="width:220pt">IEC 61850</div>           | 以太网  | 商业       | 是        | |
| <div style="width:220pt">DNP3</div>                | 以太网  | 商业       | 否        | |

### 楼宇自动化

| 协议名称        | 连接      | 类型       | 是否可用  | 备注 |
| -------------- | ------- | ---------- | -------- | ------ |
| <div style="width:220pt">BACnet IP</div>      | 以太网  | 商业        | 是        | |
| <div style="width:220pt">KNXnet IP</div>      | 以太网  | 商业        | 是        | |
| <div style="width:220pt">BACnet MS/TP</div>    | 串口   | 商业       | 否         | <div style="width:110pt"> </div> |
| <div style="width:220pt">LON</div>            | 以太网  | 商业        | 否        | |

### 数控机床和机器人

| 协议名称       | 连接     | 类型   | 是否可用   | 备注     |
| ------------- | ------- | ----- | --------- | ------- |
| <div style="width:220pt">MTConnect</div>      | 以太网    | 商业    | 否         | <div style="width:110pt"> </div> |
| <div style="width:220pt">Fanuc 0i, 30i, 31i, 32i and 35i</div>      | 以太网    | 商业    | 是         | <div style="width:110pt"> </div> |
| <div style="width:220pt">Mitsubishi M800/M80</div>      | 以太网    | 商业    | 否         | <div style="width:110pt"> </div> |
| <div style="width:220pt">Siemens 840D、810、828D</div>      | 以太网    | 商业    | 否         | <div style="width:110pt"> </div> |

## 北向插件模块

### 云连接

| 协议名称                                 | 类型                                 | 是否可用                                | 备注                  |
| --------------------------------------- | ----------------------------------- | -------------------------------------- | -------------------- |
| <div style="width:285pt">RESTful API</div>            | 开源   | 是       |  |
| <div style="width:285pt">MQTT</div>                   | 开源   | 是       | <div style="width:110pt"> </div> |
| <div style="width:285pt">MQTT Sparkplug B</div>     | 商业   | 是       |  |
| <div style="width:285pt">Websocket</div>              | 商业   | 是       |  |

### 应用程序

| 协议名称                                                            | 类型                                  | 是否可用                                 | 备注 |
| ----------------------------------------------------------------- | ------------------------------------- | --------------------------------------- | ------ |
| <div style="width:285pt">eKuiper Stream Processing</div>   | 开源    | 是         | <div style="width:110pt"> </div>  |

