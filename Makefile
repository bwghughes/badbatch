test:
	nosetests --with-growl

ci:
	sniffer . -x --with-growl

deploy:
	dotcloud push