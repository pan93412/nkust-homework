FROM ghcr.io/astral-sh/uv:debian

WORKDIR /app
COPY --link app.py .

EXPOSE 8080

RUN useradd -m app_user
USER app_user

CMD ["uvx", "marimo", "run", "app.py", "--port", "8080", "--host", "0.0.0.0", "--sandbox", "--headless"]
