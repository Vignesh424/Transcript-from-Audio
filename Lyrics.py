import assemblyai as aai

aai.settings.api_key = "649d9c788b8b473ea337f0dd105022eb"

audio_url = "BajiraoMastani.mp3"

config = aai.TranscriptionConfig(language_code="hi")
transcriber = aai.Transcriber(config=config)

transcript = transcriber.transcribe(audio_url)

with open("lyrics"+audio_url+".txt","w",encoding="utf-8") as f:
    f.write(transcript.text)
    
