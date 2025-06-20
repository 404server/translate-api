import traceback

from fastapi import FastAPI, Request
from pydantic import BaseModel
import uvicorn
import asyncio
from googletrans import Translator as googleTranslator
import requests
from deep_translator import GoogleTranslator
from deep_translator import MyMemoryTranslator
from translate import Translator
import translators as ts

app = FastAPI()


class TranslateRequest(BaseModel):
    source: str
    text: str
    dest: str


count = 1
translatorG = googleTranslator()


# text = "新款防走光运动短裤女假两件速干透气跑步瑜伽健身短裤休闲裤夏季"

# translatedGoogle = GoogleTranslator(source='zh-CN', target='kk')
# print("Google " + translatedGoogle)
#
# translatedMyMemory = MyMemoryTranslator(source='zh-CN', target='kk-KZ').translate(text)
# print("MyMemory " + translatedMyMemory)

# translator = Translator(from_lang="zh-cn", to_lang="kk")
# translation = translator.translate(text)
# print("Translator " + translation)

# print("Alibaba " + ts.translate_text(text, translator="alibaba", from_language="zh-cn",to_language="kk"))
# print("Deepl " + ts.translate_text(text, translator="deepl", from_language="zh",to_language="ru"))
# print("Google " + ts.translate_text(text, translator="google", from_language="zh-cn",to_language="kk"))
# print("Yandex " + ts.translate_text(text, translator="yandex", from_language="zh",to_language="ru"))
# print("translateCom " + ts.translate_text(text, translator="translateCom",to_language="ru"))
# print("sysTran " + ts.translate_text(text, translator="sysTran",from_language="en", to_language="kk"))
# print("lingvanex " + ts.translate_text(text, translator="lingvanex",from_language="zh-Hans_CN", to_language="kk_KZ"))


@app.post('/translate')
async def translate(request: TranslateRequest):
    global count
    result = ts.translate_text(
        request.text,
        translator="lingvanex",
        from_language=request.source,
        to_language=request.dest
    )
    print(f"{result} {count}")
    count += 1
    return {"translated": result}