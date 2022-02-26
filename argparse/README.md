# `face-detection:argparse`

## Build Image

```
$ docker build -t jstnxu/face-detection:argparse .
```

## Pull Image from Docker Hub

```
$ docker pull jstnxu/face-detection:argparse
```

## Run Image

To run this image, run the following code. Change `{local-directory}` with absolute path of your local directory, `{source}` with path to load the image, and `{target}` with path to save the result. Both `{source}` and `{target}` are relative path to `{local-directory}`.

```
$ docker run -v '{local-directory}':'/app/image' jstnxu/face-detection:argparse 'image/{source}' 'image/{target}' 
```

### Example on Linux

The following code will process image from `~/my_folder/my_image.jpg` and save the result to `~/my_folder/result.jpg`.

```
$ docker run -v '/home/justin-xu/my_folder':'/app/image' jstnxu/face-detection:argparse 'image/my_image.jpg' 'image/result.jpg' 
```

### Example on Windows

The following code will process image from `D:/my_folder/my_image.jpg` and save the result to `D:/my_folder/result.jpg`.

```
$ docker run -v D:/my_folder:/app/image jstnxu/face-detection:argparse image/my_image.jpg image/result.jpg 
```
