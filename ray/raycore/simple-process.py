import time

start = time.time()

def worker_func(pid):
    intermediate_time = time.time() - start
    print(f"### Start worker_func() [{intermediate_time}]###")
    time.sleep(5)
    return f"pid {pid} finished"

def main():
  results = [worker_func(i) for i in range(3)]
  print(results) 
  print("Elapsed:", time.time() - start) 

if __name__ == "__main__":
  main()
