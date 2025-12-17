# Docker Commands

Fill in the Docker commands you used to complete the test.

## Volume

### Create the volume

```bash
docker volume create fastapi-db
```


## Server 1

### Build the image

```bash
docker build -t shopping-server1:v1 .
```

### Run the container

```bash
docker run -d -p 8000:8000 --name con-1 -v fastapi-db:/app/db shopping-server1:v1 
```

## Server 2

### Build the image

```bash
docker build -t shopping-server2:v1 .
```

### Run the container

```bash
docker run -d -p 8001:8000 --name con-2 -v fastapi-db:/app/db shopping-server2:v1 
docker run -d -p 8001:8000 --name con-2 --mount type=volume,source=fastapi-db,target=/app/db --mount type=bind,source="%cd%/data",target=/app/data shopping-server2:v1 
```

