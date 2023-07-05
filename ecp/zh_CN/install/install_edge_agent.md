# 安装 ECP 边缘代理

针对边缘侧有自己的 VPC 或局域网，与云端的 ECP 、EMQX 集群不在一个网络内的情况， ECP 提供了边缘代理（ECP Edge Agent）组件，用于实现边缘侧对云端服务的通信。


## 安装条件

部署 ECP 边缘代理前，请确认您的环境满足以下要求：

| OS     | 版本要求        |
| :----- | :-------------- |
| Ubuntu | 20.04  或 22.04 |
| CentOS | 7.0 或以上      |

## 获取安装包

欢迎访问 EMQ 官网获取 ECP 和 EMQX Edge Operator 的安装包。

1. 进入[联系我们](https://www.emqx.com/zh/contact?product=emqx-ecp)页面。
2. 输入必要的联系信息，如姓名、公司、工作邮箱，国家和地区，以及您的联系方式。
3. 您可在下方的文本框中填写您的应用场景及需求，以便我们为您提供最适宜的资源。
4. 填写好以上信息后，点击**立即提交**，我们的销售将会尽快与您联系。

## 安装 ECP 边缘代理

1. ECP 安装包的命名规则一般为 `emqx-ecp-edge-agent.tar.gz`，运行以下命令提取 ECP Edge Agent 安装包中的内容到本地目录，提取后的内容将位于 `./emqx-ecp-edge-agent` 目录。

   ```bash
   tar -zxvf emqx-ecp-edge-agent.tar.gz # 解压缩
   sudo mv ./emqx-ecp-edge-agent/emqx-bc-tunnel-agent /usr/local/bin/ # 把可执行文件移入 /usr/local/bin 下。注：不同的系统目录可能有所不同。
   ```

2. 修改配置文件 `./emqx-ecp-edge-agent/configs/conf.yaml`。按照实际需求，配置服务器、日志、MQTT 相关，以及健康检查等相关内容。注意：请勿修改配置文件 `conf.yaml` 的文件名。

   ```bash
   server:
     # agent名称
     name: testAgent
     # agent描述
     desc: test
   
   logger:
     # 日志输出格式，可选：json 或 txt
     format: json
     # 是否要将日志输出至控制台
     consoleLog: false
     # 是否要将日志输出至文件
     fileLog: true
     # 日志存储位置
     logPath: /tmp/EMQX-BC-Tunnel-Agent.log
     # 日志级别
     level: DEBUG
     # 单日志文件大小，单位M
     rotationSize: 10
     # 历史日志最长保存天数
     maxAge: 7
     # MaxBackups is the maximum number of old log files to retain
     # 历史日志最多保存个数
     maxBackups: 3
   
   mqtt:
     # 是否启用ssl
     useSSL: false
     # 最大重连间隔，单位秒
     maxReconnectInterval: 3
     # 连接超时时间，单位秒
     connectTimeout: 5
     # 是否清理 session
     cleanSession: true
     # 是否校验证书
     verifyCertificate: false
   
   interval:
     # agent定时健康上报间隔，单位秒
     report: 30
     # 边缘服务定时健康检查间隔，单位秒
     health: 10
   ```

3. 通过以下命令安装 ECP，您需在命令中指定以下参数：

   - --orgID： 指定组织 ID，可联系 ECP **系统管理员**获取。

   - --projectID：指定项目 ID，可联系 ECP **系统管理员**获取。

   - --mqttAddr：指定 MQTT 地址和端口。

   - --mqttUsername：指定 MQTT 用户名。

   - --mqttPassword：指定 MQTT 密码。

   - --config：指定配置文件，解压后的默认路径为： `./emqx-ecp-edge-agent/configs/conf.yaml`。

   ```bash
   sudo emqx-bc-tunnel-agent install --orgID {orgID} --projectID {projectID} --mqttAddr {mqttAddr} --mqttUsername {mqttUsername} --mqttPassword {mqttPassword} --config ./emqx-ecp-edge-agent/configs/
   ```

   

### 启动 ECP 边缘代理

通过以下命令启动 ECP 边缘代理。

```bash
sudo emqx-bc-tunnel-agent start
```

启动后，ECP 边缘代理会自动注册到 ECP 云边一体化平台。您可根据启动命令中指定的组织名和项目找到对应 ECP 边缘代理。关于 ECP 边缘代理的具体使用步骤，见[ECP 边缘代理](../edge_service/batch_import.md)。

