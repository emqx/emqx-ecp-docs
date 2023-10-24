# 配置管理

NeuronEX 支持通过`命令行`、`环境变量`、`配置文件`的方式，对 NeuronEX 的配置参数进行修改，可以提供更加灵活的启动和运行方式。
如果同时配置了`命令行`、`环境变量`、`配置文件`，三者的优先级关系为：环境变量 > 命令行 > 配置文件

## 命令行

```shell
-c, --config string   config file path (default "etc/neuronex.yaml")
-e, --disable_auth    select whether to enable authentication
-h, --help            help for run
-m, --manage          manage the lifecycle of eKuiper and Neuron (default true)
```
## 环境变量

NeuronEX 支持在启动过程中读取环境变量来配置启动参数，目前支持的环境变量如下:

| 配置名                          | 配置作用                                                                           |
| ------------------------------ | --------------------------------------------------------------------------------- |
| NEURONEX_DISABLE_AUTH          | 设置为 1，NeuronEX 关闭 Token 鉴权认证；设置为0，NeuronEX 开启 Token 鉴权认证                |
| NEURON_DAEMON                  | 设置为1，Neuron 守护进程运行；设置为0，Neuron 正常运行                                   |
| NEURON_CONFIG_DIR              | Neuron 配置文件目录                                                                  |
| NEURON_PLUGIN_DIR              | Neuron 插件文件目录                                                                  |
## 配置文件

NeuronEX 提供 yaml 格式文件配置 NeuronEX 相关个性化参数。默认配置内容如下:

```yaml
server:
  # Neuronex listening port
  port: 8085

# Compatible neuron version
neuron:
  version: 2.6.0
  reverseProxies:
    - location: /api/neuron
      proxyPath: http://127.0.0.1:7000/api/v2

# Compatible ekuiper version
ekuiper:
  version: 1.10.2
  reverseProxies:
    - location: /api/ekuiper
      proxyPath: http://127.0.0.1:9081

# Log configuration, including log storage mode, log level, maximum value, storage count and syslog-related settings, etc.
log:
  mode: file
  level: info
  file: log/neuronex.log
  maxSize: 50000
  maxAge: 3
  maxBackups: 3
  listenAddr: "localhost:10514"
  syslogForward:
    enable: false
    priority: "info"
    network: "udp4"
    remoteAddr: ""
    tag: "neuron_ex_all"

official:
  url: https://license-test.mqttce.com
```
