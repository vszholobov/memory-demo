[](./round-robin.mov)
```round-robin
# nginx.conf
events {}

http {
upstream backend {
server app1:8000;
server app2:8000;
server app3:8000;
server app4:8000;
}

    server {
        listen 80;

        location / {
            proxy_pass http://backend;
        }
    }
}
```

[](./weight-7.mov)
``` weight
# nginx.conf
events {}

http {
upstream backend {
server app1:8000 weight=7;
server app2:8000 weight=1;
server app3:8000 weight=1;
server app4:8000 weight=1;
}

    server {
        listen 80;

        location / {
            proxy_pass http://backend;
        }
    }
}
```


