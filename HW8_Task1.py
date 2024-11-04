import heapq
import random

def without_heap(arr):
    print("Without Heap:")
    total_len = 0
    while len(arr) > 1:
        print(f"Cabels = {arr}")

        joint_len = arr[0] +arr[1]
        arr = arr[2:]
        arr.append(joint_len)
        total_len += joint_len

        print(f"Joint len = {joint_len}")
        print(f" Total len = {total_len}\n")


def with_heap(arr):
    print("With Heap:")
    heapq.heapify(arr)

    total_len = 0

    while len(arr) > 1:
        print(f"Cabels = {arr}")

        joint_len = heapq.heappop(arr) + heapq.heappop(arr)
        heapq.heappush(arr, joint_len)
        total_len += joint_len

        print(f"Joint len = {joint_len}")
        print(f" Total len = {total_len}\n")


def main():
    init_cabels = random.sample(range(1, 1000), 5)
    print(f"Initial cabel lengths: {init_cabels}")
    without_heap(init_cabels)
    with_heap(init_cabels)


if __name__ == '__main__':
    main()