#!/usr/bin/python3
# -*- coding: utf-8 -*-

from fastapi.testclient import TestClient
from fasumgaz import app

client = TestClient(app)


def test_read_fasumgaz():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message":  "Fasumgaz application is online!"}


"""
  
  txt = item.text 
  res = "Error."
  if txt:
     sum = summarize(model, tokenizer, txt)
     res = sum 
  return res    
"""
