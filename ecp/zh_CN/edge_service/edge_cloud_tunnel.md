# 云边通道

用户可直接通过 ECP 访问 NeuronEX 的 Dashboard 界面，其中 ECP 通过云边通道调用 NeuronEX 的 API。

**ANY**  **/api/edgeservice/proxy/{edgeServiceId}/{path}**

- ANY 指注册匹配所有 HTTP 方法的路由，包括 GET、POST、PUT、PATCH、HEAD、OPTIONS、DELETE、CONNECT、TRACE。
- {edgeServiceId} 指 NeuronEX 在 ECP 平台上的服务 ID。
- {path} 指 NeuronEX 真实调用的 URL。关于 NeuroenEX 的详细 API 请参考 [NeuronEX HTTP API](https://docs.emqx.com/zh/neuronex/latest/api/api.html)。


::: tip
所有云边通道的 API 都需要添加一个 Header, Authorization，用于 ECP 鉴权。

Authorization 的值由 Bearer 与 ECP login 接口获取的 accessToken 组成。
:::

## 示例

以下通过云边通道在 NeuronEX 上创建驱动节点。


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