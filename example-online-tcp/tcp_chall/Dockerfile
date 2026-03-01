FROM python:3.11-slim

RUN apt-get update && apt-get install -y socat

WORKDIR /app
COPY jail.py /app/jail.py

EXPOSE 1337

# if FLAG isn't set, default to a placeholder
CMD if [ -z "${FLAG}" ]; then export FLAG="FLAG{dummy}"; fi && \
    echo -n "${FLAG}" > /app/flag.txt && \
    unset FLAG && \
    socat TCP-LISTEN:1337,reuseaddr,fork EXEC:"python3 /app/jail.py",pty,stderr,setsid,sane