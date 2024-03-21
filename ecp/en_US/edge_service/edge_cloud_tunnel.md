# Edge Cloud Tunnel

ECP acts as a proxy for NeuronEX, allowing users to directly call NeuronEX's API through ECP.

**ANY** **/api/edgeservice/proxy/{edgeServiceId}/{path}**

- ANY refers to registering routes that match all HTTP methods, including GET, POST, PUT, PATCH, HEAD, OPTIONS, DELETE, CONNECT, TRACE.
- {edgeServiceId} refers to the ServiceID of NeuronEX in ECP.
- {path} refers to the actual URL called by NeuronEX. For detailed API information about NeuronEX, please refer to [NeuronEX HTTP API](https://docs.emqx.com/en/neuronex/latest/api/api.html).

::: tip
All APIs for Cloud-Edge Channels require the addition of a header, **Authorization**, for ECP authentication.

The value of Authorization consists of **Bearer** and the **accessToken** obtained from the ECP login API.
:::

## Example

The following creates a driver node on NeuronEX through the edge cloud tunnel.

### Request

*POST* **/api/edgeservice/proxy/{edgeServiceId}/api/neuron/node**

Request Header:
- **Authorization** Bearer \<accessToken\>

```json
{
    "name": "modbus-tcp-node",
    "plugin": "Modbus TCP"
}
```

### Response

Response status 200

```json
{
    "error": 0
}
```