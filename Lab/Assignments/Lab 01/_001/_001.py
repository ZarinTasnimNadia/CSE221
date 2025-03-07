import os, sys, time, random, threading, subprocess
from _001_Solution import solve
timeLimit = 1
batch = 0
test = 0
M = 0
N = 0
def printCase(verdict, batch, test, M, N, A):
    if os.path.getsize(verdict + ".txt") == 0:
        with open(verdict + ".txt", "w") as file:
            file.write("batch = " + str(batch) + ";\ntest = " + str(test) + ";\n")
            file.write("M = " + str(M) + ";\n")
            file.write("N = " + str(N) + ";\n")
            file.write("A = " + str(A) + ";\n")
    print(verdict + " on Batch " + str(batch), flush=True)
    os._exit(1)
def checkSoln(batch, test, M, N, A, B):
    C = A.copy()
    C.sort()
    i = 1
    j = 0
    k = 0
    while i <= M:
        if j < len(C) and C[j] == i:
            while j < len(C) and C[j] == i:
                j += 1
        elif k < len(B) and B[k] == i:
            k += 1
        else:
            printCase("WrongAnswer", batch, test, M, N, A.copy())
        if i == M and k != len(B):
            printCase("WrongAnswer", batch, test, M, N, A.copy())
        i += 1
def limitTime(A):
    time.sleep(timeLimit)
    printCase("TimeLimitExceeded", batch, test, M, N, A.copy())
A = []
B = []
weight = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
nTest = [0, 10, 100, 100, 10, 100, 10, 4000, 800, 20, 1]
valN = [0, 10, 10, 100, 100, 10, 10, 10, 100, 1000, 10000]
valM = [0, 100, 100, 100, 1000, 10000, 100000, 100, 10000, 1000000, 10000000]
best = 0
score = 0
total = 0
nBatch = 10
if len(sys.argv) == 2:
    batch = int(sys.argv[1])
    random.seed(batch)
if len(sys.argv) != 2 or batch < 1 or nBatch < batch:
    ID = ""
    with open("EnterIDandLanguage.txt") as file:
        ID = file.readline().split()[0]
    if os.path.exists("_001_" + ID + ".py"):
        with open("_001_" + ID + ".py") as file:
            best = int(file.readline().split()[2])
    with open("WrongAnswer.txt", "w") as file:
        pass
    with open("TimeLimitExceeded.txt", "w") as file:
        pass
    batch = 1
    while batch <= nBatch:
        process = subprocess.run("pypy _001.py " + str(batch), capture_output=True, text=True)
        if process.stdout:
            print(process.stdout, end="")
        if process.stderr:
            print(process.stderr, end="")
        if process.returncode == 0:
            score += weight[batch]
        total += weight[batch]
        batch += 1
    if best <= score:
        with open("_001_" + ID + ".py", "w") as file:
            file.write("# " + ID + " " + str(score) + "\n")
        subprocess.run("cmd /c echo # %COMPUTERNAME% %USERNAME%>>_001_" + ID + ".py")
        with open("_001_" + ID + ".py", "a") as file:
            with open("_001_Solution.py") as code:
                file.write(code.read())
    print("Tentative score = " + str(score / total) + "/1", flush=True)
    os._exit(0)
print("Running on Batch " + str(batch), flush=True)
start = time.time()
threading.Thread(target=limitTime, args=(A,), daemon=True).start()
if 1 <= batch and batch <= nBatch:
    test = 1
    while test <= nTest[batch]:
        M = valM[batch]
        N = valN[batch]
        A.clear()
        B.clear()
        i = 1
        while i <= N:
            A.append(random.randint(1, M + N))
            i += 1
        solve(M, N, A.copy(), B)
        checkSoln(batch, test, M, N, A, B)
        test += 1
finish = time.time()
elapsed = finish - start
print("Passed Batch " + str(batch) + " in " + f"{elapsed:.9f}" + "s", flush=True)
os._exit(0)