FROM python:3.8.2

LABEL maintainer="alexanderwhile@gmail.com"

ENV APPDIR /app
ENV PATH "$APPDIR/venv/bin:${PATH}"

RUN groupadd -r boi \
 && useradd -m --no-log-init -r -g boi boi

RUN mkdir -p $APPDIR \
 && chown boi:boi "$APPDIR" \
 && chmod 0755 "$APPDIR"

WORKDIR $APPDIR
USER boi

COPY ./boy.py $APPDIR
COPY ./requirements.txt $APPDIR

RUN pip install -r requirements.txt

CMD python boy.py
