# 基于 Docker 的部署

在本文中，我们将指导您如何在  Docker 中完成 ECP 及其所需组件的安装部署。

## 安装条件

EMQX ECP 部署前，请确认您的环境满足以下要求：

| OS             | 版本要求       |
| :------------- | :------------- |
| Ubuntu         | 20.04 或 22.04 |
| CentOS         | 7.0 或以上     |
| Docker-Compose | 1.27.1 或以上  |
| Docker         | 20.10.0 或以上 |

## 获取安装包

欢迎访问 EMQ 官网获取 ECP 的安装包。

1. 进入[联系我们](https://www.emqx.com/zh/contact?product=emqx-ecp)页面。
2. 输入必要的联系信息，如姓名、公司、工作邮箱，国家和地区，以及您的联系方式。
3. 您可在下方的文本框中填写您的应用场景及需求，以便我们为您提供更好的服务。
4. 填写好以上信息后，点击**立即提交**，我们的销售将会尽快与您联系。

## 安装依赖组件

在 Ubuntu 系统中，使用以下命令安装 htpasswd：

```bash
$ apt install apache2-utils
```

在 CentOS 系统中，使用以下命令安装 htpasswd：

```bash
$ yum install httpd-tools
```

## 安装 EMQX ECP

1. ECP 安装包的命名规则一般为 `emqx-ecp-chart-<x.y.z>.tar.gz`，其中 `<x.y.z>`表示版本号信息。
   运行以下命令提取 ECP 安装包中的内容到本地目录，提取后的内容将位于`./ecp-install` 目录，并切换到该目录下。

   ```bash
   $ tar -xzvf emqx-ecp-install-<x.y.z>.tar.gz # 解压缩
   $ cd ecp-install
   ```

2. 运行以下命令，检查依赖组件及 docker 版本。

   ```bash
   $ ./emqx_ecp_ctl precheck
   Docker is found. Version 20.10.12... passed
   Docker-Compose is found. Version 1.27.1 ... passed
   htpasswd is found... passed
   All checks passed.
   ```

3. 运行下列命令，进行安装前配置。

   ```bash
   $ sudo ./emqx_ecp_ctl configure
   Generating docker-compose .env file
   Please input EMQX ECP image tag (default: 1.6.1):    # 输入需要安装的版本
   Please input EMQX ECP docker registry URL (online or offline) [o/f]:  # 选择在线或者离线安装
   WARNING! Using --password via the CLI is insecure. Use --password-stdin.
   WARNING! Your password will be stored unencrypted in /root/.docker/config.json.
   Configure a credential helper to remove this warning. See
   https://docs.docker.com/engine/reference/commandline/login/#credentials-store
   
   Login Succeeded
   Please input EMQX ECP data volume path (default: /home/ecp/ecp-install/datavolumes/):    # 输入持久化数据保存路径
   Generating docker-compose env file ...
   Generating Prometheus web auth configuration ...
   Generating ECP config files ...
   Generating uiproxy/nginx.conf ...
   Generating prometheus/web.yml ...
   Generating main/emqx-bc.pub ...
   Generating main/emqx-bc ...
   Generating main/emqx-bc.lic ...
   Generating main/main.yaml ...
   Generating agents/emqxee-agent ...
   Loading ECP Agents ...
   Checking docker network emqx-ecp-network for ECP services
   4b989e94a93b54e69e6e10a9788035ff7a60d8cf9ef27daec6e24e112b482dcf
   All configurations are done.
   ```

4. 配置完成后，可以使用下列命令启动 ECP。

   ```bash
   $ sudo ./emqx_ecp_ctl start
   Creating emqx-ecp-prometheus-config   ... done
   Creating emqx-ecp-alertmanager-config ... done
   Creating emqx-ecp-ui                  ... done
   Creating emqx-ecp-mqtt                ... done
   Creating emqx-ecp-postgresql          ... done
   Creating emqx-ecp-alertmanager        ... done
   Creating emqx-ecp-redis               ... done
   Creating emqx-ecp-prometheus          ... done
   Creating emqx-ecp-main                ... done
   ```

5. 在系统启动后，通过 `status` 命令检查服务状态，确保所有容器都处于正常运行状态。

   ```bash
   $ sudo ./emqx_ecp_ctl status
               Name                          Command               State                                                  Ports
   ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   emqx-ecp-alertmanager          /bin/alertmanager --config ...   Up      0.0.0.0:39093->9093/tcp,:::39093->9093/tcp
   emqx-ecp-alertmanager-config   /emqx-antares-prometheus-c ...   Up      9091/tcp
   emqx-ecp-main                  /bc/emqx-bc-service              Up      8082/tcp
   emqx-ecp-mqtt                  /usr/bin/docker-entrypoint ...   Up      11883/tcp, 0.0.0.0:38083->18083/tcp,:::38083->18083/tcp, 0.0.0.0:31883->1883/tcp,:::31883->1883/tcp,
                                                                           4369/tcp, 4370/tcp, 5369/tcp, 6369/tcp, 6370/tcp, 8081/tcp, 8083/tcp, 8084/tcp, 8883/tcp
   emqx-ecp-postgresql            docker-entrypoint.sh postgres    Up      0.0.0.0:15432->5432/tcp,:::15432->5432/tcp
   emqx-ecp-prometheus            /bin/prometheus --config.f ...   Up      0.0.0.0:39090->9090/tcp,:::39090->9090/tcp
   emqx-ecp-prometheus-config     /emqx-antares-prometheus-c ...   Up      9091/tcp
   emqx-ecp-redis                 /opt/bitnami/scripts/redis ...   Up      0.0.0.0:16379->6379/tcp,:::16379->6379/tcp
   emqx-ecp-ui                    /docker-entrypoint.sh ngin ...   Up      80/tcp, 0.0.0.0:8082->8080/tcp,:::8082->8080/tcp
   ```

## 创建超级管理员

使用下列命令创建**超级管理员**账号，请妥善保存您的超级管理员账号和密码。

```bash
$ ./emqx_ecp_ctl create-user
Please input username:          # 请设置您的用户名，需要为email格式
Please input password:          # 请设置您的账户密码
Please input password again:    # 请重复您的账户密码
Please input your name:         # 请为您的账户设置一个显示名称，比如 ECPAdmin
```

## 登陆 ECP

现在您已经成功部署 ECP，ECP 的默认访问地址为 `http://{您的机器IP}:31900` 。请使用超级管理员账户登录 ECP 系统，开始初始化系统设置。

![login](./_assets/login.png)

通过超级用户帐户登录后，您可开始[创建用户](../system_admin/user_management.md)，配置[访问控制规则](../acl/introduction.md)，并开始设置[组织和项目](../system_admin/introduction.md)。
