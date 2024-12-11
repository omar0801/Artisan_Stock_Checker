FROM python:3.10

ENV ARTISAN_STOCK_CHECKER_CONFIG_DIR=/config
# Install required Python packages, including `dotenv`
RUN pip install --no-cache-dir requests python-dotenv

RUN pip install --no-cache-dir requests

RUN mkdir -p /app/discord_webhook_script /config
COPY discord_webhook_script /app/discord_webhook_script
COPY .env /app/discord_webhook_script/.env
WORKDIR /app/discord_webhook_script

RUN chmod 755 /app /config

CMD ["python3", "check_artisan_stock_webhook.py"]