import http.client
import threading
import time

def send_request():
    conn = http.client.HTTPConnection("localhost:8010")
    payload = "{\n  \"chat_id\": 821785013,\n  \"text\": \"string\",\n  \"priority\": 1\n}"
    headers = {
        'Content-Type': "application/json",
        'User-Agent': "insomnia/9.3.3"
    }
    conn.request("POST", "/send_message", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    conn.close()

def spam_requests(requests_per_second):
    threads = []
    for _ in range(requests_per_second):
        t = threading.Thread(target=send_request)
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

if __name__ == "__main__":
    requests_per_second = 30
    while True:
        start_time = time.time()
        spam_requests(requests_per_second)
        elapsed_time = time.time() - start_time
        if elapsed_time < 1:
            time.sleep(1 - elapsed_time)

        # time.sleep(10)

