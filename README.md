# inspectIT Gepard Demo Application

## inspectIT Gepard Demo

If you would like to see inspectIT Gepard in action with a demo application, you can use the docker compose examples described below.
The distributed version of the Spring PetClinic sample application is used as the target application. Also we provide a set of typical observability tools in the compose stack to demonstrate the capabilities of inspectIT Gepard.

## Launching the Demo.

_Pre-requisites:_
To launch the demo, Docker needs to be installed on your system. If you are using Docker Desktop or running Docker in a virtual machine, ensure that Docker has at least 4GB main memory assigned.

Please clone the [inspectIT Gepard-Demo GitHub repository](https://github.com/inspectIT/inspectit-gepard-demo) to your local machine.

Move into the repository-directory and execute the following command to launch the demo scenario:

```bash
docker-compose up
```

This will start all the Docker containers required for the corresponding demo scenario, including the PetClinic demo application.

You can access the demo application (PetClinic) under http://localhost:8080. Details on accessing monitoring infrastructure components are listed below.

## System Overview

The inspectIT Gepard agent is attached to the PetClinic application to collect telemetry signals, which are send to the OpenTelemetry Collector.
The demo uses InfluxDB as a time series database to store metrics, Grafana for visualization, and Jaeger for tracing.

The components of the demo are accessible via the following URLs:

- **PetClinic Application**: [http://localhost:8080](http://localhost:8080)
- **Grafana**: [http://localhost:3000](http://localhost:3000) (username: `admin`, password: `admin`)
- **Jaeger**: [http://localhost:16686](http://localhost:16686)
- **InfluxDB**: [http://localhost:8086](http://localhost:8086) (username: `novatec`, password:`password`)
