# Container build system

# Environmental variables
.EXPORT_ALL_VARIABLES:
SHELL := /bin/bash
NAMESPACE := homebot
DOCKER_BUILDKIT := 1

# No files to check for these targets
.PHONY: help cleanup build

# Remove windows line endings
cleanup:
	find . -iname '*.sh' -exec sed -i -e 's/\r//' {} \;
	find . -iname '*.py' -exec sed -i -e 's/\r//' {} \;
	find . -iname '*.js' -exec sed -i -e 's/\r//' {} \;
	find . -iname '*.cmake' -exec sed -i -e 's/\r//' {} \;
	find . -iname '*.txt' -exec sed -i -e 's/\r//' {} \;

base_humble:
	APP=base_humble ./_build_it.sh
web: cleanup base_humble
	APP=web ./_build_it.sh
ps4_driver: cleanup base_humble
	APP=ps4_driver ./_build_it.sh
usb_cam_driver: cleanup base_humble
	APP=usb_cam_driver ./_build_it.sh

homebot: base_humble \
	usb_cam_driver \
	ps4_driver \
	web