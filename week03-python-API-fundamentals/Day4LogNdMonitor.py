import logging
from fastapi import FastAPI , Request

app= FastAPI()
import time

logging.basicConfig(level=logging.INFO)

@app.middleware("http")
async def add_process_time(request:Request , call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    #response = await call_next(request)
    logging.info(
    f"Request : {request.method} {request.url.path} |"
    f"Status : {response.status_code} |"
    f"execute time : {process_time:.4f} sec")
    return response


#logging.info("Application started")
#logging.warning("This is a warning")
#logging.error("Something went wrong")
#logging.critical("Application not starting")
@app.get("/healthCheck")
def healthy():
    return {
       "status" : "Application is healthy"
    }
