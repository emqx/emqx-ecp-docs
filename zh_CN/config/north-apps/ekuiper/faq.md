# 常见问题

## 如何基于业务需求编写 eKuiper 规则？

请参考 [eKuiper Docs](https://ekuiper.org/docs/en/latest)

## *data-stream-processing* 北向节点处于未连接状态，但 eKuiper 运行正常。

确保您创建了使用 eKuiper ECP Edge 源的规则，并且 eKuiper 会延迟连接直到规则被启动。

## 如何查看 eKuiper 是否成功从 ECP Edge 采集到数据？

1. 检查 **data-stream-processing** 节点处于连接状态，并且订阅了南向节点。
2. 通过仪表板的性能监控面板，检查 **data-stream-processing** 节点确实采集到了设备数据。
3. 如果使用 ECP EdgeEX 仪表板，可以通过规则的统计面板，检查规则确实触发了。
