FROM python:3.7

ENV PYTHONPATH=/

RUN chmod +x /worker-start.sh

CMD ["bash", "/worker-start.sh"]
