import assemblyai as aai

aai.settings.api_key = "API_KEY"

audio_url = "BajiraoMastani.mp3"

config = aai.TranscriptionConfig(language_code="hi")
transcriber = aai.Transcriber(config=config)

transcript = transcriber.transcribe(audio_url)

with open("lyrics"+audio_url+".txt","w",encoding="utf-8") as f:
    f.write(transcript.text)
    
