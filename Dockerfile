FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN chmod +x start.sh

ENV PORT=8000

CMD ["./start.sh"]
