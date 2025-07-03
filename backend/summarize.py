# import google.generativeai as genai

# # Configure your API key
# genai.configure(api_key="AIzaSyCtA9BxuFvKvqgnEeT38gjtUH6MsGajCKI")  # <-- Replace with your Gemini API Key

# # Read the transcript file
# with open("transcription.txt", "r", encoding="utf-8") as f:
#     transcript = f.read()

# # Create a Gemini model instance
# model = genai.GenerativeModel("gemini-pro")

# # Generate a summary
# response = model.generate_content(f"Summarize the following lecture:\n\n{transcript}")

# # Save the summary to a file
# with open("summary.txt", "w", encoding="utf-8") as f:
#     f.write(response.text)

# print("✅ Summary saved to summary.txt")



import google.generativeai as genai
import time
from pathlib import Path

def generate_summary(transcript_path, output_path="summary.txt", api_key=None):
    """
    Generate a structured summary from a transcript using Gemini
    
    Args:
        transcript_path (str): Path to transcript text file
        output_path (str): Path to save summary
        api_key (str): Gemini API key (if not already configured)
    """
    try:
        # Configure API key if provided
        if api_key:
            try:
                genai.configure(api_key=AIzaSyCtA9BxuFvKvqgnEeT38gjtUH6MsGajCKI)
            except Exception as config_error:
                print(f"❌ Error configuring Gemini API: {str(config_error)}")
                return None
        
        # Verify the API is properly configured
        if not genai.api_key:
            print("❌ Error: Gemini API key not configured")
            return None
        
        # Read the transcript
        try:
            with open(transcript_path, "r", encoding="utf-8") as f:
                transcript = f.read()
        except FileNotFoundError:
            print(f"❌ Error: Transcript file not found at {transcript_path}")
            return None
        except Exception as file_error:
            print(f"❌ Error reading transcript file: {str(file_error)}")
            return None
        
        if not transcript.strip():
            print("❌ Error: Transcript file is empty")
            return None
        
        print("Initializing Gemini model...")
        try:
            model = genai.GenerativeModel("gemini-pro")
        except Exception as model_error:
            print(f"❌ Error initializing Gemini model: {str(model_error)}")
            return None
        
        # Enhanced prompt for better summarization
        prompt = f"""
        Please analyze the following lecture transcript and create a comprehensive summary 
        with the following sections:
        
        1. **Overview**: 2-3 sentence summary of the entire lecture
        2. **Key Topics**: Bullet points of main topics covered
        3. **Important Concepts**: Detailed explanations of 3-5 most important concepts
        4. **Examples/Case Studies**: Notable examples or case studies mentioned
        5. **Conclusions**: Main takeaways or conclusions from the lecture
        
        Format the output in clear markdown with proper headings.
        
        Lecture Transcript:
        {transcript}
        """
        
        print("Generating summary...")
        start_time = time.time()
        try:
            response = model.generate_content(prompt)
            summary = response.text
        except Exception as gen_error:
            print(f"❌ Error during content generation: {str(gen_error)}")
            return None
        
        # Save the summary
        try:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(summary)
        except Exception as save_error:
            print(f"❌ Error saving summary: {str(save_error)}")
            return None
        
        print(f"✅ Summary saved to {output_path}")
        print(f"Summarization took {time.time() - start_time:.2f} seconds")
        return summary
    
    except Exception as e:
        print(f"❌ Unexpected error during summarization: {str(e)}")
        return None