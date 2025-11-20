# -------------------------------
# OpenShift / UBI9 FastAPI image
# -------------------------------
FROM registry.access.redhat.com/ubi9/python-39:latest

LABEL maintainer="leacharchie98@gmail.com" \
      description="FastAPI app built for OpenShift (arbitrary UID compliant)"

ENV PYTHONUNBUFFERED=1 \
    PORT=8080 \
    APP_HOME=/opt/app-root/app

RUN mkdir -p /opt/app-root/run \
    && chmod -R g+rwX /opt/app-root/run \
    && find /opt/app-root/run -type d -exec chmod g+x {} +

WORKDIR ${APP_HOME}

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . ${APP_HOME}

EXPOSE 8080

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8080"]
