#!/bin/bash
#
# Stop all containers.

tmux kill-session -t $(basename $(git rev-parse --show-toplevel))
docker-compose -f "docker-compose-${1}.yml" stop
