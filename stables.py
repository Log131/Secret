import requests



import json
import time








async def softs_5(init, promts, scale, safety):
    
    
    s = {
    "key": "UdIXcJpmuLjV68h51zWdaPeGF5koIdM0hoyBkxClpQNPKGxZEqsCAUrFUzKb",
    
    "prompt": promts,
    
    "negative_prompt": "High pass filter, airbrush,portrait,zoomed, soft light, smooth skin,closeup, Anime, fake, cartoon, deformed, extra limbs, extra fingers, mutated hands, bad anatomy, bad proportions , blind, bad eyes, ugly eyes, dead eyes, blur, vignette, out of shot, out of focus, gaussian, closeup, monochrome, grainy, noisy, text, writing, watermark, logo, oversaturation , over saturation, over shadow, floating limbs, disconnected limbs, anime, kitsch, cartoon, penis, fake, (black and white), airbrush, drawing, illustration, boring, 3d render, long neck, out of frame, extra fingers, mutated hands, monochrome, ((poorly drawn hands)), ((poorly drawn face)), (((mutation))), (((deformed))), ((ugly)), blurry, ((bad anatomy)), (((bad proportions))), ((extra limbs)), cloned face, glitchy, bokeh, (((long neck))), (child), (childlike), 3D, 3DCG, cgstation, red eyes, multiple subjects, extra heads, close up, man, ((asian)), text, bad anatomy, morphing, messy broken legs decay, ((simple background)), deformed body, lowres, bad anatomy, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low jpeg artifacts, signature, watermark, username, blurry, out of focus, old, amateur drawing, odd, fat, morphing, ((simple background)), artifacts, signature, artist name, [blurry], disfigured, mutated, (poorly hands), messy broken legs, decay, painting, duplicate, closeup",
    
    "init_image": init,
    "num_inference_steps": "30",
    "safety_checker": safety,
    "guidance_scale": scale,
    "width": "512",
    "height": "512",
    "samples": "1",
    "num_inference_steps": "30",
    "enhance_prompt": "yes",
    "strength": 0.7,
    "seed": None,
    "webhook": None,
    "track_id": None
    
    
    }
    datas = json.dumps(s)
    
    
    
    
    headers = {
    'Content-Type': 'application/json'
    }
    res = requests.post('https://stablediffusionapi.com/api/v3/img2img',headers=headers, data=datas)




    result = json.loads(res.text)
    
    
    
    if result.get('status') == 'processing':
        time.sleep(18)
        res_ = requests.post(f'{result.get("fetch_result")}',headers=headers, data=datas)
        res_5 = json.loads(res_.text)
        print(res_5)
        return res_5.get('output')[0]
    elif result.get('status') == 'error':
        return None
    else:
        return result.get('output')[0]




async def softstexts(promts,safety,scale):

    s = {
    "key": "UdIXcJpmuLjV68h51zWdaPeGF5koIdM0hoyBkxClpQNPKGxZEqsCAUrFUzKb",
    
    "prompt": promts,
    
    "negative_prompt": "High pass filter, airbrush,portrait,zoomed, soft light, smooth skin,closeup, Anime, fake, cartoon, deformed, extra limbs, extra fingers, mutated hands, bad anatomy, bad proportions , blind, bad eyes, ugly eyes, dead eyes, blur, vignette, out of shot, out of focus, gaussian, closeup, monochrome, grainy, noisy, text, writing, watermark, logo, oversaturation , over saturation, over shadow, floating limbs, disconnected limbs, anime, kitsch, cartoon, penis, fake, (black and white), airbrush, drawing, illustration, boring, 3d render, long neck, out of frame, extra fingers, mutated hands, monochrome, ((poorly drawn hands)), ((poorly drawn face)), (((mutation))), (((deformed))), ((ugly)), blurry, ((bad anatomy)), (((bad proportions))), ((extra limbs)), cloned face, glitchy, bokeh, (((long neck))), (child), (childlike), 3D, 3DCG, cgstation, red eyes, multiple subjects, extra heads, close up, man, ((asian)), text, bad anatomy, morphing, messy broken legs decay, ((simple background)), deformed body, lowres, bad anatomy, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low jpeg artifacts, signature, watermark, username, blurry, out of focus, old, amateur drawing, odd, fat, morphing, ((simple background)), artifacts, signature, artist name, [blurry], disfigured, mutated, (poorly hands), messy broken legs, decay, painting, duplicate, closeup",
    "width": "512",
    "height": "512",
    "samples": "1",
    "num_inference_steps": "20",
    "seed": None,
    "guidance_scale": 7.5,
    "multi_lingual": "no",
    "panorama": "no",
    "self_attention": "no",
    "upscale": "no",
    "embeddings_model": None,
    "webhook": None,
    "track_id": None,
  
    "safety_checker": safety,
    
    "guidance_scale": scale

    }

    
   

    
    
    
    
    
    datas = json.dumps(s)
    headers = {
    'Content-Type': 'application/json'
    
    
    
    
    
    }
    res = requests.post('https://stablediffusionapi.com/api/v3/text2img',headers=headers, data=datas)

    result = json.loads(res.text)
    
    
    
    if result.get('status') == 'processing':
        time.sleep(18)
        res_ = requests.post(f'{result.get("fetch_result")}',headers=headers, data=datas)
        res_5 = json.loads(res_.text)
        print(res_5)
        return res_5.get('output')[0]
    elif result.get('status') == 'error':
        
        return None
    
    
    
    else:
        return result.get('output')[0]