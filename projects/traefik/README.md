# Docker Swarm Traefik v2

![logo](logo.png)

Deploy Traefik v2 in Docker Swarm

## Prerequisites

Create a network for the swarm cluster

```bash
docker network create --driver=overlay --attachable --scope=swarm traefik
```

Set your domain for Traefik dashboard and metrics in `stack.yml`. The default value is http://traefik.cluster

## Install

```bash
docker stack deploy -c stack.yml Traefik
```

## Access

- Traefik dashboard : [http://traefik.cluster](http://traefik.cluster)
- Traefik prometheus metrics : [http://traefik.cluster/metrics](http://traefik.cluster/metrics)
