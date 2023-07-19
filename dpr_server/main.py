from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
from model import DenseRetriever
from starlette.middleware.cors import CORSMiddleware


class Item(BaseModel):
    query: str
    reviews: List[str]


class SummaryItem(BaseModel):
    query: str
    products: List[dict]


class DBItem(BaseModel):
    query: str
    reviews: List[dict]


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


DPR = DenseRetriever()


@app.post("/dpr/concat")
def retrieve_concat(item: Item):
    try:
        return {"review": DPR.run_dpr_concat(item.query, item.reviews)}
    except:
        raise HTTPException(status_code=500, detail="DPR Error")


@app.post("/dpr/split")
def retrieve_split(item: Item):
    try:
        return {"review": DPR.run_dpr_split(item.query, item.reviews)}
    except:
        raise HTTPException(status_code=500, detail="DPR Error")


@app.post("/dpr/split_db")
def retrieve_split_db(item: DBItem):
    try:
        return {"review": DPR.run_dpr_db(item.query, item.reviews)}
    except:
        raise HTTPException(status_code=500, detail="DPR Error")


@app.post("/dpr/split_v3")
def retrieve_split_v3(item: DBItem):
    try:
        return {"review": DPR.run_dpr_db_v3(item.query, item.reviews)}
    except:
        raise HTTPException(status_code=500, detail="DPR(raw) 에러")


@app.post("/dpr/concat_v3")
def retrieve_concat_v3(item: SummaryItem):
    try:
        return {"product": DPR.run_dpr_concat_v3(item.query, item.products)}
    except:
        raise HTTPException(status_code=500, detail="DPR(요약) 에러")
