# Configuration Management

NeuronEX supports modifying Neuron's configuration parameters through `command line`, `environment variables`, and `configuration files`, which can provide a more flexible way of starting and running. If `command line`, `environment variables`, and `configuration files` are configured at the same time, the priority relationship between the three is: environment variable > command line > configuration file

## Command Line

```shell
-c, --config string   config file path (default "etc/neuronex.yaml")
-e, --disable_auth    select whether to enable authentication
-h, --help            help for run
-m, --manage          manage the lifecycle of eKuiper and Neuron (default true)
```
## Environment Variables

NeuronEX supports reading environment variables during the startup process to configure startup parameters. The currently supported environment variables are as follows:

| Configuration name             | Configuration function                                                            |
| ------------------------------ | --------------------------------------------------------------------------------- |
| NEURONEX_DISABLE_AUTH          | Set to 1, NeuronEX turns off Token authentication and authentication; set to 0, NeuronEX turns on Token authentication and authentication   |
| NEURON_DAEMON                  | Set to 1, the Neuron daemon runs; set to 0, Neuron runs normally                   |
| NEURON_CONFIG_DIR              | Neuron configuration file directory                                                |
| NEURON_PLUGIN_DIR              | Neuron plug-in file directory                                                      |
## Configuration File

NeuronEX provides a YAML format file to configure personalized parameters related to NeuronEX. The default configuration is as follows:

```yaml
server:
  # Neuronex listening port
  port: 8085

# Compatible neuron version
neuron:
  version: 2.6.0
  reverseProxies:
    - location: /api/neuron
      proxyPath: http://127.0.0.1:7000/api/v2

# Compatible ekuiper version
ekuiper:
  version: 1.10.2
  reverseProxies:
    - location: /api/ekuiper
      proxyPath: http://127.0.0.1:9081

# Log configuration, including log storage mode, log level, maximum value, storage count and syslog-related settings, etc.
log:
  mode: file
  level: info
  file: log/neuronex.log
  maxSize: 50000
  maxAge: 3
  maxBackups: 3
  listenAddr: "localhost:10514"
  syslogForward:
    enable: false
    priority: "info"
    network: "udp4"
    remoteAddr: ""
    tag: "neuron_ex_all"

