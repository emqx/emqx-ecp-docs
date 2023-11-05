# 许可证政策

NeuronEX默认安装了试用许可证，提供30个点（30 个连接和 30 个数据标签）的免费额度，您可在不安装 EMQ 许可证的情况下，运行这些商业模块。超出免费额度后，则必须安装有效的官方 EMQ 许可证。NeuronEX的功能受许可证的限制，所以请在许可证有效期前更换合适的许可证，以避免影响您的功能使用。

## 安装许可证

许可证可以多次安装，重新安装后，旧的许可证将会被删除，安装许可证有以下3种方式，：

- **官网申请许可证**

  您可直接[联系我们](https://www.emqx.com/zh/contact?product=neuron)申请不需要硬件标识绑定设备的许可证，申请许可证后，可以在进入neuronex后，点击管理 ->  许可证页面，点击重新上传，上传成功后，即可在该页面看到该许可证 的详细信息。

  ![upload-license](_assets/upload-license.png)

- **激活许可证**

  这种方式适用于希望能在网关硬件中安装NeuronEX，且能对大批量的盒子快速注册许可证的用户，需要通过注册激活码来手动激活NeuronEX，实现许可证的分发与硬件绑定。

  - 用户首先在EMQ官网下单，购买批量的NeuronEX 许可证，获取到订单号，也可以联系我们。

  - 用户进入到[NeuronEX许可证信息查询](https://site.mqttce.com/zh/neuronex-license-info)页面,输入订单号，订单号绑定的邮箱及验证码，可以查询到当前购买的许可证订单信息，保存激活码。

    ![license-order](_assets/license-order.png)

  - 进入neuronex后，点击管理 ->  许可证页面，输入刚保存的激活码，点击重新激活，NeuronEX将从官网获得许可证，并自动导入。激活成功后，重新进入[NeuronEX许可证信息查询](https://site.mqttce.com/zh/neuronex-license-info)页面,会发现剩余License数减少，若硬件设备丢失许可证后，可通过注册激活码重新下发license到硬件设备。许可证与NeuronEX的硬件标识对应一一对应，同一个设备，多次激活，剩余License数只会减1。

    ![register-license](_assets/register-license.png)

- **浮动许可证**

  - 这种方式适用于被ECP纳管或托管的NeuronEX,NeuronEX被ECP管理后，NeuronEX在在线状态下，用户可在ECP端为NeuronEX分配点位数，ECP将自动下发相应的浮动许可证给NeuronEX。NeuronEX的功能将受所被分配的点位数的限制。请合理分配点位数。

## 查看许可证

无论哪种方式安装的许可证，都可以在许可证页面查看到具体的信息。

| 内容         | 描述                                                         |
| :----------- | :----------------------------------------------------------- |
| 签发时间     | NeuronEX 申请 License 生效的时间                             |
| 过期时间     | NeuronEX 可使用的截止日期，如果 License 过期，系统将无法正常工作，您必须重新获取新的有效的 License，重新上传 License |
| 点位试用情况 | NeuronEX 可创建的所有点位总和的最大值以及正在使用的点位数    |
| 可用插件     | NeuronEX 已授权的插件。每个商业插件模块都可以在 EMQ 许可证中独立授权 |

