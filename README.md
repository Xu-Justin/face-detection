# face-detection

The program will receive an image and will draw a bounding box on each detected face.

## Build the docker

```
docker build -t jstnxu/face-detection .
```

## Push built docker to docker hub

```
docker push jstnxu/face-detection:latest
```

## Pull docker from docker hub

```
docker pull jstnxu/face-detection:latest
```

## Run docker

```
docker run jstnxu/face-detection source target
```
To connect local directory with docker directory, use `-v {local_dir}:/opt/build/{docker_dir}`.

Below example code to connect local directory `D:/my_folder/` to docker directory `my_folder/` and will retrieve image from `D:/my_folder/image.jpg` and will save the result to `D:/my_folder/result.jpg`.
```
docker run -v D:/my_folder:/opt/build/my_folder jstnxu/face-detection my_folder/image.jpg my_folder/result.jpg
```

## Appendix
Some sample images provided in the docker directory.
```
sample_image/0.jpg
sample_image/1.jpg
sample_image/1.jpg
```
