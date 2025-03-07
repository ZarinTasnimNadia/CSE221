import java.util.*;
import java.io.*;

public class _001 {
    public static int timeLimit = 1, batch = 0, test = 0, M = 0, N = 0;

    public static void printCase(String verdict, int batch, int test, int M, int N, ArrayList<Integer> A) {
        try {
            if (new File(verdict + ".txt").length() == 0) {
                BufferedWriter file = new BufferedWriter(new FileWriter(verdict + ".txt"));
                file.write("batch = " + batch + ";\ntest = " + test + ";\n");
                file.write("M = " + M + ";\n");
                file.write("N = " + N + ";\n");
                file.write("A = " + A + ";\n");
                file.close();
            }
            System.out.print(verdict + " on Batch " + batch + "\n");
            System.exit(1);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void checkSoln(int batch, int test, int M, int N, ArrayList<Integer> A, ArrayList<Integer> B) {
        ArrayList<Integer> C = new ArrayList<>(A);
        C.sort(null);
        for (int i = 1, j = 0, k = 0; i <= M; ++i) {
            if (j < C.size() && C.get(j) == i)
                while (j < C.size() && C.get(j) == i)
                    ++j;
            else if (k < B.size() && B.get(k) == i)
                ++k;
            else
                printCase("WrongAnswer", batch, test, M, N, new ArrayList<>(A));
            if (i == M && k != B.size())
                printCase("WrongAnswer", batch, test, M, N, new ArrayList<>(A));
        }
    }

    public static void limitTime(ArrayList<Integer> A) {
        try {
            Thread.sleep(1000 * timeLimit);
            printCase("TimeLimitExceeded", batch, test, M, N, new ArrayList<>(A));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void main(String args[]) {
        try {
            ArrayList<Integer> A = new ArrayList<>(), B = new ArrayList<>();
            int weight[] = { 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 };
            int nTest[] = { 0, 10, 100, 100, 10, 100, 10, 4000, 800, 20, 1 };
            int valN[] = { 0, 10, 10, 100, 100, 10, 10, 10, 100, 1000, 10000 };
            int valM[] = { 0, 100, 100, 100, 1000, 10000, 100000, 100, 10000, 1000000, 10000000 };
            int best = 0, score = 0, total = 0, nBatch = 10;
            Random rng = new Random();
            if (args.length == 1)
                rng = new Random(batch = Integer.parseInt(args[0]));
            if (args.length != 1 || batch < 1 || nBatch < batch) {
                BufferedReader code = new BufferedReader(new FileReader("EnterIDandLanguage.txt"));
                String ID = code.readLine().split("\\s+", 2)[0];
                code.close();
                if (new File("_001_" + ID + ".java").exists()) {
                    code = new BufferedReader(new FileReader("_001_" + ID + ".java"));
                    best = Integer.parseInt(code.readLine().split("\\s+", 4)[2]);
                    code.close();
                }
                new File("WrongAnswer.txt").createNewFile();
                new File("TimeLimitExceeded.txt").createNewFile();
                for (batch = 1; batch <= nBatch; total += weight[batch], ++batch) {
                    Process process = new ProcessBuilder("java", "_001", "" + batch).start();
                    code = new BufferedReader(new InputStreamReader(process.getInputStream()));
                    code.lines().forEach(System.out::println);
                    code.close();
                    if (process.waitFor() == 0)
                        score += weight[batch];
                }
                if (best <= score) {
                    BufferedWriter file = new BufferedWriter(new FileWriter("_001_" + ID + ".java"));
                    file.write("// " + ID + " " + score + "\n");
                    file.close();
                    new ProcessBuilder("cmd", "/c", "echo // %COMPUTERNAME% %USERNAME%>>_001_" + ID + ".java").start()
                            .waitFor();
                    file = new BufferedWriter(new FileWriter("_001_" + ID + ".java", true));
                    code = new BufferedReader(new FileReader("_001_Solution.java"));
                    file.write(code.lines().collect(java.util.stream.Collectors.joining(System.lineSeparator())));
                    code.close();
                    file.close();
                }
                System.out.print("Tentative score = " + (score / (double) total) + "/1\n");
                System.exit(0);
            }
            System.out.println("Running on Batch " + batch);
            long start = System.nanoTime();
            new Thread(() -> limitTime(A)).start();
            if (1 <= batch && batch <= nBatch) {
                for (test = 1; test <= nTest[batch]; ++test) {
                    M = valM[batch];
                    N = valN[batch];
                    A.clear();
                    B.clear();
                    for (int i = 1; i <= N; ++i)
                        A.add(1 + rng.nextInt(M + N));
                    _001_Solution.solve(M, N, new ArrayList<>(A), B);
                    checkSoln(batch, test, M, N, A, B);
                }
            }
            long finish = System.nanoTime();
            long elapsed = finish - start;
            System.out.printf("Passed Batch " + batch + " in %.9fs\n", elapsed * 1e-9);
            System.exit(0);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}