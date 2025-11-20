# -------------------------------
# OpenShift / UBI9 FastAPI image
# -------------------------------
FROM registry.access.redhat.com/ubi9/python-39:latest

LABEL maintainer="you@example.com" \
      description="FastAPI app built for OpenShift (arbitrary UID compliant)"

ENV PYTHONUNBUFFERED=1 \
    PORT=8080 \
    APP_HOME=/opt/app-root/app

# Create writable runtime dir
RUN mkdir -p /opt/app-root/run \
    && chmod -R g+rwX /opt/app-root/run \
    && find /opt/app-root/run -type d -exec chmod g+x {} +

WORKDIR ${APP_HOME}

# Copy dependencies and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your source code (without .git, thanks to .dockerignore)
COPY . ${APP_HOME}

EXPOSE 8080

# Optional health checdockk
HEALTHCHECK --interval=30s --timeout=3s CMD curl -f http://localhost:8080/healthz || exit 1

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8080"]
