#!/usr/bin/env bash

podman run -ti --rm --name=ishbot \
	-v ./.env:/app/.env \
	alexanderwhile/ishbot \
	"$@"
