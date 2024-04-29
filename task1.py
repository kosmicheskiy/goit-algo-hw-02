from queue import Queue
import uuid

#Створити чергу заявок
q = Queue()


#Функція generate_request
def generate_request():
    print("Generating request ...")
    request = uuid.uuid4()
    q.put(request)
    print(f"Request {request} added to queqe")


#Функція process_request():
def process_request():
    print("Processing request ...")
    if not q.empty(): 
        request = q.get()
        print(f"Processing request {request}")
    else:
        print(f"The is no active requests")


while True:
    try:
        generate_request()
        process_request()
    except KeyboardInterrupt:
        break       
