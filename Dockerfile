FROM python:3.10-slim
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
WORKDIR .
COPY . .
RUN pip3 install -r requirements.txt
CMD if __name__ == "__main__":
    asyncio.run(main())
