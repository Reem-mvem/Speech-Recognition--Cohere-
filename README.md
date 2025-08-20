## Cohere Voice Task

Convert speech to text, generate a response with a large language model (Cohere), and play the response back as audio.

---

### Files
- `.env` → environment variables (store the API key here)  
- `main.py` → main script (record voice → transcribe → Cohere → synthesize response → play)  
- `response/` → folder containing generated audio responses  
- `result.png` → example terminal output showing transcript text  

### API Key:

[Cohere API Key](https://dashboard.cohere.com/api-keys)
 → required for generating LLM responses.

Add your key inside the .env file:
COHERE_API_KEY=your_api_key_here


### Workflow

Record audio input from microphone(convert to .wav )

Convert speech -> text (speech recognition)

Send text -> Cohere LLM for a response

Convert response text -> audio

Play the generated audio


### Note

The speech recognition API may be blocked by some ISP.

Changing DNS did not solve the issue.

Works reliably when using a VPN (preferably US or Europe).