#include<bits/extc++.h>
using namespace std;
int timeLimit = 1, batch = 0, test = 0, M = 0, N = 0;
extern void solve(int M, int N, vector<int> A, vector<int>& B);
inline string to_string(vector<int> x) {
    string z = "vector<int>({";
    if (!x.empty()) z += " " + to_string(x[0]);
    for (int i = 1; i < x.size(); ++i)
        z += ", " + to_string(x[i]);
    return z + " })";
}
inline void printCase(string verdict, int batch, int test, int M, int N, vector<int> A) {
    if (ifstream(verdict + ".txt").peek() == ifstream::traits_type::eof()) {
        ofstream fout(verdict + ".txt");
        fout << "batch = " << to_string(batch) << ";\ntest = " << to_string(test) << ";\n";
        fout << "M = " << to_string(M) << ";\n";
        fout << "N = " << to_string(N) << ";\n";
        fout << "A = " << to_string(A) << ";\n";
    }
    cout << verdict << " on Batch " << batch << "\n", exit(1);
}
inline void checkSoln(int batch, int test, int M, int N, vector<int>& A, vector<int>& B) {
    vector<int> C(A);
    sort(C.begin(), C.end());
    for (int i = 1, j = 0, k = 0; i <= M; ++i) {
        if (j < C.size() && C[j] == i) while (j < C.size() && C[j] == i) ++j;
        else if (k < B.size() && B[k] == i) ++k;
        else printCase("WrongAnswer", batch, test, M, N, A);
        if (i == M && k != B.size()) printCase("WrongAnswer", batch, test, M, N, A);
    }
}
inline void limitTime(vector<int>& A) {
    this_thread::sleep_for(chrono::seconds(timeLimit));
    printCase("TimeLimitExceeded", batch, test, M, N, A);
}
int main(int argc, char** argv) {
    vector<int> A, B;
    int weight[] = { 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 };
    int nTest[] = { 0, 10, 100, 100, 10, 100, 10, 4000, 800, 20, 1 };
    int valN[] = { 0, 10, 10, 100, 100, 10, 10, 10, 100, 1000, 10000 };
    int valM[] = { 0, 100, 100, 100, 1000, 10000, 100000, 100, 10000, 1000000, 10000000 };
    int best = 0, score = 0, total = 0, nBatch = 10;
    if (argc == 2) srand(batch = stoi(argv[1]));
    if (argc != 2 || batch < 1 || nBatch < batch) {
        string ID, temp;
        ifstream("EnterIDandLanguage.txt") >> ID;
        if (ifstream("_001_" + ID + ".cpp"))
            ifstream("_001_" + ID + ".cpp") >> temp >> temp >> best;
        ofstream("WrongAnswer.txt").close();
        ofstream("TimeLimitExceeded.txt").close();
        for (batch = 1; batch <= nBatch; total += weight[batch], ++batch)
            if (!system((".\\a.exe " + to_string(batch)).c_str()))
                score += weight[batch];
        if (best <= score) {
            ofstream("_001_" + ID + ".cpp") << "// " << ID << " " << score << "\n";
            system(("echo // %COMPUTERNAME% %USERNAME%>>_001_" + ID + ".cpp").c_str());
            ofstream("_001_" + ID + ".cpp", ios::binary | ios::app) << ifstream("_001_Solution.cpp", ios::binary).rdbuf();
        }
        cout << "Tentative score = " << double(score) / total << "/1\n", exit(0);
    }
    cout << "Running on Batch " << batch << endl;
    chrono::_V2::system_clock::time_point start = chrono::high_resolution_clock::now();
    thread(limitTime, ref(A)).detach();
    if (1 <= batch && batch <= nBatch) {
        for (test = 1; test <= nTest[batch]; ++test) {
            M = valM[batch], N = valN[batch], A.clear(), B.clear(), A.reserve(N);
            for (int i = 1; i <= N; A.push_back(1 + rand() % (M + N)), ++i);
            solve(M, N, A, B), checkSoln(batch, test, M, N, A, B);
        }
    }
    chrono::_V2::system_clock::time_point finish = chrono::high_resolution_clock::now();
    chrono::_V2::system_clock::duration elapsed = chrono::duration_cast<chrono::nanoseconds>(finish - start);
    cout << fixed << setprecision(9) << "Passed Batch " << batch << " in " << (elapsed.count() * 1e-9) << "s\n", exit(0);
}