# View EMQX Cluster Details

In the **Cluster List** panel, you can see the clusters managed/hosted within the current organization, you can choose to view them as cards or lists. 

![emqx_card](./_assets/emqx_card.png)

Below is the explanation of each field:

- **Cluster Name**: Cluster name, you can click the name (or **Cluster ID** in the list view) to enter the cluster details page to find the network information. 
- **Status**: Operational status of the cluster, could be **Creating**, **Running**, **Created** (for managed clusters, usually paired with **Register Node**), **stopping**, **stopped**, **Starting**, and **Error**.  
- **Register Node**: Register to an existing EMQX cluster. 
- **Start Time**: Indicate when the cluster is started. 
- **Replicas**: Number of EMQX nodes configured in each cluster. 
- **Create Time**: Indicate when the cluster is created.
- **Connections**: Indicate the maximum number of connections that can be established. 
- **Specifications**: Indicate the cluster specifications. For hosted clusters, ECP allows system admins to change the cluster specifications to better serve their business needs. For details, see [Resource Settings](../system_admin/resource_config.md#configure-emqx-cluster-quota).
- **Type**: Indicate whether it is a hosted cluster (created by ECP) or managed cluster (created by users). 
- **Version**: Indicate the EMQX version. 

## Check Cluster Details via EMQX Dashboard

On the **Cluster / Detail** page, you can click on **Enter Dashboard** in the top-right corner to enter the EMQX Enterprise Edition Dashboard. This web-based control panel provided by EMQX allows users to monitor the operational status and statistical metrics of server nodes and clusters. 

![console](./_assets/cluster-console.png)

EMQX Dashboard provides insights into client connectivity and subscription relationships. It also offers capabilities to configure and enable/disable plugins, manage HTTP API keys, perform hot configuration management for EMQX clusters, and conduct MQTT connection testing. 

For detailed guidance on managing and controlling EMQX Enterprise Edition, please refer to the [EMQX 4.4 Documentation](https://docs.emqx.com/zh/enterprise/v4.4/).

