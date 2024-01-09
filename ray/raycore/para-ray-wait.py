import ray
import time
import random

ray.init()
start = time.time()

@ray.remote
def worker_func(pid):
    randint_val = random.randint(3, 15)
    time.sleep(randint_val)
    return f"pid {pid} finished randint={randint_val}"

def main():
    works_in_progress = [worker_func.remote(i) for i in range(10)]

    for i in range(10):
        finished, works_in_progress = ray.wait(works_in_progress, num_returns=1)
        orf = finished[0]
    
        print(ray.get(orf))
        print("Elapsed:", time.time() - start)

if __name__ == "__main__":
    main()
