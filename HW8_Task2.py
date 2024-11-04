import heapq

def merge_k_lists(lists):
    min_heap = []
    for lst in lists:
        for el in lst:
            heapq.heappush(min_heap, el)
    return heapq.nsmallest(len(min_heap), min_heap)


def main():
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Sorted list:", merged_list)


if __name__ == "__main__":
    main()
