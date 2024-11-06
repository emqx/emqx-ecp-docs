# 链路追踪

[OpenTelemetry 追踪](https://opentelemetry.io/docs/concepts/signals/traces/)是一个用于追踪请求在分布式系统中的流动的规范，用于追踪请求在分布式系统中的流动情况。 ECP 集成OpenTelemetry 追踪，并提供了可视化分析请求的性能和行为的能力。

## 链路追踪配置

以管理员或普通用户身份登录 ECP，您可在**系统管理**->**系统配置**-> **通用配置**查看链路追踪配置，即 [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/getting-started)的地址。

![image-20241015174431606](_assets/trace-config.png)

## 链路追踪记录

当链路数据上传到ECP后，在**工作台**界面，点击左侧 **监控运维->链路追踪**菜单即可进入链路追踪列表

![image-20241015151726616](_assets/trace-list.png)

您同样可以通过 ECP 的过滤和筛选功能，从**服务名称、span名称、attribute关键字，时间**等方面快速定位某条追踪记录。

点击 **Trace ID**,可以查看链路详情，观察链路情况。

![image-20241015172418965](_assets/trace-detail.png)