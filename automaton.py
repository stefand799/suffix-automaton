def transition(n: int) -> int:
    """
    Discrete suffix automaton transition function:
    F(N) = sum of each unique integer suffix value (with leading-zero 
    deduplication). Operates as an iterative feedback system where 
    the output becomes the input for the next state: N_{t+1} = F(N_t).
    """
    s = str(n)
    return sum({int(s[i:]) for i in range(len(s))})

def simulate(seed: int, steps: int):
    current = seed
    cycle_len = 37
    
    for i in range(steps):
        if i > 0 and i % cycle_len == 0:
            print(f"{'-' * 45} [Cycle Repeat] {'-' * 45}")
        
        print(f"Step {i:3d}: {current}")
        current = transition(current)

if __name__ == "__main__":
    simulate(seed=9618, steps=75)