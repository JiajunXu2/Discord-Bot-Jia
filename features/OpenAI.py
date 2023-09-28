def create_story(prompt):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        text = response.choices[0].text
        return (f'Prompt: {prompt} \n{text}')
    except Exception:
        return ("Error generating prompt")

    
def create_pictures(prompt):
    try:
      response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="256x256"
      )
      image_url = response['data'][0]['url']
      return image_url
    except Exception:
      return ("Error generating image")