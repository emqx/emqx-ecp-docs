# Cloud-Edge Channel API

## EMQX Cloud-Edge Channel

ECP acts as a proxy for EMQX, allowing users to directly call EMQX's API through ECP.

*ANY* **/api/emqxee/dashboard/{clusterId}/{path}**

- ANY refers to registering routes that match all HTTP methods, including GET, POST, PUT, PATCH, HEAD, OPTIONS, DELETE, CONNECT, TRACE.
- {path} refers to the actual URL called by EMQX.

Responses are based on the invoked EMQX interface.

Example: Publish MQTT messages.
For detailed API information about EMQX, please refer to [EMQX HTTP API](https://docs.emqx.com/en/enterprise/v4.4/advanced/http-api.html)

::: tip
All APIs for Cloud-Edge Channels require the addition of a header, **Authorization**, for ECP authentication.

The value of Authorization consists of **Bearer** and the **accessToken** obtained from the ECP login API.
:::

### Request

*POST*  **/api/emqxee/dashboard/{clusterId}/api/v4/mqtt/publish**

Request Header:
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

### Response

```json   
{
  "code": 0
}
```

## NeuronEX Cloud-Edge Channel

ECP acts as a proxy for NeuronEX, allowing users to directly call NeuronEX's API through ECP.

*ANY* **/api/edgeservice/proxy/{edgeServiceId}/{path}**

- ANY refers to registering routes that match all HTTP methods, including GET, POST, PUT, PATCH, HEAD, OPTIONS, DELETE, CONNECT, TRACE.
- {path} refers to the actual URL called by NeuronEX.

Responses are based on the invoked NeuronEX interface.

Example: Add node.
For detailed API information about NeuronEX, please refer to [NeuronEX HTTP API](https://docs.emqx.com/en/neuronex/latest/api/api.html)

::: tip
All APIs for Cloud-Edge Channels require the addition of a header, **Authorization**, for ECP authentication.

The value of Authorization consists of **Bearer** and the **accessToken** obtained from the ECP login API.
:::

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