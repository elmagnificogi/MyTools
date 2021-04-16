// ConsoleApplication1.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <fstream>
#include <vector>
#include <string>
#include "Vector3.h"

using namespace std;
using namespace RVO;

#define _for(i,a,b) for(LONGLONG i = (a); i<(b); i++)
#define _rep(i,a,b) for(LONGLONG i = (a); i<=(b); i++)

const int maxi = 20;
const int maxn = maxi + 2;
const int INF = maxn + 10;
const LONGLONG maxsum = 1 << maxi;

// n 是顶点个数
// m 是边数,不重复边数
int n, m, G[maxn][maxn], d[maxsum], noedges[maxsum];

void split(const string & s, vector<string>&tokens, char delim = ' ')
{
    tokens.clear();
    auto string_find_first_not = [s, delim](size_t pos = 0) -> size_t {
        for (size_t i = pos; i < s.size(); i++) {
            if (s[i] != delim) return i;
        }
        return string::npos;
    };
    size_t lastPos = string_find_first_not(0);
    size_t pos = s.find(delim, lastPos);
    while (lastPos != string::npos) {
        tokens.emplace_back(s.substr(lastPos, pos - lastPos));
        lastPos = string_find_first_not(pos);
        pos = s.find(delim, lastPos);
    }
}

int main()
{
    //scanf_s("%d%d", &n, &m);
    //int u, v;
    //_for(i, 0, m) {
    //    scanf_s("%d%d", &u, &v);
    //    G[u][v] = G[v][u] = 1;
    //}
    //G[0][1] = G[1][0] = 1;

    ifstream input;
    vector<Vector3> sp;
    vector<Vector3> ep;
    //vector<Drone_base> ps;

    input.open("F:\\DmdPathFinding\\Dmd_pathfinding\\Dmd_pathfinding_test\\Resourse\\divider_test.txt");
    if (input.fail())
    {
        return 0;
        //Assert::Fail(L"data file cant open");
    }

    string data_str;
    getline(input, data_str);
    int num = 0;
    while (!data_str.empty())
    {
        vector<string> data;
        split(data_str, data, ' ');
        //Logger::WriteMessage(data_str.data());
        //Logger::WriteMessage(data[0].data());

        Vector3 s(stod(data[0]), stod(data[1]), stod(data[2]));
        sp.push_back(s);
        //Point e(stod(data[3]), stod(data[4]), stod(data[5]));
        //ep.push_back(e);
        getline(input, data_str);
        num++;
        if (num == 20)
            break;
    }

    n = sp.size();

    m = 0;
    for (int index = 0; index < sp.size(); index++)
    {
        for (int index1 = index; index1 < sp.size(); index1++)
        {
            double dis = (sp[index] - sp[index1]).length();
            if (dis < 3.5)
            {
                G[index][index1] = G[index1][index] = 1;
                m++;
            }
        }
    }

    // 先预处理出noedges
    _rep(S, 0, (1 << n) - 1) {
        noedges[S] = 1;
        _rep(i, 1, n)
            if (S & (1 << i))
                _rep(j, 1, n)
                if (i != j && G[i][j] && (S & (1 << j)))
                    noedges[S] = 0;
    }

    d[0] = 0;
    _for(S, 1, (1 << n)) {
        d[S] = INF;
        for (int S0 = S; S0; S0 = (S0 - 1) & S)
            if (noedges[S0]) d[S] = min(d[S], d[S - S0] + 1);  // 此处S-S0的操作，可以自己试一下，就是删去S中S0的部分
    }

    printf("%d\n", d[(1 << n) - 1]);
}

// 运行程序: Ctrl + F5 或调试 >“开始执行(不调试)”菜单https://github.com/massgravel/Microsoft-Activation-Scripts/releases
// 调试程序: F5 或调试 >“开始调试”菜单

// 入门使用技巧: 
//   1. 使用解决方案资源管理器窗口添加/管理文件
//   2. 使用团队资源管理器窗口连接到源代码管理
//   3. 使用输出窗口查看生成输出和其他消息
//   4. 使用错误列表窗口查看错误
//   5. 转到“项目”>“添加新项”以创建新的代码文件，或转到“项目”>“添加现有项”以将现有代码文件添加到项目
//   6. 将来，若要再次打开此项目，请转到“文件”>“打开”>“项目”并选择 .sln 文件
