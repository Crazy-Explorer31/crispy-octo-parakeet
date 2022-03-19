students, distance = list(map(int, input().split()))
if distance == 0:
    xs = list(map(int, input().split()))
    print(1, '1 '*students, sep = '\n')
else:
    xs = list(map(int, input().split()))
    for_recovery = {i : xs[i] for i in range(len(xs))}
    xs.sort(); students_tickets = {xs[0] : 1}
    cur_ticket = 2; r_finished = False
    r = 1
    for l in range(students):
        while xs[r] - xs[l] <= distance:
            students_tickets[xs[r]] = cur_ticket; cur_ticket += 1
            r += 1
            if r == students:
                r_finished = True; break
        if r_finished:
            break
        students_tickets[xs[r]] = students_tickets[xs[l]]; r += 1
        if r == students:
            break
    res = ''
    for i in range(students):
        res += str(students_tickets[for_recovery[i]]) + ' '
    print(cur_ticket - 1, res, sep = '\n')