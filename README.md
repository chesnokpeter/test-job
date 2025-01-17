Тестовое задание

1. `git clone https://github.com/chesnokpeter/test-job.git`
2. Edit TELEGRAM_BOT_TOKEN in `.env` file
3. `docker compose up --build`
4. `http://localhost:8010/docs`


В будущем можно рассмотреть такие способы масштабирования:
1. Использовать собственный bot-api: \
сделать так, чтобы consumer отправлял запрос на отправление сообщения не в оффициальный telegram-bot-api, а в собственный bot-api по http/grpc/broker, а bot-api сервер уже напрямую mtproto \
это поможет увеличить скорость доставки сообщений в телеграм, а увеличить ограничения до mtproto
2. Добавить поддержку всех типов сообщений в телеграмм
