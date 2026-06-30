deploy:
	docker stack deploy -c stack.yml revup

logs:
	docker service logs revup_revup-web -f

ps:
	docker service ls
