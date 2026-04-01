.PHONY: build up down restart logs ps status clean

build:
	sudo docker-compose build

up:
	sudo docker-compose up -d
	@echo "[OK] Uygulama başlatıldı > http://localhost:5000"

down:
	sudo docker-compose down
	@echo "[STOP] Uygulama durduruldu"

restart:
	sudo docker-compose restart
	@echo "[RESTART] Yeniden başlatıldı"

logs:
	sudo docker-compose logs --tail=20 -f

ps:
	sudo docker-compose ps

status:
	@echo "=== Container Durumu ==="
	sudo docker-compose ps
	@echo ""
	@echo "=== Son Loglar ==="
	sudo docker-compose logs --tail=10

clean:
	sudo docker-compose down -v
	sudo docker system prune -f
	@echo "[CLEAN] Temizledi (volume dahil!)"