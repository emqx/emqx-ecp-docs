# Release History

## v2.2.0
Release Date: 03/27/2024

### Enhancements

- All in one install package include create-init-admin.sh
- Advance automatic decompression dashboard package
- Support custom alarm to receive user defined alarms via webhook
- New implementation for template management and template deliver to NeuronEX
- NeuronEX start & stop function which deploy by docker
- NeuronEX restart function by docker
- neuron persistent direction check， ensure the `/opt/neuronex/data` is exist.
- add the audit of start/stop/restart docker container service
- docker compose and docker-compose compatible
- init configuration when first login ECP
- New implementation for managing NeuronEX via agent
- merge telegraf syslog server port and pushGateway server port into ECP 8082 port
- merge ecp root address , telegraf address, pushGateway address
- Support adding EMQX V5 into management and dashboard view
- If first login ecp, will alert user to confirm the root address
- Add default value of docker API port
- Optimize user invite error message
- refactor custom setting
- refactor template setting page
- add polling for batch deliver result
- add batch buttons auth for NeuornEX installed by docker
- change edge config manage label position in leftSider
- set container path is disabled in NeuronEX docker config
- set default value for NeuronEX config
- add proxyManage page for managed NeuronEX
- feat delete history alarm
- recode english

### Bug Fixes

- Fix creation issue when number of edge services have reached license quota
- an issue with telegraf configuration
- fix docker compose version persistence directory rights error which may lead to prometheus repeated restart
- fix metrics statistics issue when prometheus not configured with authentication
- Fixed Elasticsearch configuration nil panic
- fix NeuronEX dynamic license sync issue when ECP reboots frequently
- add warnning setting check button
- fix check bug in setting root url
- fix show check message twice when reset password
- fix batch upgrade page sizes
- fix header change bug
- fix setting when user is docker
- change email and root loaction
- fix root lable
- fix idpSloUrl and idpSsoUrl regx and remove idpSsoUrl check when idpSsoUrl is empty
- set edge desc maxlength is 500 in create and edit edge


## v2.1.1
Release Date: 01/18/2024

### Fixes
- Fixed creation issue when the number of edge services reaches the license quota.
- Fixed Telegraf configuration issue.
- Fixed issue of missing warning setting check button.
- Fixed problem with duplicate check message when resetting password.
- Corrected batch upgrade page sizes.
- Fixed settings problem for Docker users.


## v2.1.0
Release Date: 12/29/2023

### Enhancements

- Installation package and installation process have been re-optimized and adjusted to reduce the complexity of installing and deploying ECP.
- Redesigned and implemented the detection mechanism between ECP and edge service NeuronEX.
- The architecture and implementation of ECP integrated edge service NeuronEX monitoring and alarming.
- Redesigned alarm judgement logic to support user-defined alarm rules.
- Optimize the alarm push function and support pushing alarm information by label.
- Optimized Docker hosting deployment of edge services.
- Added edge service forced deletion function.
- Improved the process of incorporating and unmanaging edge services.
- Optimized the default settings of configuration items for newly installed ECP.
- Other Dashboard adjustments and usability optimizations.

### Fixes

- Some error messages were not accurate for actions on edge services.
- Edge node name in edge service list remained unchanged after editing.


## v2.0.0
Release Date: 11/8/2023

### Enhancement

- Support managing NeuronEX through floating license

- ECP integrated new NeuronEX Dashboard

- Architecture and implementation of the new ECP integrated edge service NeuronEX

- Access and management of edge service NeuronEX

- Support batch configuration delivery for edge service NeuronEX

- Supports monitoring and alarming of edge service NeuronEX

- Support access authentication for edge service NeuronEX

- Support remote deployment, upgrade, and deletion of NeuronEX instances through docker

- Modification and adjustment of ECP global configuration page

- ECP operation audit information is pushed to the external log server

:::tip note
ECP V2 is not compatible with V1 version
:::


## v1.12.0
Release Date: 12/11/2023

### Enhancement

- Supports pushing logs and operation audits to external syslog

- Supports management of eKuiper with JWT authentication enabled

- Edge services installed based on docker support forced deletion.

- Support downloading Neuron logs from Neuron UI

- Trial License cancel the limit of no more than 3 tags

### Fixes

Fixed the issue of incorrect operation audit information for starting/restarting/stopping docker edge services in batches

Fixed the issue where the cluster name contains multiple consecutive spaces, which may cause the cluster to fail to be deleted.

Fixed the issue of duplicate IP addresses when setting up edge nodes

Fix the log file of Neuron installed by docker that cannot be successfully downloaded

Fixed the problem of missing organization and project names in the audit log information of operations such as template distribution.

## v1.11.0
Release Date: 09/15/2023

### Enhancements

- Bulk deployment, upgrade, and deletion of edge services based on Docker deployment

  - Global configuration for edge service

  - Edge node management

  - Related audit logs

- Support for configuring display items in the edge service list with checkboxes

