from random import seed, choice
from new_example import create_example

def test_create_example():
    
    N = 8
    seed = 42

    example1 = create_example(N, seed)
    example2 = create_example(N, seed)

    assert example1 == example2, f"Expected: {example1}, Actual: {example2}"

if __name__ == "__main__":
    test_create_example()
    print("Everything passed")