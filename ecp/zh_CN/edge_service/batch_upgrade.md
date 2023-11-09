# 升级边缘服务

ECP 支持对一个或多个**托管**的边缘服务实例，以批量的方式方便快捷地进行统一升级，提高运维效率和减少人力成本。


## 批量升级

1. 以系统/组织/项目管理员的身份登录 ECP。
2. 在边缘服务管理页，点击 **升级**。

<img src="./_assets/edge-batch-upgrade-panel.png" style="zoom:80%;" align="middle">

3. 在弹出的批量升级对话框，选择升级方式，**串行升级**或**并行升级**，选择边缘服务的**版本镜像**，点击**下一步**。

**串行升级**指，当有多个边缘服务同时升级时，ECP 将按照边缘服务列表中的顺序，依次升级每个边缘服务，当上一个边缘服务升级完成后，才会开始下一个边缘服务的升级。当升级过程中某个边缘服务升级失败时，ECP 将停止后续边缘服务的升级。

**并行升级**指，当有多个边缘服务同时升级时，ECP 将同时并行升级所有边缘服务，不会因为某个边缘服务升级失败而影响其他边缘服务的升级。


<img src="./_assets/edge-batch-upgrade-pop.png" style="zoom:60%;" align="middle">

4. 在随即出现的边缘服务列表中，选择一个或多个待升级的边缘服务。

<img src="./_assets/edge-batch-upgrade-edges.png" style="zoom:60%;" align="middle">

5. 确认以上信息，如果选择无误请点击**执行**。

<img src="./_assets/edge-batch-upgrade-confirm.png" style="zoom:60%;" align="middle">

## 查看升级进度

点击**执行**后，将弹出批量升级结果对话框，您可在此查看：

- 升级总数、成功数、失败数和执行中的边缘服务数量
- 对于升级失败的情况，您可在**原因**列查看失败原因

<img src="./_assets/edge-batch-upgrade-results.png" style="zoom:60%;" align="middle">

待升级完成后，返回边缘服务管理页，您可在此看到待升级的边缘服务实例已经升级到目标版本。