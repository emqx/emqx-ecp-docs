# Trace

[OpenTelemetry Tracing](https://opentelemetry.io/docs/concepts/signals/traces/) is a specification for tracing the flow of requests in distributed systems, used to track the flow of requests within distributed systems. ECP integrates OpenTelemetry tracing and provides the capability for visual analysis of the performance and behavior of requests.

## Trace Setting

Log in to ECP as an administrator , you can view the traceability configuration under **Administration** -> **System Setting** -> **General Setting**, which is the address of the [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/getting-started).

![image-20241015173721355](_assets/trace-config.png)

## Traceability Records

After the trace data is uploaded to ECP, on the **Workspace** interface, click the **Maintenance** -> Trace** menu on the left to enter the traceability list.

![image-20241015173421041](_assets/trace-list.png)

You can also quickly locate a specific trace record from aspects such as **service name, span name, attribute keyword, time** using ECP's filtering and sorting functions.

Click on **Trace ID** to view the trace details and observe the trace situation.

![image-20241015173511959](_assets/trace-detail.png)