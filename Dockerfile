                From python:3-stretch
                MAINTAINER Hanna Lee <hannalee.dev@gmail.com>

                ENV INSTALL_PATH /bulksend
                RUN mkdir -p $INSTALL_PATH

                WORKDIR $INSTALL_PATH

                COPY requirements.txt requirements.txt
                RUN pip install -r requirements.txt

                COPY . .

                CMD gunicorn -c "python:config.gunicorn" "bulksend.app:create_app()"
