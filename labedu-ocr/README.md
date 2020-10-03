# labedu-code

Labedu project

1. Build docker

```
docker build -t labedu-ocr .
```
2. Run docker
 
```
docker run -d -p 5000:5000 labedu-ocr
```

3. Querying the code

```

POST on http://localhost:5000/imgtotext
Body > form-data > {key: file_01; value: image.jpg}
Body > form-data > {key: file_02; value: image.jpg}
Body > form-data > {key: file_03; value: image.jpg}

```