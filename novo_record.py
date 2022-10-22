while True:
    try:
        N = int(input())
        vm = []
        for i in range(N):
            T, D = input().split()
            vm.append(float(float(D)/float(T)))
        record = 0
        for i in range(int(len(vm))):
            if vm[i] > record:
                record = vm[i]
                print(i+1)
    except EOFError:
        break
