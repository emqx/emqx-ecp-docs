# Upgrade Edge Services

ECP supports the upgrading of edge services hosted by ECP in batches. This functionality further streamlines the process and convenience of managing edge services, ensuring they're always running the latest, most efficient versions.

## Upgrade in Batches

To upgrade multiple edge service instances simultaneously: 

:::tip
For the compatibility and restrictions of batch upgrades, see [Known Limitations](../others/known_limitations) and [Version Compatibility](../others/version_limitations).
:::

1. Log in as system admin, organization admin, or project admin. 

2. Then click **Upgrade** in the **Edge Services** panel. 

   <img src="./_assets/edge-batch-upgrade-panel.png" style="zoom:80%;" align="middle">

3. In the popup dialog box, select the corresponding image version. Then click **Next**. 

   <img src="./_assets/edge-batch-upgrade-pop.png" style="zoom:80%;" align="middle">

4. Click to check the instances to be upgraded in batch. Click **Next**. 

   <img src="./_assets/edge-batch-upgrade-edges.png" style="zoom:80%;" align="middle">

5. Click **Confirm** to finish the setting. 

   <img src="./_assets/edge-batch-upgrade-confirm.png" style="zoom:80%;" align="middle">

## View the Upgrade Process

View the upgrade progress. Here you can observe:

- The total count of services to be upgraded, those upgraded created, ones that failed, and those currently in process.
- For any failed instances, the **Reason** column will provide information on the cause of failure.

<img src="./_assets/edge-batch-upgrade-results.png" style="zoom: 80%;" align="middle">