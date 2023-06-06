# 配置

eKuiper的配置是基于yaml文件，允许通过更新文件、环境变量和REST API进行配置。

## 配置范围

eKuiper的配置包括

1. `etc/kuiper.yaml`：全局配置文件。对其进行修改需要重新启动eKuiper实例。请参考[基本配置文件](./global_configurations.md)了解详情。
2. `etc/sources/${source_name}.yaml`：每个源的配置文件，用于定义默认属性（MQTT源除外，其配置文件为`etc/mqtt_source.yaml`）。详情请参考每个源的文档。例如，[MQTT 源](../guide/sources/builtin/mqtt.md)和[Neuron 源](../guide/sources/builtin/neuron.md)涵盖的配置项目。
3. `etc/connections/connection.yaml`：共享连接配置文件。

## 配置方法

用户可以通过3种方法设置配置，按优先级排序。

1. 管理控制台/REST API
2. 环境变量
3. etc文件夹中的Yaml文件

yaml 文件通常被用来设置默认配置。在裸机上部署时，用户可以很容易地访问文件系统，因此通常通过配置修改配置文件来更改配置。

当在docker或k8s中部署时，操作文件就不容易了，少量的配置可以通过环境变量来设置或覆盖。而在运行时，终端用户将使用管理控制台来动态地改变配置。eKuiper 管理控制台中的"配置"页面可以帮助用户直观地修改配置。

### 环境变量的语法

从环境变量到配置 yaml 文件之间有一个映射。当通过环境变量修改配置时，环境变量需要按照规定的格式来设置，例如。

```
KUIPER__BASIC__DEBUG => basic.debug in etc/kuiper.yaml
MQTT_SOURCE__DEMO_CONF__QOS => demo_conf.qos in etc/mqtt_source.yaml
EDGEX__DEFAULT__PORT => default.port in etc/sources/edgex.yaml
CONNECTION__EDGEX__REDISMSGBUS__PORT => edgex.redismsgbus.port int etc/connections/connection.yaml
```

环境变量用`__`分隔，分隔后的第一部分内容与配置文件的文件名匹配，其余内容与不同级别的配置项匹配。文件名可以是 `etc` 文件夹中的 `KUIPER` 和 `MQTT_SOURCE` ；或 `etc/connection` 文件夹中的`CONNECTION`。其余情况，映射文件应在 `etc/sources` 文件夹下。

## 配置文件

eKuiper 的配置文件位于 `$ eKuiper / etc / kuiper.yaml` 中。 配置文件为 yaml 格式。应用程序可以通过环境变量进行配置。环境变量优先于 yaml 文件中的对应项。为了对给定的配置使用 env 变量，我们必须使用如下格式： `KUIPER__`前缀 + 由`__`连接的路径元素。例如，在配置的情况下：

```yaml
basic:
  # true|false, with debug level, it prints more debug info
  debug: false
  # true|false, if it's set to true, then the log will be print to console
  consoleLog: false
  # true|false, if it's set to true, then the log will be print to log file
  fileLog: true
  # How many hours to split the file
  rotateTime: 24
  # Maximum file storage hours
  maxAge: 72
  # Whether to ignore case in SQL processing. Note that, the name of customized function by plugins are case-sensitive.
  ignoreCase: true
```

将basic项目下debug的值设置为true是有效的 `KUIPER__BASIC__DEBUG=true`。

配置ignoreCase用于在SQL处理中忽略大小写。默认情况下，它设置为 true 以符合标准 SQL。在这种情况下，摄取的数据可能不区分大小写。如果 SQL 中的列名、流定义和摄取的数据可以统一为区分大小写的名称，建议设置为 false 以获得更好的性能。

## 日志级别

```yaml
basic:
  # true|false, with debug level, it prints more debug info
  debug: false
  # true|false, if it's set to true, then the log will be print to console
  consoleLog: false
  # true|false, if it's set to true, then the log will be print to log file
  fileLog: true
  # How many hours to split the file
  rotateTime: 24
  # Maximum file storage hours
  maxAge: 168
  # Whether to ignore case in SQL processing. Note that, the name of customized function by plugins are case-sensitive.
  ignoreCase: false
```

配置项 **ignoreCase** 用于指定 SQL 处理中是否大小写无关。若为 true，则输入数据的列名大小写可以与 SQL 中的定义不同。如果 SQL 语句中，流定义以及输入数据中可以保证列名大小写完全一致，则建议设置该值为 false 以获得更优的性能。在 1.10 版本之前，其默认值为 true ， 以兼容标准 SQL ；在 1.10 及之后版本中，默认值改为 false ，以获得更优的性能 。

## 系统日志

用户将名为 KuiperSyslogKey 的环境变量的值设置为 true 时，日志将打印到系统日志中。

## Cli 地址

```yaml
basic:
  # CLI 绑定 IP
  ip: 0.0.0.0
  # CLI port
  port: 20498
```

## REST 服务配置

```yaml
basic:
  # REST service 绑定 IP
  restIp: 0.0.0.0
  # REST service port
  restPort: 9081
  restTls:
    certfile: /var/https-server.crt
    keyfile: /var/https-server.key
```

