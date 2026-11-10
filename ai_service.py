import requests

def analyze_sentiment(text):
    url = "https://api.aiforthai.in.th/ssense"
    
    # ใส่ API Key ของตัวเองตรงนี้
    headers = {
        'Apikey': 'addultR7hIRMEcI847gL84NNgOTOvi57',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    payload = {
        'text': text
    }
    
    try:
        response = requests.post(url, headers=headers, data=payload)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"API Error: {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}