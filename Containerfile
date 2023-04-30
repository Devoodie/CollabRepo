FROM python:3.11.3
WORKDIR /CollabRepo

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /CollabRepo/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /CollabRepo/requirements.txt

COPY ./src /CollabRepo/src
CMD ["uvicorn", "src.cookdevmax:app", "--host", "0.0.0.0", "--port", "8000"]