### restPort

REST http 服务器监听端口

### restTls

TLS 证书 cert 文件和 key 文件位置。如果 restTls 选项未配置，则 REST 服务器将启动为 http 服务器，否则启动为 https 服务器。

## authentication 

当 `authentication` 选项为 true 时，eKuiper 将为 rest api 请求检查 `Token` 。请检查此文件以获取 [更多信息](../api/restapi/authentication.md)。

```yaml
basic:
  authentication: false
```


## Prometheus 配置

如果 `prometheus` 参数设置为 true，eKuiper 将把运行指标暴露到 prometheus。Prometheus 将运行在 `prometheusPort` 参数指定的端口上。

```yaml
basic:
  prometheus: true
  prometheusPort: 20499
```

在如上默认配置中，eKuiper 暴露于 Prometheus 运行指标可通过 `http://localhost:20499/metrics` 访问。

Prometheus 端口可设置为与 eKuiper 的 REST 服务端口相同。这样设置的话，两个服务将运行在同一个 HTTP 服务中。

## Pluginhosts 配置

默认在 `packages.emqx.net` 托管所有预构建 [native 插件](../extension/native/overview.md)。

所有插件列表如下：

| 插件类型 | 预构建插件列表                                               |
| -------- | ------------------------------------------------------------ |
| source   | random zmq                                                   |
| sink     | file image influx redis tdengine zmq                         |
| function | accumulateWordCount countPlusOne echo geohash image labelImage |

用户可以通过以下 Rest-API 获取所有预构建插件的名称和地址：

```
GET http://localhost:9081/plugins/sources/prebuild
GET http://localhost:9081/plugins/sinks/prebuild
GET http://localhost:9081/plugins/functions/prebuild
```

获取插件信息后，用户可以尝试这些插件，[更多信息](../api/restapi/plugins.md)

**注意：只有官方发布的基于 debian 的 docker 镜像支持以上操作**

## 规则配置

配置规则选项的默认属性。所有的配置都可以在规则层面上被覆盖。查看[规则选项](../guide/rules/overview.md#选项)了解详情。

## Sink 配置

配置 sink 的默认属性，目前主要用于配置[缓存策略](../guide/sinks/overview.md#缓存)。在规则层有同样的配置选项，可以覆盖这些默认配置。

```yaml
  # 是否开启缓存
  enableCache: false
  
  # 内存缓存的最大存储条数
  memoryCacheThreshold: 1024

  # 磁盘缓存的最大存储条数
  maxDiskCache: 1024000

  # 读写磁盘的缓存页条数，作为磁盘读写的基本单位
  bufferPageSize: 256

  # 重发的间隔时间，单位为毫秒
  resendInterval: 0

  # 规则停止后是否清除缓存
  cleanCacheAtStop: false
```

## 存储配置

可通过配置修改创建的流和规则等状态的存储方式。默认情况下，程序状态存储在 sqlite 数据库中。把存储类型改成 redis，可使用 redis 作为存储方式。

### Sqlite

可配置如下属性：

* name - 数据库文件名。若为空，则设置为默认名字`sqliteKV.db`。

### Redis

可配置如下属性：

* host     - redis 服务器地址。
* port     - redis 服务器端口。
* password - redis 服务器密码。若 redis 未配置认证系统，则可不设置密码。
* timeout  - 连接超时时间。
* connectionSelector - 重用 etc/connections/connection.yaml 中定义的连接信息, 主要用在 edgex redis 配置了认证系统时
  * 只适用于 edgex redis 的连接信息 
  * 连接信息中的 server， port 和 password 会覆盖以上定义的 host， port 和 password
  * [具体信息可参考](../guide/sources/builtin/edgex.md#connectionselector)

### 外部状态

还有一个名为 `extStateType` 的配置项。 这个配置的用途是用户可以预先在数据库中存储一些信息，当流处理规则需要这些信息时，他们可以通过
SQL 中的 [get_keyed_state](../sqls/functions/other_functions.md#getkeyedstate) 函数轻松获取它们。
*注意*：`type` 和 `extStateType` 可以使用不同的存储配置。

### 配置示例

```yaml
    store:
      #Type of store that will be used for keeping state of the application
      type: sqlite
      extStateType: redis
      redis:
        host: localhost
        port: 6379
        password: kuiper
        #Timeout in ms
        timeout: 1000
      sqlite:
        #Sqlite file name, if left empty name of db will be sqliteKV.db
        name:
```

## Portable 插件配置

配置 portable 插件的运行时属性。

```yaml
  portable:
      # 配置 python 可执行文件的位置或命令。
      # 若系统中有多个 python 版本，可通过此配置指定具体的 python 地址。
      pythonBin: python
      # 控制插件初始化超时时间，单位为毫秒。eKuiper portable 插件运行时会等待插件初始化以完成握手，若超时则终止插件进程
      initTimeout: 5000
```

## 初始化规则集

支持基于文件的流和规则的启动时配置。用户可以将名为 `init.json` 的[规则集](../api/restapi/ruleset.md#规则集格式)文件放入 `data` 目录，以初始化规则集。该规则集只在eKuiper 第一次启动时被导入。