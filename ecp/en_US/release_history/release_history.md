# Release History

## v2.5.1
Release Date: 2025-04-30

### Enhancements

- Added AI analysis feature for tracing function
- Industrial link tracing supports querying by device name/rule ID
- Tracing query adaptive aggregation window
- SQL optimization related to tracing advanced query
- Optimization of filter conditions for tracing advanced query
- EMQX agent starts as a service

### Fixes

- Fixed the issue of abnormal display after upgrading the managed EMQX cluster
- Fixed the issue where the data access page can only display up to 10 clusters
- Fixed the issue where offline agents sometimes incorrectly show as online again
- Fixed the issue with version display after the managed cluster upgrade
- Fixed the issue with the license connection number sometimes being reset when registering the managed cluster

## v2.5.0
Release Date: 2025-03-20

### Enhancements

- EMQX Cluster Management
  - Managed EMQX v4 clusters supports unified License management through ECP
  - Managed EMQX v4/v5 clusters supports unified log collection for multiple EMQX nodes in clusters
  - Managed EMQX v4/v5 clusters support independent configuration of License management enablement
- Trace Function
  - Support end-to-end EMQX cluster and industrial trace capabilities
  - Provide more dimensions for trace query conditions
  - Provide richer dashboard visualization charts
- Security vulnerability fixes for ECP container images
- Enhanced password strength policy
- Hosted NeuronEX supports configuring default authentication settings (enable/disable)

### Fixes

- Fixed issue with special characters not being supported in email addresses during user creation

## v2.4.1
Release Date: 2025-01-10

### Enhancements

- hosted NeuronEX supports configuration of authentication on or off by default
- Support password complexity configuration

### Fixes

- Fix ECP container image security vulnerability
- Fix the error that the Root Address must be filled in with the port
- Fix the error that the email has been used when creating a user
- Create sso users without invitation, and the re-invite option reports 500 error
- Fix the error when allocating licenses for managed EMQX clusters
- Fix the problem of verifying password parameters when creating sso users


## v2.3.1
Release Date: 2024-12-17

### Enhancements

- SAML SSO displays EntityID information

### Fixes

- Fix the error  when deleting files in the file management after ECP jumps to the NeuronEX page
- Fix the page of abnormal driver list cannot be turned on the edge service monitoring page
- Fix the problem that the managed NeuronEX displayed blank when entering the Dashboard when ECP 2.2.x is upgraded to 2.3.x
- Fix the problem that the algorithm plugin name is different from the json file in the plugin zip package, and the displayed distribution result is inconsistent with the expectation
- Fix the problem that the Root Adress must fill in the port regardless of the domain name or IP
- Fix the problem that the error log is displayed when kubeconfig is not configured


## v2.4.0
Release Date: 2024-11-07

### Enhancements

- Optimized SSO Functionality
  - When SSO users log into ECP, user registration page no longer appears. ECP will automatically synchronize the organization & project permissions for SSO users
  - Dashboard now supports displaying “SP Entity ID”
  - Configuration supports "Auto Bind IdP User" option
  - New user creation supports the option to designate as SSO user
- Added Trace Functionality
  - Internal integration with OpenTelemetry
  - Supports tracing of NeuronEX and EMQX messages
  - Dashboard displays trace chain results
- Enhanced Template Features
  - Added template version management
  - Added support for template parameter modification during distribution
  - Added template sharing between multiple organizations
  - ECP Dashboard supports synchronizing NeuronEX drivers and rule configurations as ECP templates
- Added EMQX cluster registered node management, supporting helm installation method
- Added storage of NeuronEX CPU and memory metrics to Prometheus

### Fixes

- Fixed pagination issue for abnormal driver list in edge service monitoring page
- Fixed organization project frame ID flash issue
- Fixed login failure issue caused by long email addresses during first SSO login
- Fixed display issues with user information when email addresses are lengthy


## v2.3.0
Release Date: 07/12/2024

