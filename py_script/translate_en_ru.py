
from googletrans import Translator


translator = Translator()

async def translate_en_ru(text_, src_la='ru',dest_la='en'):
    result= translator.translate(text_,  src=src_la, dest=dest_la)
    return result.text
