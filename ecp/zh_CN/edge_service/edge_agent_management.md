# 代理方式管理边缘服务

如果 NeuronEX 所在边缘节点 IP 不固定，或者 NeuronEX 处于自己的 VPC 或局域网中，ECP 无法主动获取到 NeuronEX 所在边缘节点的 IP 信息，直连模式导入边缘服务将不再适用。ECP 提供了代理纳管方式，对上述场景中的 NeuronEX 进行管理接入。

## 配置代理服务 

代理模式下，ECP 与 NeuronEX 之间使用 MQTT 协议进行通信，在 ECP 端和 NeuronEX 端都需要先配置 MQTT 并开启代理服务。NeuronEX 端的代理功能配置请参考[NeuronEX 代理功能配置](https://docs.emqx.com/zh/neuronex/latest/admin/sys-configuration.html#%E4%BB%A3%E7%90%86%E5%8A%9F%E8%83%BD%E9%85%8D%E7%BD%AE)。ECP 端安装时已自带 MQTT 服务器 NanoMQ，可以使用该服务器，也可以自行安装。如果使用自行安装的 MQTT 服务器，需要按以下方式手动配置 MQTT 相关配置项。

### 基于 Docker 部署的 ECP

进入安装文件所在目录后，修改 configs/main/main.yaml 配置文件中的 mqtt 相关配置项，并重启 ECP。

```
mqtt:
  # 是否启用ssl
  useSSL: false
  # mqtt broker，格式为<mqtt服务地址>:<mqtt服务端口>
  addr: mqtt:1883
  # 连接mqtt服务验证用的用户名，如果未开启验证，可以不设置
  username: "ecp-mqtt-cloud"
  # 连接mqtt服务验证用的密码，如果未开启验证，可以不设置
  password: "ecp-mqtt-cloud1!"
  # 最大重连间隔，单位秒
  maxReconnectInterval: 3
  # 连接超时时间，单位秒
  connectTimeout: 8
  # 是否清理 session
  cleanSession: true
  # 是否校验证书，适用于ssl启用场景
  verifyCertificate: false
  # CA证书文件位置，适用于ssl启用场景，如果使用的是可信机构签发的证书，可以不设置
  cacertFile: ""
  # ECP端证书文件位置，适用于ssl启用场景
  certFile: ""
  # ECP端证书密钥文件位置，适用于ssl启用场景
  keyFile: ""
```

### 基于 Kubernetes 部署的 ECP

修改 configmap 中 mqtt 相关配置项。配置项具体内容与上文基于 Docker 方式部署的相同。

```
kubectl -n emqx-ecp edit configmap kube-ecp-stack-main-conf
```

### 代理服务中开启 SSL/TLS

ECP 默认代理服务器通过 TCP 协议进行数据传输，如果您希望使用更安全的传输方式，可以进行适当的配置，开启 SSL/TLS。以下将以 Docker 部署的 ECP 使用自带的 NanoMQ 为例来详细说明配置步骤。您也可以参考[NanoMQ Docker 部署文档](https://nanomq.io/docs/zh/latest/installation/docker.html)获取更完整的介绍。

1. 准备好NanoMQ 使用的 SSL 证书文件，包括 CA 文件（cacert.pem）、NanoMQ 使用的证书文件（cert.pem）、NanoMQ 使用的证书密钥文件（key.pem），并保存到安装文件所在目录的 configs/nanomq 子目录下。

2. 准备好 ECP 使用的 SSL 证书文件，包括 CA 文件（cacert.pem）、ECP 使用的证书文件（client-cert.pem）、NanoMQ 使用的证书密钥文件（client-key.pem），并保存到安装文件所在目录的 configs/main 子目录下。

3. 进入安装文件所在目录，修改 configs/nanomq/nanomq.conf，增加 SSL 监听器，主要配置端口和证书位置：

   - `bind` 中使用 8883 端口。
   - `keyfile`,  `certfile`,  `cacertfile` 分别为 NanoMQ SSL 证书文件所挂载到的容器中的路径。

   ```
   listeners.ssl {
       bind = "0.0.0.0:8883"
       keyfile = "/etc/certs/server.key"
       certfile = "/etc/certs/server.pem"
       cacertfile = "/etc/certs/cacert.pem"
   }
   ```

4. 进入安装文件所在目录，修改 docker-compose.yaml 文件中的 mqtt 部分，需要改动的具体内容如下：

   - `image` 中确认使用完整版 NanoMQ 的镜像，如0.21.2-full。
   - `ports` 中新增 SSL 端口 8883 的映射。示例中映射到 38883 端口（38883 端口供 NeuronEX 等外部访问使用，ECP 仍使用容器内网络端口 8883）
   - `volumes` 中挂载证书文件到 NanoMQ 容器，请确保与上一步 nanomq.conf 中指定的容器内路径保持一致。
   - `environment` 中配置 SSL/TLS 相关环境变量
     - NANOMQ_TLS_ENABLE 设为 true，表示开启 TLS。
     - NANOMQ_TLS_VERIFY_PEER 设为 false 表示 NanoMQ 不验证客户端证书，设为 true 表示需要验证客户端证书，请根据实际需要设置。
     - NANOMQ_TLS_FAIL_IF_NO_PEER_CERT 设为 false 表示 NanoMQ 允许客户端不发送证书或发送空证书，设为 true 表示拒绝客户端无证书连接，请根据实际需要设置。

```
  mqtt:
    container_name: emqx-ecp-nanomq
    image: ${IMAGE_REGISTRY}/${IMAGE_NANOMQ}-full
    restart: always
    hostname: ecp-nanomq
    ports:
      - ${MQTT_EXTERNAL_PORT}:1883
      - 38883:8883
    volumes:
      - ${ECP_CONFIG_DIR}/nanomq/nanomq.conf:/etc/nanomq.conf
      - ${ECP_CONFIG_DIR}/nanomq/cacert.pem:/etc/certs/cacert.pem:ro
      - ${ECP_CONFIG_DIR}/nanomq/cert.pem:/etc/certs/cert.pem:ro
      - ${ECP_CONFIG_DIR}/nanomq/key.pem:/etc/certs/key.pem:ro
    environment:
      NANOMQ_TLS_ENABLE: 'true'
      NANOMQ_TLS_VERIFY_PEER: 'false'
      NANOMQ_TLS_FAIL_IF_NO_PEER_CERT: 'false'
    networks:
      emqx-ecp-network:
        aliases:
          - node1
```

4. 修改 docker-compose.yaml 文件中的 main 部分，需要改动的具体内容如下：
   - `volumes` 中挂载证书文件到 ECP main 容器。示例中将证书文件都挂载到容器的 `/bc/certs` 目录下。

```
  main:
    container_name: emqx-ecp-main
    image: ${IMAGE_REGISTRY}/${IMAGE_ECP_MAIN}
    restart: always
    depends_on:
      postgres:
        condition: service_healthy
      mqtt:
        condition: service_started
      emqxagentdlproxy:
        condition: service_started
    environment:
      - GIN_MODE=release
      - ECP_DEPLOYMENT_MODE=docker
    volumes:
      - ${ECP_MAIN_VOLUME}:/bc/assets/files
      - ${ECP_CONFIG_DIR}/main/main.yaml:/bc/configs/conf.yaml
      - ${ECP_CONFIG_DIR}/main/cacert.pem:/bc/certs/cacert.pem:ro
      - ${ECP_CONFIG_DIR}/main/client-cert.pem:/bc/certs/client-cert.pem:ro
      - ${ECP_CONFIG_DIR}/main/client-key.pem:/bc/certs/client-key.pem:ro
    networks:
      - emqx-ecp-network
```

5. 修改 ECP 配置文件 configs/main/main.yaml 中的 mqtt 部分：
   - `useSSL` 设为 true，表示开启 TLS。
   - `addr` 中端口设为 8883。
   - `verifyCertificate` 表示是否要验证 NanoMQ 端证书，请根据实际需要设置。
   - `cacertFile`,  `cacertFile`,  `cacertFile` 分别为 ECP 证书文件所挂载到的容器中的路径，请确保与上一步 docker-compose.yaml 中指定的容器内路径保持一致。

```
mqtt:
  useSSL: true
  addr: mqtt:8883
  username: "ecp-mqtt-cloud"
  password: "ecp-mqtt-cloud1!"
  maxReconnectInterval: 3
  connectTimeout: 8
  cleanSession: true
  verifyCertificate: false
  cacertFile: "/bc/certs/cacert.pem"
  certFile: "/bc/certs/client-cert.pem"
  keyFile: "/bc/certs/client-key.pem"
```

6. 重启 ECP 服务。

```shell
./emqx_ecp_ctl start
```


## 检查代理服务状态 

在**系统管理**页面，点击**系统设置** -> **通用配置**，并点击展开**代理配置**部分，可以查看代理服务是否已正常连接。如果启用了 TLS/SSL 连接，也可以导出相应证书文件，在 NeuronEX 端使用。

![agent-service-status](./_assets/edge-agent-svc-status.png)

## 管理边缘代理

以系统/组织/项目管理员的身份登录 ECP，点击**工作台** -> **边缘服务**进入边缘服务页，点击页面右侧的**代理管理**按钮，打开**边缘代理管理**窗口。

![agent-manage-btn](./_assets/edge-agent-manage-btn.png)

您可在此窗口查看所有注册到 ECP 的 NeuronEX 代理。尚未被 ECP 纳管的代理显示为“未纳管“状态，实际在线情况也一并显示。您可以删除未被纳管的 NeuronEX 代理，也可以通过页面的筛选功能快速定位。

![agent-manage-list](./_assets/edge-agent-manage-list.png)

## 代理纳管边缘服务

在未被纳管的 NeuronEX 代理的**操作**列点击**纳管**按钮，输入边缘服务的名称，选择目标组织和项目，并点击**确认**按钮，将以代理方式完成对 NeuronEX 的纳管。

![agent-add-manage](./_assets/edge-agent-add-manage.png)

纳管后，**边缘代理管理**窗口中该代理的状态将更新为”已纳管“，纳管后代理将无法从代理管理页面直接删除，需要先取消对应边缘服务的纳管后再删除。

从代理管理窗口**边缘服务名称**列链接可跳转到对应边缘服务，并进行正常的边缘服务管理操作。