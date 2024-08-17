FROM python:3.10

WORKDIR /fastApi

COPY ./docker ./docker
COPY ./main.py .  

COPY ./dockerRequirements.txt ./dockerRequirements.txt

RUN pip install --no-cache-dir -r dockerRequirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
