# Running example queries from Jupyter notebook against dockerized ES

## Running Jupyter notebook with poetry

### Setting up poetry

1. install the `poetry` package manager
   ```
   pip3 install poetry
   ```
2. use python3 env
   ```
   cd Jupyter
   poetry env use python3
   ```
3. install dependencies
   ```
   poetry update
   ```

### Using the notebooks in the browser

```
poetry run jupyter-lab
```

### Running the notebooks in the IDE

1. Install the python plugin for intelliJ if you don't already have it
1. Open `Project settings` (cmd + ;) and then `Platform settings -> SDK`. Click on the plus, add a poetry environment
   and select your existing poetry environment which was installed in step 1.
1. In the `Project settings`, select Poetry in the SDK dropdown

## Running ES in a Docker container

1. Pull the ES image from Dockerhub
   ```
   docker pull docker.elastic.co/elasticsearch/elasticsearch:8.6.1
   ```
2. Create an `elastic` network
   ```
   docker network create elastic
   ```
2. Start the container with SSL disabled so you can use `http` calls
   ```
   docker run --name elasticsearch --net elastic -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -e "xpack.security.enabled=false" -t docker.elastic.co/elasticsearch/elasticsearch:8.6.1
   ```

Once you have done this, you can start the container by running the following command:

```
docker start elasticsearch
```

Instructions adapted from [elastic website](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html).