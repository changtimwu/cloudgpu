import torch
import time

print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")

if torch.cuda.is_available():
    print(f"CUDA version: {torch.version.cuda}")
    print(f"GPU count: {torch.cuda.device_count()}")
    
    for i in range(torch.cuda.device_count()):
        gpu = torch.cuda.get_device_properties(i)
        print(f"GPU {i}: {gpu.name}")
        print(f"  Memory: {gpu.total_memory / 1024**3:.1f} GB")
        print(f"  Compute capability: {gpu.major}.{gpu.minor}")
    
    # Simple GPU computation test
    print("\n=== GPU Computation Test ===")
    device = torch.device('cuda:0')
    
    # Create large tensors and perform operations
    a = torch.randn(5000, 5000, device=device)
    b = torch.randn(5000, 5000, device=device)
    
    start_time = time.time()
    c = torch.matmul(a, b)
    torch.cuda.synchronize()
    end_time = time.time()
    
    print(f"Matrix multiplication (5000x5000): {end_time - start_time:.2f} seconds")
    print(f"Result tensor shape: {c.shape}")
    print(f"GPU memory allocated: {torch.cuda.memory_allocated() / 1024**3:.2f} GB")
    print(f"GPU memory cached: {torch.cuda.memory_reserved() / 1024**3:.2f} GB")
    
    # Test a simple model
    print("\n=== Simple Model Test ===")
    model = torch.nn.Sequential(
        torch.nn.Linear(1000, 2000),
        torch.nn.ReLU(),
        torch.nn.Linear(2000, 1000),
        torch.nn.ReLU(),
        torch.nn.Linear(1000, 10)
    ).to(device)
    
    x = torch.randn(64, 1000, device=device)
    with torch.no_grad():
        y = model(x)
    print(f"Model output shape: {y.shape}")
    
else:
    print("CUDA not available - check GPU setup!")