### Enhancements
- Re-adjust the overall layout of ECP
- Added a boot page after logging into ECP for the first time
- Added the ability to set up an administrator account through the UI
- Supports NeuronEX RBAC function, and the ECP role permissions are connected to the NeuronEX role permissions
- Supports NeuronEX managed Kubernetes deployment
- Supports EMQX V5 management, and support for assigning licenses to multiple managed EMQX V5 clusters
- Added EMQX V5 monitoring and alarm functions
- Optimized custom alarms and alarm rule functions
- Reconstructed tasks and audit functions

### Fixes
- Docker installation and deployment of neuronex, if the port is repeated, give a correct prompt
- After triggering a custom alarm, the alarm display interface 500 error
- The alarm link address in the alarm information email and webhook push is incorrect


## v2.2.2
Release Date: 08/05/2024

### Enhancements
- Supports EMQX v5 management and license management for EMQX v5 (>=5.7 version)
- Supports monitoring and alarming for managed EMQX v5 clusters
- Managed EMQX v4 supports port mapping for Loadbalancer and NodePort
- Display EMQX version information in connection field on the license page
- When managing EMQX clusters, dashboard displays agent exception information
- Optimize ECP backend logs

### Fixes
- Fix the configuration of SSO single sign-on options
- Fix the error in NeuronEX management prompt information
- Fix the error in deleting files after ECP jumps to the NeuronEX page


## v2.2.1
Release Date: 05/20/2024

### Enhancements
- WebSocket support for cloud-edge tunnel in NeuronEX agent mode
- Optimization of NeuronEX function management through agent
- Integration of EMQX v4.4.24 Dashboard
- Support for restart functionality in managed EMQX V4 clusters
- Managed EMQX V4 clusters can modify connection, with LB external IP remaining unchanged
- Managed EMQX V4 clusters may be deployed to specific nodes using labels and taints
- Default activation of alarm function when creating project in ECP
- Optimization of configuration for monitoring metrics in global settings

### Fixes
- Incomplete display of k8s connection configuration
- Loss of telegraf address information when reopening the log receiver after closing it
- Inability to use NeuronEX log monitoring function in docker compose deployed ECP
- ECP failing to correctly receive monitoring data reported by NeuronEX to Prometheus
- Rule debugging with WebSocket connection via cloud-edge tunnel to NeuronEX not including token parameter in the URL


## v2.2.0
Release Date: 03/27/2024

### Enhancements
- Southbound driver, rule configuration template management and configuration distribution
- Portable plugin management and plugin distribution
- Support edge service proxy connection 
- Third-party alarm display and alarm push
- Onboarding management EMQX V5
- "Hosted - docker connection" mode supports NeuronEX start and stop operations
- Support deletion of historical alarms
- Improve operation audit function
- User prompted to confirm root address on first login to ECP.
- Merge component ports and optimize ECP initialization configuration items after installation


### Fixes
- The project name is missing in the alarm storm information
- The log receiver is not configured, causing the installation of NeuronEX to fail.
- Prometheus does not use username and password, and edge monitoring always prompts that the configuration item is not set.
- After the license expires, batch deletion will report an error
- Fixed NeuronEX dynamic license sync issue after frequent ECP reboots.
- Fixed metrics statistics issue when Prometheus not configured with authentication.

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

- Fixed the issue of incorrect operation audit information for starting/restarting/stopping docker edge services in batches

- Fixed the issue where the cluster name contains multiple consecutive spaces, which may cause the cluster to fail to be deleted.

- Fixed the issue of duplicate IP addresses when setting up edge nodes

- Fix the log file of Neuron installed by docker that cannot be successfully downloaded

- Fixed the problem of missing organization and project names in the audit log information of operations such as template distribution.


## v1.11.2
Release Date: 01/14/2025

### Fixes

- Fixed the issue where debug logs could not be enabled when managing Neuron 2.6.3.

- Fixed the issue where the interface parameter for enabling debug logs in Neuron 2.6.3 driver should be debug instead of notice.

- Fixed the issue where the prompt message is incorrect when disabling node debug logs.

- Removed the custom alert threshold feature from the frontend.


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