### Fixes

- Fixed an issue where edge services could not be deleted after being removed from Kubernetes (K8S).

- Fixed various bugs related to Docker certificate configuration.


## v1.10.5
Release Date: 07/21/2023

### Enhancements

- Implemented read-only access for regular users in eKuiper v1.10 and Neuron v2.5

### Fixes

- Fixed an issue that prevented the reset of edge service offline alerts once triggered
- Fixed an issue of inaccurate progress indication during the creation and maintenance of EMQX clusters.
- Removed redundant fields from EMQX cluster resource settings
- Fixed an issue within the ECP integrated EMQX Dashboard that prevented deletion of topics containing a "/" character in the EMQX built-in database
- Fixed an issue that caused an incorrect display of project counts in the project list
- Fixed an issue with the clearing logic when filtering logs by organizations and projects
- Fixed a display issue within system-level monitoring settings


## v1.10.4
Release Date: 07/07/2023

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
Release Date: 06/25/2023

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
Release Date: 06/09/2023

### Enhancements

- Integration of eKuiper 1.10.0 UI
- Restored the 'description' attribute of edge services
  
### Fixes

- Optimized error prompts for Name Cluster when installing edge services
- Optimized instance-level monitoring of edge services, ECP will generate an error prompt in case of metrics obtaining error
- Optimized prompts after closing logs
- Fixed an issue where member emails could not be displayed correctly when editing organizations and projects


## v1.10.1
Release Date: 05/26/2023

### Enhancements

- Double confirmation is required in order to proceed with the delete operation of EMQX cluster and edge services
- Log receiver configuration can now be edited again after the initial setup
  
### Fixes

- Org/project administrators now have the authorization to download JWT public keys for Neuron authentication
- Fixed email verification error that occurred during password recovery process
- Fixed email verification error when forgetting password
- Fixed issue of Configuration Key of eKuiper's source reported an oAuth error when configuring the Configuration Key


## v1.10.0
Release Date: 05/12/2023

### Enhancements

- Implemented NanoMQ's proxy management, batch import, monitoring, and alerting
- Enhanced instance-level monitoring of Neuron
- Optimized the switching between system management interface and workbench interface
- Integrate Neuron 2.4.3 UI
  
### Fixes

- Fixed the Neuron 2.4 UI document link 404 error
- Fixed the issue where the EMQX cluster and edge services did not display the storage class after adding storage classes to edge services


## v1.9.0
Release Date: 04/28/2023

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
Release Date: 04/14/2023

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
Release Date: 03/31/2023

### Enhancements

- Implemented differential batch deployment of Neuron/eKuiper configuration distribution through template and variable replacement. An online template editor is available to generate configuration templates from existing Neuron/eKuiper instances, enabling easy batch cloning to other instances
- Refactored ECP EMQXEE proxy download program
- Support for fine-grained audit logs of edge service import

### Fixes

- Fixed the issue of incorrect audit logs will be generated when switching to the NodePort network type


## v1.6.1
Release Date: 3/17/2023

### Fixes

- Fixed an issue on Kubesphere for displaying incorrect logs for edge services


## v1.6.0
Release Date: 3/10/2023

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
Release Date: 02/17/2023

### Enhancements
- Unified monitoring and alarm services now support webhook notifications
- Removed invalid links in the eKuiper UI

### Fixes

- Fixed an issue where metric collectors could not be saved after the release of the new version of the alarm service
- Fixed an issue where cluster number statistics were incorrect when deleting an EMQX cluster failed

## v1.4.0
Release Date: 02/03/2023

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
Release Date: 01/13/2023

### Enhancements

- Migrated edge service monitoring metrics to Prometheus
- Supported integration of Neuron (2.3.0+) and eKuiper (1.8.0+) metrics and displayed them on the edge service management page
- Provided a project-level statistical dashboard
- Implemented online configuration batch distribution for eKuiper 1.8.0. Users can clone configurations from running eKuiper instances and set up new eKuiper instances in batches
- Integrated Neuron 2.3.1 UI
- Improved UI/UE, refactored lists and menu panels

## v1.2.0
Release Date: 12/30/2022

### Enhancements

- Supported label management and business grouping for batch identification, filtering, and management of edge services
- Allowed users invited via email to re-edit profiles, change passwords, and switch roles

### Fixes

- Fixed the pagination issue in the integrated Neuron UI
- Fixed UI errors when installing Antares for the first time

## v1.1.0
Release Date: 12/16/2022

### Enhancements

- Improved UI/UE, making Antares' feature classification and user interaction modes more reasonable and easy to understand, thus more convenient for management, operation, and maintenance
- Supported customization of the logo, system name, and login background image

### Fixes

- Fixed an issue where the cluster name was repeated during cluster transfer
- Fixed the issue of receiving a 404 error when an invited user clicked the email link address when inviting users via email


## v1.0.0
Release Date: 11/18/2022

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
