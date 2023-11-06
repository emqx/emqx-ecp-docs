# Add Existing Edge Services

ECP provides the capability to manage existing edge services. However, these services must first be added to ECP. You can add [an externally created edge service](#add-an-existing-edge-service), or [import them from csv in bulk](#add-existing-edge-services-in-bulk).

## Add an Existing Edge Service

ECP supports to add a NeuronEX instance in [direct connection mode](#direct-connection-mode).

### Direct Connection Mode

Direct connection mode generally refers to the scenario where the cluster and all edge services are within the same local area network and can access each other.

1. Log in as system admin, organization admin, or project admin. 
2. Click the **Add Edge Service** button to enter the **Add Edge Service** page.
3. Choose **Add existing service** for **Add Type**.
4. For **Category**, choose **NeuronEX**.
5. Choose **Direct Connection** for the **Connection Type**;
6. Give a name to the edge service; it should be 1 - 200 characters, and also support "-" and blank spaces. 
7. Enter the access address of the edge service. HTTP and HTTPS protocols are supported;
8. Optionally add tags to facilitate future management. For details, see [Tags](./batch_tag.md).
9. Click the **Confirm** button to finish the creation. The newly-added edge service is now displayed in the **Edge Service** section. 

<img src="./_assets/edge-service-add.png" style="zoom:60%;" align="middle"> 

### Proxy Mode

If the edge side and ECP are on separate networks and cannot establish a direct connection, it is necessary to install ECP Agent to establish a proxy connection. 

#### Operation Steps

1. Log in as system admin, organization admin, or project admin. 
2. Click the **Add Edge Service** button to enter the **Add Edge Service** page.
3. Choose **Add existing service** for the **Add Type**.
4. For **Category**, you can choose **eKuiper**, **Neuron**, **NanoMQ**, or **Customize**.
5. Choose **Proxy** for the **Connection Type**;
6. Give a name to the edge service; it should be 1 - 200 characters and also support "-" and blank spaces. 
7. Enter the access address of the edge service. HTTP and HTTPS protocols are supported;
8. Add tags to facilitate future management.
9. Click the **Confirm** button to finish the creation. The newly-added edge service is now displayed in the **Edge Service** section. 

## Add Existing Edge Services in Bulk

ECP supports batch importing of existing edge services in CSV file format. 

- Log in as system admin, organization admin, or project admin. 
- Click the **Add Edge Service** button to enter the **Add Edge Service** page.
- Choose **Import existing services in batches** for the **Add Type**.
- Import the prepared .csv file. **Note**: The file size should be less than 100 MB. 

After the import, the imported edge services will automatically be displayed in the **Edge Service** panel. Note that only data in a valid format will be imported, and the system will flag any incorrectly formatted entries.

<img src="./_assets/edge-batch-import.png" style="zoom:70%;" align="middle">

The following table provides an overview of the column names of the .csv file and their corresponding explanations:

| Column    | Explanation                       |
| --------- | --------------------------------- |
| category  | Edge product type                 |
| name      | Edge service name                 |
| nodeType  | Direct/Proxy                      |
| endpoint  | Edge service address              |
| scheme    | http/https/MQTT                   |
| agentID   | Edge agent ID, optional           |
| tagName   | Tag name, optional                |
| serviceID | Edge service ID, optional         |
| username  | Authentication username, optional |
| password  | Authentication password, optional |