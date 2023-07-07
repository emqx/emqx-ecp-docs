# Release History


## v1.10.4
Release Date: 2023-07-07

### Enhancements

- Integration of Neuron 2.5.0 UI
- The Neuron (2.4 and above) managed by ECP has now exposed port 7081 to support TCP connectivity with eKuiper (versions 1.9 and above)

### Fixes

- Fixed the issue of abnormal edge service online status after modifying the authentication configuration
- Fixed the issue that Neuron's northbound MQTT exhibits abnormalities after turning off SSL
- Improved error prompts when creating or editing organizations, projects, or users
- Deleted the invalid "Quota List Description" field in Edge Service Setting
- Improved the LoadBalancer configuration example in Cluster Settings
- Fixed an issue of false prompts appearing during the startup of the EMQX cluster


## v1.10.3
Release Date: 2023-06-25

### Enhancements

- Implemented the feature to check the EMQX cluster status through "CURL"
- Add default resource configuration specifications for EMQX cluster, eKuiper, and Neuron
  
### Fixes

- Fixed issue where the EMQX startup time was incorrectly displayed in UTC format
- Fixed issue with ekuiper 1.10, where configuration cannot be configured in batch
- Fixed issue with eKuiper 1.10, where an enabled Cron task couldn't be subsequently disabled
- Fixed issue with eKuiper 1.10, where validation error would occur when editing CRON rules
- Fixed the issue with eKuiper 1.10, where changes to CRON plans didn't take effect immediately


## v1.10.2
Release Date: 2023-06-09

### Enhancements

- Integration of eKuiper 1.10.0 UI
- Restored the 'description' attribute of edge services
  
### Fixes

- Optimized error prompts for Name Cluster when installing edge services
- Optimized instance-level monitoring of edge services, ECP will generate an error prompt in case of metrics obtaining error
- Optimized prompts after closing logs
- Fixed an issue where member emails could not be displayed correctly when editing organizations and projects


## v1.10.1
Release Date: 2023-05-26

### Enhancements

- Double confirmation is required in order to proceed with the delete operation of EMQX cluster and edge services
- Log receiver configuration can now be edited again after the initial setup
  
### Fixes

- Org/project administrators now have the authorization to download JWT public keys for Neuron authentication
- Fixed email verification error that occurred during password recovery process
- Fixed email verification error when forgetting password
- Fixed issue of Configuration Key of eKuiper's source reported an oAuth error when configuring the Configuration Key


## v1.10.0
Release Date: 2023-05-12

### Enhancements

- Implemented NanoMQ's proxy management, batch import, monitoring, and alerting
- Enhanced instance-level monitoring of Neuron
- Optimized the switching between system management interface and workbench interface
- Integrate Neuron 2.4.3 UI
  
### Fixes

- Fixed the Neuron 2.4 UI document link 404 error
- Fixed the issue where the EMQX cluster and edge services did not display the storage class after adding storage classes to edge services


## v1.9.0
Release Date: 2023-04-28

### Enhancements

- Batch feature implemented for ECP installed on Kubernetes, enabling batch operations such as start, stop, restart, and delete for edge services Neuron, eKuiper
- Improved batch configuration deployment, batch configuration deployment by rule supported for eKuiper 1.9
- Visisualling of  eKuiper instance level monitor data supported
- ECP installed on Kubernetes now supports independent storage class setup for the EMQX cluster and each edge service (Neuron, eKuiper)
- Supported connection to third-party authentication systems with SAML protocol

### Fixes

- Fixed the issue of delayed offline warnings in edge services due to long ECP restart intervals
- Fixed the problem of triggering offline alarms when edge services installed in batch are online
- Fixed the issue of Chinese punctuation marks appearing in English prompts
- Support management of offline edge services
- Optimized unclear error messages when the access point of the edge services to be managed has already been managed within the project
- Fixed the issue that the edge service filter would judge those being created as offline


## v1.8.0
Release Date: 2023-04-14

### Enhancements

- Optimized alarm function; when deleting resources, the alarms associated with the deleted resources will be cleared regularly
- Added an upgrade function for edge services:
  - supporting batch upgrades and single-instance upgrades
  - compatible with eKuiper and Neuron. 
  - upgrade information will be recorded in operation audits

- Integrated eKuiper 1.9 UI and Neuron 2.4 UI
- Log levels classified by product: 
  - Neuron: debug, info, notice, warning, error
  - eKuiper: debug, info, warning, error
  - EMQX: debug, info, notice, warning, error, critical, alert, emergency
  - ECP: debug, info, warning, error, alert, emergency

- Optimized tag name display on the edge service management page

### Fixes

- Fixed the error of document links on the Neuron management page
- Fixed eKuiper's alarm error


