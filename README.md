# pokemon-python-docker

## Deploy the application
```
docker build -t my-poke-app .
```
```
docker run -it --rm --name my-running-app my-poke-app
```

## Resources
```
./pokemon-python-docker/
│
├── src/
│   ├── main.py
│   └── requirements.txt
│
├── README.md
├── .env
└── Dockerfile
```