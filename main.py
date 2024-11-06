import uuid
from typing import Dict
from fastapi import FastAPI, HTTPException, Path
from schema import ReceiptSchema
from utils import calculate_points

app = FastAPI(
    title="Receipt Processor",
    description="A simple receipt Processor",
    version="1.0.0",
)

receipts: Dict[str, int] = {}
receipt_objects: Dict[str, ReceiptSchema] = {}


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/receipts/process",
          description="Submits a receipt for processing")
async def process_receipt(data: ReceiptSchema):
    print("Request Data: ", data.model_dump_json())

    items = data.items

    for item in items:
        if not item.shortDescription or not item.price:
            raise HTTPException(status_code=400, detail="Each item should have a 'shortDescription' and 'price' field")


    # Generate unique receipt ID ans store calculated points
    receipt_id = str(uuid.uuid4())
    receipts[receipt_id] = calculate_points(data.model_dump())

    # Save receipt objects alongside ID for convenience of access
    receipt_objects[receipt_id] = data

    print(receipts)

    return {"receipt_id": receipt_id}


@app.get("/receipts/{id}/points",
         description="Returns the points awarded for the receipt",
         responses={
             404: {"description": "Not found"},
         })
async def get_points(id: str = Path(..., description="The receipt ID for retrieving points")):
    if id not in receipts:
        raise HTTPException(status_code=404, detail="No receipt with ID '{}'".format(id))

    return {"points": receipts[id]}


@app.get("/receipts",
         description="Returns the list of all receipt IDs with points")
async def get_receipts_points():
    return receipts


@app.get("/receipts/objects",
         description="Returns the list of all receipt IDs with Receipts")
async def get_receipts_objects():
    return receipt_objects