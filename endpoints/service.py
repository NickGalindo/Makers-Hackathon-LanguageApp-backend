from typing import Dict, List
import requests

from pymongo import MongoClient

from manager.load_config import CONFIG

from endpoints.models import FrCard, EnCard

def frError(card: FrCard, mongodb: MongoClient):
    frcol = mongodb.MakerHackathon.frError

    frcol.insert_one({
        "_id": card.cardid,
        "card": card.card
    })

    return True

def frCorrect(card: FrCard, mongodb: MongoClient):
    frcol = mongodb.MakerHackathon.frCorrect

    frcol.insert_one({
        "_id": card.cardid,
        "card": card.card
    })

    return True

def enError(card: EnCard, mongodb: MongoClient):
    encol = mongodb.MakerHackathon.enError

    encol.insert_one({
        "_id": card.cardid,
        "card": card.card
    })

    return True

def enCorrect(card: EnCard, mongodb: MongoClient):
    encol = mongodb.MakerHackathon.enCorrect

    encol.insert_one({
        "_id": card.cardid,
        "card": card.card
    })

    return True

def enRecommend(mongodb: MongoClient):
    er = mongodb.MakerHackathon.enError.find({})
    cor = mongodb.MakerHackathon.enCorrect.find({})

    er_ls = []
    cor_ids = []

    for i in er:
        er_ls.append(i["card"])
    for i in cor:
        cor_ids.append(i["_id"])

    resp = requests.post("http://127.0.0.1:8001"+"/recommendEnCard", json={"history": er_ls})

    ids = resp.json()
    print(ids)
    ans = []

    en = mongodb.decks.decks.find({"language": "English"})
    for i in en:
        for c in i["cards"]:
            if str(c["id"]) in ids:
                if str(c["id"]) in cor_ids:
                    continue
                ans.append(c)


    return ans


def frRecommend(mongodb: MongoClient):
    er = mongodb.MakerHackathon.frError.find({})
    cor = mongodb.MakerHackathon.frCorrect.find({})

    er_ls = []
    cor_ids = []

    for i in er:
        er_ls.append(i["card"])
    for i in cor:
        cor_ids.append(i["_id"])

    resp = requests.post("http://127.0.0.1:8001"+"/recommendFrCard", json={"history": er_ls})

    ids = resp.json()
    print(ids)
    ans = []

    en = mongodb.decks.decks.find({"language": "French"})
    for i in en:
        for c in i["cards"]:
            if str(c["id"]) in ids:
                if str(c["id"]) in cor_ids:
                    continue
                ans.append(c)


    return ans
