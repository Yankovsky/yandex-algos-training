#include <iostream>
#include <vector>
#include <algorithm>
#include <tuple>


using namespace std;

enum class PointType {
    START = -1,
    CONTROL = 0,
    FINISH = 1
};

int main() {
    int n, m;
    cin >> n >> m;
    vector<std::tuple<int, PointType, int>> points;
    points.reserve(2 * n + m);

    for (int i = 0; i < n; ++i) {
        int pos1, pos2;
        cin >> pos1 >> pos2;
        int startPos = min(pos1, pos2);
        int finishPos = max(pos1, pos2);
        points.emplace_back(startPos, PointType::START, 0);
        points.emplace_back(finishPos, PointType::FINISH, 0);
    }
    for (int i = 0; i < m; ++i) {
        int point;
        cin >> point;
        points.emplace_back(point, PointType::CONTROL, i);
    }

    sort(points.begin(), points.end());

    int segmentsCount = 0;
    vector<int> answer;
    answer.resize(m);

    for (const auto&[point, pointType, idx] : points) {
        if (pointType == PointType::CONTROL) {
            answer[idx] = segmentsCount;
        } else if (pointType == PointType::START) {
            ++segmentsCount;
        } else {
            --segmentsCount;
        }
    }

    for (auto point : answer) {
        cout << point << ' ';
    }

    return 0;
}