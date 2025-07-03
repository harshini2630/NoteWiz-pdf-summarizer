# import whisper

# model = whisper.load_model("base")  # or use "small", "medium", "large" for higher accuracy
# result = model.transcribe("audio2.mp3")  

# with open("transcription.txt", "w", encoding="utf-8") as f:
#     f.write(result["text"])

# print("Transcription complete. Text saved to transcription.txt")

import whisper
import time
from pathlib import Path

def transcribe_audio(input_path, output_path="transcription.txt", model_size="base"):
    """
    Transcribe audio file to text using Whisper
    
    Args:
        input_path (str): Path to audio file
        output_path (str): Path to save transcription
        model_size (str): Whisper model size (base, small, medium, large)
    """
    try:
        print(f"Loading Whisper {model_size} model...")
        start_time = time.time()
        model = whisper.load_model(model_size)
        print(f"Model loaded in {time.time() - start_time:.2f} seconds")
        
        print(f"Transcribing {input_path}...")
        result = model.transcribe(input_path)
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(result["text"])
        
        print(f"✅ Transcription saved to {output_path}")
        print(f"Transcription took {time.time() - start_time:.2f} seconds total")
        return result["text"]
    
    except Exception as e:
        print(f"❌ Error during transcription: {str(e)}")
        return None

if __name__ == "__main__":
    # Example usage
    audio_file = "audio2.mp3"  # Change to your audio file path
    transcript = transcribe_audio(audio.mp3)
    
    if transcript:
        print("\nSample of transcription:")
        print(transcript[:500] + "...")  # Print first 500 characters