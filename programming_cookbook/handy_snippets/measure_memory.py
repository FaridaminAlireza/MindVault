import psutil
import os
import time

# File to save results
output_file = "usage_log.txt"

def log_usage():
    process = psutil.Process(os.getpid())
    
    # Memory usage in MB
    memory_mb = process.memory_info().rss / (1024 * 1024)
    
    # CPU usage percentage over 0.1 second
    cpu_percent = process.cpu_percent(interval=0.1)
    
    log_line = f"Memory Usage: {memory_mb:.2f} MB, CPU Usage: {cpu_percent:.2f}%\n"
    
    # Append to file
    with open(output_file, "a") as f:
        f.write(log_line)

# Example usage
if __name__ == "__main__":
    for i in range(5):
        # Simulate workload
        x = [j**2 for j in range(10**6)]
        log_usage()
        time.sleep(1)
