ARG PYTHON_IMG_TAG=3.11.9

FROM docker.io/python:${PYTHON_IMG_TAG}-slim-bookworm
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /code
RUN mkdir -p /sock
RUN mkdir -p /logs
WORKDIR /code

COPY apt_requirements.txt /code/
RUN apt-get -y update
RUN cat apt_requirements.txt | xargs apt -y --no-install-recommends install && \
	rm -rf /var/lib/apt/lists/* && \
	apt autoremove && \
	apt autoclean

ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

COPY requirements.txt /code/

#required for gdal installation
RUN pip install --no-cache-dir setuptools==69.2.0
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir --force-reinstall numpy==2.0.0 GDAL==3.6.2
RUN rm /code/requirements.txt /code/apt_requirements.txt


COPY . /code

ENTRYPOINT [ "/code/docker/docker-entrypoint.sh" ]
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]
