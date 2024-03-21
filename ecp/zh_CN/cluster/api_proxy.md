# 云边通道 API 说明

## EMQX 云边通道

ECP 代理 EMQX，用户可直接通过 ECP 调用 EMQX 的 API。

*ANY*  **/api/emqxee/dashboard/{clusterId}/{path}**

- ANY 指注册匹配所有 HTTP 方法的路由，包括 GET、POST、PUT、PATCH、HEAD、OPTIONS、DELETE、CONNECT、TRACE。
- {path} 指 EMQX 真实调用的 URL。

根据调用的 EMQX 接口响应。

示例，发布 MQTT 消息。
关于 EMQX 的详细 API 请参考 [EMQX 企业版 HTTP API](https://docs.emqx.com/zh/enterprise/v4.4/advanced/http-api.html#%E6%8E%A5%E5%8F%A3%E5%AE%89%E5%85%A8)

::: tip
所有云边通道的 API 都需要添加一个 Header, Authorization，用于 ECP 鉴权。

Authorization 的值由 Bearer 与 ECP login 接口获取的 accessToken 组成。
:::

### 请求

*POST*  **/api/emqxee/dashboard/{clusterId}/api/v4/mqtt/publish**

请求头部：
- **Authorization** Bearer \<accessToken\>

```json
{
  "topic": "a/b/c",
  "payload": "Hello World",
  "qos": 1,
  "retain": false,
  "clientid": "example",
  "properties": {
    "user_properties": {
      "id": 10010,
      "name": "emqx",
      "foo": "bar"
    },
    "content_type": "text/plain"
  }
}
```

### 响应

```json   
{
  "code": 0
}
```

## NeuronEX 云边通道

ECP 代理 NeuronEX，用户可直接通过 ECP 调用 NeuronEX 的 API。

*ANY*  **/api/edgeservice/proxy/{edgeServiceId}/{path}**

- ANY 指注册匹配所有 HTTP 方法的路由，包括 GET、POST、PUT、PATCH、HEAD、OPTIONS、DELETE、CONNECT、TRACE。
- {path} 指 NeuronEX 真实调用的 URL。

根据调用的 NeuronEX 接口响应。

示例，添加节点。
关于 NeuroenEX 的详细 API 请参考 [NeuronEX HTTP API](https://docs.emqx.com/zh/neuronex/latest/api/api.html)

::: tip
所有云边通道的 API 都需要添加一个 Header, Authorization，用于 ECP 鉴权。

Authorization 的值由 Bearer 与 ECP login 接口获取的 accessToken 组成。
:::

### 请求

*POST* **/api/edgeservice/proxy/{edgeServiceId}/api/neuron/node**

请求头部：
- **Authorization** Bearer \<accessToken\>

```json
{
    "name": "modbus-tcp-node",
    "plugin": "Modbus TCP"
}
```

### 响应

响应状态 200

```json
{
    "error": 0
}
```