FROM jjanzic/docker-python3-opencv:opencv-3.2.0

WORKDIR /app
COPY haarcascade haarcascade
COPY app-argparse.py .

ENTRYPOINT [ "python3", "app-argparse.py" ]
