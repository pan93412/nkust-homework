FROM ghcr.io/marimo-team/marimo

COPY --link app.py .

EXPOSE 8080

RUN ["marimo", "run", "app.py", "--port", "8080", "--host", "0.0.0.0", "--sandbox", "--headless"]
