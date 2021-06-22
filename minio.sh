#!/usr/bin/env bash

set -ex
nohup minio server . --address "${1}" &
