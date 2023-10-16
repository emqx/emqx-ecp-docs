# 基于 Kubernetes 部署 ECP

在本文中，我们将指导您如何在 kubernetes 环境中完成 ECP 及其所需组件的安装与部署。

## 安装条件

部署 EMQX ECP 前，请确认您的环境满足以下要求：

| 软件                     | 版本要求      |
| :----------------------- | :------------ |
| Kubernetes               | 1.22.0 或以上 |
| [Helm](https://helm.sh/) | 3 或以上      |

## 获取安装包

欢迎访问 EMQ 官网获取 ECP 和 EMQX Edge Operator 的安装包。

1. 进入[联系我们](https://www.emqx.com/zh/contact?product=emqx-ecp)页面。
2. 输入必要的联系信息，如姓名、公司、工作邮箱，国家和地区，以及您的联系方式。
3. 您可在下方的文本框中填写您的应用场景及需求，以便我们为您提供更好的服务。
4. 填写好以上信息后，点击**立即提交**，我们的销售将会尽快与您联系。

## 选择存储类

出于持久化 ECP 运行数据的目的，推荐为 ECP 选择合适的持久化卷存储类。

您可通过如下命令查询 Kubernetes 中可用的存储类类型：

```
$ kubectl get storageclasses
```

:::tip

推荐选择共享存储上的持久化卷，保证 ECP 运行的稳定性。

:::

## 安装依赖组件

1. 安装cert-manager

   ```bash
   $ helm repo add jetstack https://charts.jetstack.io
   $ helm repo update
   $ helm install cert-manager jetstack/cert-manager \
       --set installCRDs=true \
       --namespace cert-manager \
       --create-namespace \
       --version 'v1.11.0'
   ```

2. 安装telegraf-operator

   ```bash
   $ helm repo add influx https://helm.influxdata.com
   $ helm repo update
   $ helm -n emqx-ecp install telegraf-operator influx/telegraf-operator --create-namespace --version '1.3.10'
   $ kubectl -n emqx-ecp apply -f https://github.com/emqx/emqx-bc-iaas-hand/blob/develop/plugins/emqx_operator1_2_7/telegraf-operator-class.yaml
   ```

3. 安装 EMQX Operator。

   ```bash
   $ helm repo add emqx https://repos.emqx.io/charts
   $ helm repo update
   $ helm install emqx-operator emqx/emqx-operator \
       --namespace emqx-operator-system \
       --create-namespace \
       --set installCRDs=true  \
       --version '1.0.11-ecp.7'
   ```

4. 安装 EMQX Edge Operator。

   ```bash
   $ helm install edge-operator emqx/edge-operator \
      --version 0.0.5 \
      --namespace edge-operator-system \
      --create-namespace
   ```

5. 安装 PostgreSQL ，请选择支持共享存储的存储类。

   ```bash
   $ helm repo add bitnami https://charts.bitnami.com/bitnami
   $ helm repo update
   $ helm -n emqx-ecp install emqx-ecp-postgresql bitnami/postgresql \
       --create-namespace \
       --version '12.1.14' \
       -f emqx-ecp-chart/postgres.yaml \
       --set global.storageClass=<StorageClassName>
   ```

## 安装 EMQX ECP

1. ECP 安装包的命名规则一般为 `emqx-ecp-chart-<x.y.z>.tar.gz`，其中 `<x.y.z>`表示版本号信息。
   运行以下命令提取 ECP 安装包中的内容到本地目录，提取后的内容将位于 `./emqx-ecp-chart` 目录。

   ```bash
   $ tar -xzvf emqx-ecp-chart-<x.y.z>.tar.gz # 解压缩
   ```

2. 运行以下命令安装 EMQX ECP，请选择支持共享存储的存储类类型。

   ```bash
   $ helm -n emqx-ecp install emqx-ecp --set storage.storageClassName=<StorageClassName> emqx-ecp-chart
   ```

3. 等待 ECP 部署完成。

   ```bash
   $ kubectl -n emqx-ecp wait --for=condition=Ready pods -l 'app=emqx-ecp-main'
   pod/emqx-ecp-main-76dcb6b5c4-2f7wp condition met
   ```

## 创建超级管理员

使用下列命令创建**超级管理员**账号，请妥善保存您的超级管理员账号和密码。

```bash
$ kubectl -n emqx-ecp exec $(kubectl -n emqx-ecp get pod -l 'app=emqx-ecp-main' -o jsonpath='{.items[0].metadata.name}') \
    -c emqx-ecp-main -it -- create-init-admin.sh
Please input username:          # 请设置您的用户名，需要为 email 格式
Please input password:          # 请设置您的账户密码
Please input password again:    # 请重复您的账户密码
Please input your name:         # 请为您的账户设置一个显示名称，比如 ECPAdmin
```

## 登陆 ECP

现在您已经成功部署 ECP，ECP 的默认访问地址为 `http://{kubernetes-node-ip}:31900`。请使用超级管理员账户登录 ECP 系统，开始初始化系统设置。

![login](./_assets/login.png)

通过超级用户帐户登录后，您可开始[创建用户](../system_admin/user_management.md)，配置[访问控制规则](../acl/introduction.md)，并开始设置[组织和项目](../system_admin/introduction.md)。