FROM jjanzic/docker-python3-opencv
ADD script.py .
ADD haarcascade haarcascade
ADD sample_image sample_image
CMD [ "python","./script.py" ]
