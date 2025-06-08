deploy:
	docker run -d --name gar -p 1994:80 -v $(realpath .):/usr/share/nginx/html:ro -d nginx
