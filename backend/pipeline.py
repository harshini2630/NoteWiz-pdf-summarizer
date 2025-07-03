from transcribe import transcribe_audio
from summarize import generate_summary
import argparse

def main():
    parser = argparse.ArgumentParser(description="Lecture Audio to Summary Pipeline")
    parser.add_argument("audio_file", help="Path to audio file to process")
    parser.add_argument("--model_size", default="base", 
                       choices=["base", "small", "medium", "large"],
                       help="Whisper model size (default: base)")
    parser.add_argument("--api_key", required=True, 
                       help="Gemini API key (enclose in quotes if it contains special characters)")
    args = parser.parse_args()
    
    print("\nStarting lecture processing pipeline...")
    print(f"Audio file: {args.audio_file}")
    print(f"Whisper model: {args.model_size}")
    
    # Step 1: Transcribe audio
    print("\n=== Transcription Phase ===")
    transcript = transcribe_audio(args.audio_file, model_size=args.model_size)
    if not transcript:
        print("❌ Pipeline failed at transcription phase")
        return
    
    # Step 2: Generate summary
    print("\n=== Summarization Phase ===")
    success = generate_summary(
        "transcription.txt", 
        api_key=args.api_key.strip('"\'')  # Remove any accidental quotes
    )
    
    if success:
        print("\n✅ Pipeline completed successfully!")
        print("Output files:")
        print(f"- Transcription: transcription.txt")
        print(f"- Summary: summary.txt")
    else:
        print("\n❌ Pipeline failed during summarization")

if __name__ == "__main__":
    main()