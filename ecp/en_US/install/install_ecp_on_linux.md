# Deploy with Docker

This section introduces how to deploy ECP with Docker. 

## Platform Support

EMQX ECP supports the following versions of operating systems: 

| OS             | Version          |
| :------------- | :--------------- |
| Ubuntu         | 20.04 or 22.04   |
| CentOS         | 7.0 or above     |
| Docker-Compose | 1.27.1 or above  |
| Docker         | 20.10.0 or above |

## Get Installation Package

If you're interested in obtaining the installation packages for ECP and EMQX Edge Operator, please visit EMQ's website and follow the steps below:

1. Navigate to the [Contact Us](https://www.emqx.com/en/contact?product=emqx-ecp) page on the EMQ website.
2. Fill out the form with your relevant contact details, including your name,  company name, email address, country or region, and your phone number. 
3. In the text field, specify your interest in the ECP and EMQX Edge Operator installation packages. Be clear about your use case and requirements to ensure that you're provided with the most suitable resources.
4. After you've filled in all the necessary details, click **Submit**.

## Install Dependencies

`htpasswd` must be installed before installing ECP:

If you are using the Ubuntu system, run the following command:

```
$ apt install apache2-utils
```

If you are using the CentOS system, run the following command:

```
$ yum install httpd-tools
```

## Install ECP

1. The installation package you receive will generally be named `emqx-ecp-install-<x.y.z>.tar.gz`, where `<x.y.z>` denotes version information.  Execute the following command to extract the installation, and switch to this directory after extraction.

   ```bash
   $ tar -xzvf emqx-ecp-install-<x.y.z>.tar.gz # decompress
   $ cd ecp-install
   ```

2. Run the command below to verify the Docker version and dependencies. 

   ```bash
   $ ./emqx_ecp_ctl precheck
   Docker is found. Version 20.10.12... passed
   Docker-Compose is found. Version 1.27.1 ... passed
   htpasswd is found... passed
   All checks passed.
   ```

3. Run the command to finish the configuration before the installation. 

   ```bash
   $ sudo ./emqx_ecp_ctl configure
   Generating docker-compose .env file
   Please input EMQX ECP image tag (default: 1.6.1):    # Specify the version to install
   Please input EMQX ECP docker registry URL (online or offline) [o/f]:  # Select online/offline install
   WARNING! Using --password via the CLI is insecure. Use --password-stdin.
   WARNING! Your password will be stored unencrypted in /root/.docker/config.json.
   Configure a credential helper to remove this warning. See
   https://docs.docker.com/engine/reference/commandline/login/#credentials-store
   
   Login Succeeded
   Please input EMQX ECP data volume path (default: /home/ecp/ecp-install/datavolumes/):    # input the path for data persistence
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

4. After the configuration, use the command below to start ECP. 

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

5. After the installation, use the `status` command to verify the operating status. 

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

## Create a Superuser

Execute the command below to create a superuser. You will need this superuser account and password to log into ECP later, so please ensure they are stored securely.

```bash
$ ./emqx_ecp_ctl create-user
Please input username:          # should be emails
Please input password:          
Please input password again:    
Please input your name:         # Set a display name for your account, for example, ECPAdmin
```

## Log in to ECP 

You have now successfully deployed ECP with Docker. Open your web browser and enter `http://localhost:8082/` (replace `localhost` with your IP address if necessary) into the address bar to access the ECP platform. 

<img src="./_assets/ECP-login.png" alt="Log in" style="zoom:50%;" />

Log in with your superuser account, and you can now start to [create users](../system_admin/user_management.md), configure [access control rules](../acl/introduction.md), and begin to set up [organizations and projects](../system_admin/introduction.md). 
