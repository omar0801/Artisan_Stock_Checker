# Define variables
DOCKER_IMAGE=matthewdesouza/artisan-stock-checker:latest
CONTAINER_NAME=artisan-stock-checker
CONFIG_DIR=artisan_data


# Prepare the artisan_data directory with correct permissions
prepare:
	mkdir -p $(CONFIG_DIR)
	sudo chown -R $(shell id -u):$(shell id -g) $(CONFIG_DIR)
	chmod -R u+rw $(CONFIG_DIR)

# Target to build the Docker image
build:
	docker build -t $(DOCKER_IMAGE) .

# Target to run the bot
bot:
	@echo "Starting the container and following logs..."
	docker run -it \
		--restart unless-stopped \
		--name $(CONTAINER_NAME) \
		--user $$(id -u):$$(id -g) \
		-e ARTISAN_STOCK_CHECKER_CONFIG_DIR=/config \
		-v $$(pwd)/$(CONFIG_DIR):/config \
		$(DOCKER_IMAGE)

# Target to restart the container
restart:
	@$(MAKE) clean
	@$(MAKE) bot

# Target to stop the container
stop:
	docker stop $(CONTAINER_NAME)

clean-files:
	sudo rm -rf artisan_data

# Target to remove the container
clean-docker:
	docker rm -f $(CONTAINER_NAME)

# Target to check logs
logs:
	docker logs -f $(CONTAINER_NAME)

# Target to run prepare, build, and bot sequentially
run: prepare build bot
	@echo "Prepare, build, and bot steps completed successfully!"

fresh: clean-docker clean-files prepare build bot
	@echo "Fresh steps completed successfully!"
