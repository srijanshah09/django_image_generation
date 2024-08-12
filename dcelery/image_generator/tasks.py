import requests
from celery import shared_task
from dcelery.settings import STABILITY_API_KEY


@shared_task(name="image_generator")
def create_image_st_ai(prompt):
    response = requests.post(
        f"https://api.stability.ai/v2beta/stable-image/generate/ultra",
        headers={
            "authorization": f"Bearer {STABILITY_API_KEY}",
            "accept": "image/*"
        },
        files={"none": ''},
        data={
            "prompt": prompt,
            "output_format": "webp",
        },
    )
    filename= prompt.replace(" ","_")
    if response.status_code == 200:
        with open(f"./{filename}.webp", 'wb') as file:
            file.write(response.content)
            return file
    else:
        raise Exception(str(response.json()))