## v1.7.0
Release Date: 2023-03-31

### Enhancements

- Implemented differential batch deployment of Neuron/eKuiper configuration distribution through template and variable replacement. An online template editor is available to generate configuration templates from existing Neuron/eKuiper instances, enabling easy batch cloning to other instances
- Refactored ECP EMQXEE proxy download program
- Support for fine-grained audit logs of edge service import

### Fixes

- Fixed the issue of incorrect audit logs will be generated when switching to the NodePort network type


## v1.6.1
Release Date: 2023-3-17

### Fixes

- Fixed an issue on Kubesphere for displaying incorrect logs for edge services


## v1.6.0
Release Date: 2023-3-10

### Enhancements

- Added support for batch deployment of edge services in a Kubernetes environment
	- Improved edge service high availability (HA)
	- Custom resource and storage reservation
	- Implemented log integration and visualization for edge services (applies only to Kubesphere)
	- Support for Neuron (2.3.4+) and eKuiper (1.7.1+)
- Completed deployment error alerts for the EMQX cluster
- Redesigned the edge service management page
- Created a helm chart based on the kubesphere/stack environment

## v1.5.0
Release Date: 2023-2-17

### Enhancements
- Unified monitoring and alarm services now support webhook notifications
- Removed invalid links in the eKuiper UI

### Fixes

- Fixed an issue where metric collectors could not be saved after the release of the new version of the alarm service
- Fixed an issue where cluster number statistics were incorrect when deleting an EMQX cluster failed

## v1.4.0
Release Date: 2023-2-3

### Enhancements

- New product name (EMQX ECP - EMQX Cloud-Edge Integrated Platform) and new logo
- Unified monitoring and alarm service
  - Implemented an alarm platform capable of aggregation, convergence, and prevention of alarm storms
  - Configured email notifications and recipients for each project
  - Supported 9 types of alerts, covering most service offline and data loss situations (Neuron 2.3.0+ and eKuiper 1.7.0+)
- Unified log service: centralized log integration and visualization for EMQX/Edge/ECP on ECP UI (requires Kubernetes and ElasticSearch)

### Fixes

- Fixed an issue where eKuiper's configuration distribution task could not start correctly

## v1.3.0
Release Date: 2023-1-13

### Enhancements

- Migrated edge service monitoring metrics to Prometheus
- Supported integration of Neuron (2.3.0+) and eKuiper (1.8.0+) metrics and displayed them on the edge service management page
- Provided a project-level statistical dashboard
- Implemented online configuration batch distribution for eKuiper 1.8.0. Users can clone configurations from running eKuiper instances and set up new eKuiper instances in batches
- Integrated Neuron 2.3.1 UI
- Improved UI/UE, refactored lists and menu panels

## v1.2.0
Release Date: 2022-12-30

### Enhancements

- Supported label management and business grouping for batch identification, filtering, and management of edge services
- Allowed users invited via email to re-edit profiles, change passwords, and switch roles

### Fixes

- Fixed the pagination issue in the integrated Neuron UI
- Fixed UI errors when installing Antares for the first time

## v1.1.0
Release Date: 2022-12-16

### Enhancements

- Improved UI/UE, making Antares' feature classification and user interaction modes more reasonable and easy to understand, thus more convenient for management, operation, and maintenance
- Supported customization of the logo, system name, and login background image

### Fixes

- Fixed an issue where the cluster name was repeated during cluster transfer
- Fixed the issue of receiving a 404 error when an invited user clicked the email link address when inviting users via email


## v1.0.0
Release Date: 2022-11-18

### Enhancements

- Supported multi-tenant and multi-project
- Implemented role-based access control and user management
- Managed the lifecycle of EMQX clusters
- Deployed EMQX Enterprise clusters on Kubernetes using the EMQX Operator
- Supported horizontal and vertical scaling of EMQX Enterprise clusters
- Supported EMQX Enterprise ClusterIP/NodePort/LoadBalancer network services
- Upgraded EMQX Enterprise clusters seamlessly
- Supported EMQX Enterprise cluster log aggregation through an external ElasticSearch log server
- Dynamically adjusted the maximum number of connections for the EMQX Enterprise cluster
- Managed edge services
- Imported existing Neuron and eKuiper services
- Provided integrated UI for remote Neuron and eKuiper management
- Provided a cloud-edge tunnel for edge agents
- Supported monitoring and alarm for Neuron and eKuiper
- Global settings
- Managed Kubernetes and hardware settings
- Managed resource quotas for EMQX Enterprise
- User registration configuration
- Operation audits
- License management

[Release history](https://github.com/emqx/EMQX-Business-Critical/releases)