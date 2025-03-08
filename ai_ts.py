#!/usr/bin/env python

import os

from mistralai import Mistral
from mistralai.models import UserMessage
from gtts import gTTS

def main():
    api_key = os.environ["MISTRAL_API_KEY"]
    model = "mistral-tiny"

    client = Mistral(api_key=api_key)

    chat_response = client.chat.complete(
        model=model,
        messages=[UserMessage(content="Les Maths ca sert à quoi ? Tu réponderas en 1 phrases liées et en Français.")],
    )
    print(chat_response.choices[0].message.content)
    text = chat_response.choices[0].message.content
    tts = gTTS(text=text, lang='fr')
    tts.save("test.mp3")
    os.system("mpg123 -c test.mp3")


if __name__ == "__main__":
    main()
