import ray
import time

start = time.time()
ray.init()

@ray.remote
def worker_func(pid):
    time.sleep(5)
    return f"pid {pid} finished"

def main():
  results = [worker_func.remote(i) for i in range(3)]
  print(results)
  print(ray.get(results))
  print("Elapsed:", time.time() - start) 

if __name__ == "__main__":
  main()
