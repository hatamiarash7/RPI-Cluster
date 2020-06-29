# DockerSwarm Gitea

Deploy Gitea server in Docker Swarm

![logo](gitea.png)

Set server's options ( [more info](https://docs.gitea.io/en-us/install-with-docker/#environments-variables) ) and run the server :

```shell
docker stack deploy --with-registry-auth -c stack.yml Gitea
```

Access gitea from **swarm-ip:3000** and install server via Register link

# Warning !!

I used images from a local registry. Change them
