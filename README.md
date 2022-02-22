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

This code will connect local directory `D:/my_folder/` to docker directory `my_folder/`.
```
docker run -v D:/my_folder:/opt/build/my_folder -it jstnxu/face-detection
```

Example of running the code using docker. The image was retrieved from `my_folder/image.jpg` and the result was saved to `my_folder/result.jpg`.
```
Image Path: my_folder/image.jpg
Output Path: my_folder/result.jpg
```

## Appendix
Some sample images provided in the docker directory.
```
sample_image/0.jpg
sample_image/1.jpg
sample_image/1.jpg
```
