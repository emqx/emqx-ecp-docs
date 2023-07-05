# Install ECP Edge Agent

In the edge scenario, where the edge side has its own VPC or LAN that is separated from the ECP and EMQX clusters in the cloud, the edge side requires a proxy configuration to access the cloud services. To address this scenario, ECP provides the Edge Agent component.


## Prerequisites

| OS     | Version         |
| :----- | :-------------- |
| Ubuntu | 20.04  or 22.04 |
| CentOS | 7.0 or above    |

## Get Installation Package

If you're interested in obtaining the installation packages for ECP and EMQX Edge Operator, please visit EMQ's website and follow the steps below:

1. Navigate to the [Contact Us](https://www.emqx.com/en/contact?product=emqx-ecp) page on the EMQ website.
2. Fill out the form with your relevant contact details, including your name,  company name, email address, country or region, and your phone number. 
3. In the text field, specify your interest in the ECP and EMQX Edge Operator installation packages. Be clear about your use case and requirements to ensure that you're provided with the most suitable resources.
4. After you've filled in all the necessary details, click **Submit**.

## Install ECP Edge Agent

1. The installation package you receive will generally be named `emqx-ecp-edge-agent.tar.gz`.  Execute the following command to extract the installation, and the extracted contents will be in the `./emqx-ecp-edge-agent` folder. 

   ```bash
   tar -zxvf emqx-ecp-edge-agent.tar.gz # decompress
   sudo mv ./emqx-ecp-edge-agent/emqx-bc-tunnel-agent /usr/local/bin/ # move the executables into /usr/local/bin. Note: The directories under different operating systems may differ
   ```

   <!--这里需要说明常见操作系统下的目录吧-->

2. Modify configuration file `./emqx-ecp-edge-agent/configs/conf.yaml` to set the server, log, MQTT-related, and health check intervals. Note: The file name `conf.yaml` MUST NOT be changed. 

   ```yaml
   server:
     # agent name
     name: testAgent
     # agent description
     desc: test
   
   logger:
     # Log output format, options: json or txt
     format: json
     # Whether to output logs to the console
     consoleLog: false
     # Whether to output logs to a file
     fileLog: true
     # Log file storage location
     logPath: /tmp/EMQX-BC-Tunnel-Agent.log
     # Log level
     level: DEBUG
     # Single log file size in MB
     rotationSize: 10
     # Maximum number of days to keep historical logs
     maxAge: 7
     # Maximum number of historical log files to keep
     maxBackups: 3
   
   mqtt:
     # Whether to enable SSL
     useSSL: false
     # Maximum reconnect interval in seconds
     maxReconnectInterval: 3
     # Connection timeout in seconds
     connectTimeout: 5
     # Whether to clean the session
     cleanSession: true
     # Whether to verify certificates
     verifyCertificate: false
   
   interval:
     # Interval in seconds for Agent's periodic health report
     report: 30
     # Interval in seconds for edge service health check
     health: 10
   ```

3. Run the command below to start the installation. The following parameters should be provided:

   - --orgID: Specify the organization ID. Contact the **system admin** of ECP to obtain this information.

   - --projectID: Specify the project ID. Contact the **system administrator** of ECP to obtain this information.

   - --mqttAddr: Specify the MQTT address and port.

   - --mqttUsername: Specify the MQTT username

   - --mqttPassword: Specify the MQTT password

   - --config: Specify the path of the configuration file `conf.yaml`. The default path is `./emqx-ecp-edge-agent/configs/conf.yaml`.

   ```bash
   sudo emqx-bc-tunnel-agent install --orgID {orgID} --projectID {projectID} --mqttAddr {mqttAddr} --mqttUsername {mqttUsername} --mqttPassword {mqttPassword} --config ./emqx-ecp-edge-agent/configs/
   ```

## Start the Agent

Run the command below to start the agent. 

```bash
sudo emqx-bc-tunnel-agent start
```

Once the ECP Edge Agent is started, it will automatically register with ECP. You can find it within the organization and project you specified with the start command. On how to use ECP Edge Agent to manage edge services, see [ECP Edge Agents](../edge_service/batch_import.md#ecp-edge-agent).