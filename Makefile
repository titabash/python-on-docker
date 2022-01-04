NETWORK_NAME = shared-network
BUILD_MODE = api
FIX_PYTHON_TEMP = false

init:
	sh ./tools/init.sh $(FIX_PYTHON_TEMP)
start:
	@if [ -z "`docker network ls | grep $(NETWORK_NAME)`" ]; then docker network create $(NETWORK_NAME); fi
	sh ./tools/start.sh $(BUILD_MODE)
remove:
	sh ./tools/remove.sh $(BUILD_MODE)
	@if [ -n "`docker network inspect $(NETWORK_NAME) | grep \"\\"Containers\\": {}\"`" ]; then docker network rm $(NETWORK_NAME); fi
stop:
	sh ./tools/stop.sh
restart:
	sh ./tools/remove.sh $(BUILD_MODE)
	@if [ -z "`docker network ls | grep $(NETWORK_NAME)`" ]; then docker network create $(NETWORK_NAME); fi
	sh ./tools/start.sh $(BUILD_MODE)
