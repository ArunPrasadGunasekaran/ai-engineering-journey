from fastapi import FastAPI , Request
import logging
import uuid

app=FastAPI()
logging.basicConfig(level=logging.INFO,filename="correlation_ID.log")
@app.middleware("http")
async def add_process_time(request:Request , call_next):
    correlation_id=request.headers.get("X-Correlation-ID")
    if not correlation_id:
        correlation_id = str(uuid.uuid4())
    response= await call_next(request)
    response.headers["X-Correlation-ID"]=str(correlation_id)
    logging.info(f"Method-Url >> {request.method}{request.url.path} |"
    f"Status >> {response.status_code} |"
    f"correlation_id >> {correlation_id} |")
    return response

@app.get("/correlationID")
def correlation_id():
    return{
       "message":"CorrelationID created Successful"
          }


