server {
    listen ${LISTEN_PORT};
    server_name 172.20.10.2;

    location /static {
        alias /../vol/static;
    }
}