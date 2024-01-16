#!/bin/bash

# example: docker build --force-rm -t homebot/base_humble ./base_humble/

# Input args
[ -z "$NAMESPACE" ] && echo "NAMESPACE is not defined, exitting!" && exit 1
[ -z "$APP" ] && echo "APP is not defined, exitting!" && exit 1

set -e  # exit on error
# set -u  # treat refs to unassigned vars as errors

# Directories
app_dir="$(pwd)/${APP}"

# Full image target
if [ -z "$TARGET" ]; then
    target="${NAMESPACE}/${APP}"
fi

if [ ${PLATFORM} == "arm64v8" ]; then
        tag=arm64v8
        target="${NAMESPACE}/${APP}:${tag}"
    fi

# Build command
build_cmd="docker build --force-rm --platform linux/${PLATFORM:-amd64} -t ${target}"

# Build
echo ">>> Building ${target}"
cd $app_dir
$build_cmd .
echo ">>> Done building ${target}"
