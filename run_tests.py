from datetime import datetime
import time
import json
from sorting_algorithms import bubble_sort, insertion_sort, selection_sort, merge_sort

def run_tests():
    with open("testcases.json", "r", encoding="utf-8") as f:
        testcases = json.load(f)

    algorithms = {
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort,
        "Selection Sort": selection_sort,
        "Merge Sort": merge_sort
    }

    for name, func in algorithms.items():
        print(f"\n🔍 Testing {name}")
        total_time = 0
        total_count = 0

        start_time = datetime.now()
        print(f"⏰ Start Time: {start_time.strftime('%H:%M:%S.%f')}")

        for i, case in enumerate(testcases):
            input_data = case["input"]
            expected = case["expected"]

            start = time.perf_counter()
            result, count = func(input_data.copy())
            end = time.perf_counter()

            elapsed = end - start
            total_time += elapsed
            total_count += count

            status = "✅ PASS" if result == expected else "❌ FAIL"
            print(f"Testcase {i+1}: {case['description']}")
            print(f"Loop Count: {count}")
            print(f"Time: {elapsed:.6f} seconds")
            print(f"Status: {status}\n")

        end_time = datetime.now()
        print(f"⏰ End Time: {end_time.strftime('%H:%M:%S.%f')}")
        print(f"⏱️ Tổng thời gian: {total_time:.6f} giây")
        print(f"🔁 Tổng số vòng lặp: {total_count}")

if __name__ == "__main__":
    run_tests()
