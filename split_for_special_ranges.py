for _ in range(int(input())):
    n = int(input()); a = list(map(int, input().split())); temp_len = 0; cur_number = float('inf'); ans = 0
    results = []
    for i in range(n):
        cur_number = min(cur_number, a[i]); temp_len += 1
        if temp_len > cur_number:
            results.append(temp_len - 1); ans += 1; cur_number = a[i]; temp_len = 1
    results.append(temp_len); results = ' '.join(map(str, results))
    print(ans + 1, results, sep = '\n')