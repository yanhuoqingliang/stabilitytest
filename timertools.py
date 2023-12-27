import time


def start():
    start_time = time.time()
    return start_time


def is_expired(start_time, target_time):
    current_time = time.time()
    elapsed_time = current_time - start_time
    return elapsed_time >= target_time
