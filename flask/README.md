# `face-detection:flask`

## Build Image

```
$ docker build -t jstnxu/face-detection:flask .
```

## Pull Image from Docker Hub

```
$ docker pull jstnxu/face-detection:flask
```

## Run Image

To run this image, run the following code. Change `{local-port}` with your local port (or just use 5000).

```
$ docker run -p {local-port}:5000 jstnxu/face-detection:flask
```

After running the code, open `localhost:{local-port}` on your browser.
