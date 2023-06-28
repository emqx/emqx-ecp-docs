# Manage Edge Services

## Edge Service

Edge computing is a distributed computing paradigm that brings computation and data storage closer to the sources of data, like IoT devices or local edge servers. This approach minimizes latency, reduces bandwidth usage, and enhances data privacy by processing data locally rather than transmitting it to a central data center or cloud.

ECP excels in efficiently managing various aspects of edge services as part of its primary functions. These include seamless deployment, streamlined management, flexible configuration, streamlined batch operations, and optimization for popular edge software such as Neuron, eKuiper, and NanoMQ.

## Access Edge Services Workspace

After logging in, you can find the **Workspace** option in the ribbon area. Click on it to navigate to the **Workspace - Edge Services** page. This page provides an overview of the edge services hosted or managed by ECP and displays the current number of members in your organization. 

:::tip

System admin, organization admin, project admin, and regular users all can access this page, however, regular users do not have access to the administration page.

For the permission of each role, see [Permissions and Roles](../acl/authorize.md#permissions-and-roles).

:::

There are some functional differences between ECP deployments based on Kubernetes and those based on Docker. For details, see [Kubernetes vs. Docker Deployments](../install/introduction.md#feature-difference-between-kubernetes-and-docker-deployment).


![edge-list](./_assets/edge-list.png) 



Below are topics that will be covered in this chapter:

- [Project Level Overview](./edge_project_statistics.md)
- [Install Edge Service in Bulk](./batch_intall)
- [Add Existing Edge Services](./batch_import)
- [Authenticate Edge Services](./e2c)
- [Tags and Grouping](./batch_tag)
- [Upgrade Edge Services](./batch_upgrade)
- [Batch Configurations Distribution](./batch_distribution)
- [Edge Service Management & Operations](./edge_ops)

<!--Overall, I think we should state the difference between K8s and docker deployment-->
