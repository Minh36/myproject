import json
from sorting_algorithms import bubble_sort, insertion_sort, selection_sort

def run_tests():
    with open("testcases.json", "r", encoding="utf-8") as f:
        testcases = json.load(f)

    algorithms = {
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort,
        "Selection Sort": selection_sort
    }

    for name, func in algorithms.items():
        print(f"\n🔍 Testing {name}")
        for i, case in enumerate(testcases):
            input_data = case["input"]
            expected = case["expected"]
            result = func(input_data.copy())
            status = "✅ PASS" if result == expected else "❌ FAIL"
            print(f"Testcase {i+1}: {case['description']}")
            print(f"Input: {input_data}")
            print(f"Expected: {expected}")
            print(f"Result:   {result}")
            print(f"Status: {status}\n")

if __name__ == "__main__":
    run_tests()
