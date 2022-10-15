FROM tiangolo/uwsgi-nginx-flask:python3.8

# Setup environment
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Get project
RUN apt-get install git
RUN git config --global http.sslVerify false
RUN git clone https://github.com/danielsvens/image-api.git

# Fix static folder and permissions
WORKDIR /usr/src/app/image-api/
RUN mkdir -p /var/www/static
RUN chmod 777 /var/www/static

# Install requirements
RUN pip install -r requirements.txt

# Setup environment variables
ENV STATIC_PATH /var/www/static
ENV UWSGI_INI /usr/src/app/image-api/uwsgi.ini
