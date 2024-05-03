import time


def test_sleep():
    start_time = time.perf_counter()
    # Change this value if you want to test different durations
    time.sleep(0.001)
    end_time = time.perf_counter()

    elapsed_time = end_time - start_time
    print(f"Requested sleep time was 0.001 seconds")
    print(f"Actual sleep time was {elapsed_time:.6f} seconds")


if __name__ == '__main__':
    test_sleep()
