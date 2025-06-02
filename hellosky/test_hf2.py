try:
    from transformers import pipeline
    import torch
    
    if torch.cuda.is_available():
        # Small model test
        classifier = pipeline("sentiment-analysis", 
                            model="distilbert-base-uncased-finetuned-sst-2-english",
                            device=0)
        result = classifier("RunPod GPU is working great!")
        print(f"Sentiment analysis result: {result}")
    else:
        print("Skipping HF test - no CUDA available")
except Exception as e:
    print(f"HF test failed (this is optional): {e}")
