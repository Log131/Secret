import requests



import json
import asyncio








async def softs_5(init, promts, scale, safety):
    
    
    s = {
    "key": "UdIXcJpmuLjV68h51zWdaPeGF5koIdM0hoyBkxClpQNPKGxZEqsCAUrFUzKb",
    
    "prompt": promts,
    
    "negative_prompt": "",
    
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
        asyncio.sleep(18)
        res_ = requests.post(f'{result.get("fetch_result")[0]}',headers=headers, data=datas)
        res_5 = json.loads(res_.text)
        print(res_5)
        return res_5.get('output')[0]
    elif result.get('status') == 'error':
        return None
    else:
        return result.get('output')[0]

async def softs_6(init, promts, scale, safety):
    
    
    s = {
    "key": "UdIXcJpmuLjV68h51zWdaPeGF5koIdM0hoyBkxClpQNPKGxZEqsCAUrFUzKb",
    
    "prompt": promts,
    
    "negative_prompt": "",
    
    "init_image": init,
    "safety_checker": safety,
    "guidance_scale": scale,
    "model_id": "deliberate",
    "prompt": "papercraft, quilling, layers, landscape",
    "width": "512",
    "height": "512",
    "samples": "1",
    "num_inference_steps": "30",
    "enhance_prompt": "yes",
    "guidance_scale": 7.5,
    "strength": 0.7,
    "scheduler": "UniPCMultistepScheduler",
    "seed": None,
    "lora_model": None,
    "tomesd": "yes",
    "use_karras_sigmas": "yes",
    "vae": None,
    "lora_strength": None,
    "embeddings_model": None,
    "webhook": None,
    "track_id": None
    
    }
    datas = json.dumps(s)
    
    
    
    
    headers = {
    'Content-Type': 'application/json'
    }
    res = requests.post('https://stablediffusionapi.com/api/v4/dreambooth/img2img',headers=headers, data=datas)




    result = json.loads(res.text)
    
    
    
    if result.get('status') == 'processing':
        asyncio.sleep(18)
        res_ = requests.post(f'{result.get("fetch_result")[0]}',headers=headers, data=datas)
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
    
    "negative_prompt": "",
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

        asyncio.sleep(18)
        res_ = requests.post(f'{result.get("fetch_result")[0]}',headers=headers, data=datas)
        res_5 = json.loads(res_.text)
        print(res_5)
        return res_5.get('output')[0]
    elif result.get('status') == 'error':
        
        return None
    
    
    
    else:
        return result.get('output')[0]


async def softstexts5(promts,safety,scale):

    s = {
    "key": "UdIXcJpmuLjV68h51zWdaPeGF5koIdM0hoyBkxClpQNPKGxZEqsCAUrFUzKb",
    
    "prompt": promts,
    "model_id": "deliberate",
    "negative_promt": "",
    "width": "512",
    "height": "512",
    "samples": "1",
    "num_inference_steps": "30",
    "enhance_prompt": "yes",
    "seed": None,
    "multi_lingual": "no",
    "panorama": "no",
    "self_attention": "no",
    "upscale": "no",
    "embeddings_model": None,
    "lora_model": None,
    "tomesd": "yes",
    "use_karras_sigmas": "yes",
    "vae": None,
    "lora_strength": None,
    "scheduler": "UniPCMultistepScheduler",
    "webhook": None,
    "track_id": None,
    "safety_checker": safety,
    
    "guidance_scale": scale

    }

    
   

    
    
    
    
    
    datas = json.dumps(s)
    headers = {
    'Content-Type': 'application/json'
    
    
    
    }
    res = requests.post('https://stablediffusionapi.com/api/v4/dreambooth',headers=headers, data=datas)

    result = json.loads(res.text)
    
    
    
    if result.get('status') == 'processing':

        asyncio.sleep(18)
        res_ = requests.post(f'{result.get("fetch_result")[0]}',headers=headers, data=datas)
        res_5 = json.loads(res_.text)
        print(res_5)
        return res_5.get('output')[0]
    elif result.get('status') == 'error':
        
        return None
    
    
    
    else:
        return result.get('output')[0]
