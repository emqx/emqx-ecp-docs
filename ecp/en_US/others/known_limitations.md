# Known Limitations 



|     Feature     | Limitation                                              |
| :--------------| :-----------------------------------------------------------|
|Manage edge services|Supports up to 400 edge services.|
|Batch configuration deployment (Global Overwrite)|1. At most one batch configuration deployment job can be running within one project. <!--to confirm--><br/><br/>2. A template can support up to 50 parameters.<br/><br/>3. At most 200 edge services can be configured with this batch configuration deployment job.|
|Batch configuration deployment (Local Update)|At most one batch configuration deployment job can be running within one project.|
|Batch install of edge services|1. At most one batch install job can be running within one project. <br/>2.  At most 200 edge services can be installed in bulk<br/>3. Only direct connection mode is supported|
|Batch upgrade of edge services|At most one batch upgrade job can be running within one project.|
|     Tag management     | 1. One service can have up to 10 tags.<br/><br/> 2. One project can support up to 100 tags. |
|Organization| Supports up to 100 organizations |
|Project| 1. One organization can support up to 100 projects.<br><br> 2. One ECP platform can support up to 1000 projects. |