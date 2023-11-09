# Installation

This chapter mainly introduces how to deploy ECP with [Kubernetes](install_ecp_on_kubernetes) or [ Docker](install_ecp_on_linux). There are certain functional differences between these two deployment methods, for details, see the table below.

After the installation, please configure [the ECP license](license_setting) and start your journey with this cloud-edge collaboration platform. 


## Kubernetes vs. Docker Deployments

|Category| Features | Kubernetes | Docker |
| :--------------| :-------| :----| :----|
|EMQX Cluster Management|Life cycle management|✅|❌|
||Horizontal and vertical scaling|✅|❌|
||Access type configuration|✅|❌|
||Upgrade|✅|❌|
||Manage existing  EMQX clusters|✅|✅|
||View EMQX cluster details|✅|✅|
||EMQX cluster transfer|✅|✅|
||EMQX connection management|✅|❌|
|Edge Service Management|Manage edge services|✅|✅|
||Manage Neuron, eKuiper and NanoMQ|✅|✅|
||Batch install|✅|❌|
|| Batch upgrade                                     |            |              |
|                         |Batch manage|✅|✅|
||Batch operate|✅|❌|
||Batch configuration deployment (Global Overwrite)|✅|✅|
||Batch configuration deployment (Local Update)|✅|✅|
||Service grouping|✅|✅|
|Monitor|Monitor EMQX clusters |✅|✅|
||Monitor edge services|✅|✅|
|Alarm|EMQX service alarm|✅|✅|
||Edge service alarms|✅|✅|
||Alarm rules and notification|✅|✅|
|Logs|EMQX log management|✅|✅|
||Neuron servcie log|✅|❌|
||eKuiper servcie log|✅|❌|
||ECP service log|✅|✅|
|Tags|Tag management|✅|✅|
|System Management|Organization management|✅|✅|
||Project management|✅|✅|
||User management|✅|✅|
||Operation audit|✅|✅|
||Resource setting|✅|✅|
||General setting|✅|✅|
||Customized login page|✅|✅|
||License management|✅|✅|
