#include <iostream>
#include <set>

using namespace std;


int manhattan_distance(pair<int, int> pos_a, pair<int, int> pos_b) {
    return abs(pos_a.first - pos_b.first) + abs(pos_a.second - pos_b.second);
}

int main() {
    int t, d, n;
    cin >> t >> d >> n;

    set<pair<int, int>> previous_positions;
    previous_positions.emplace(pair<int, int>{0, 0});

    pair<int, int> navigator_position;
    for (int i = 0; i < n; i++) {
        cin >> navigator_position.first >> navigator_position.second;

        set<pair<int, int>> possible_positions;

        for (const auto &previous_position: previous_positions) {
            int distance = manhattan_distance(navigator_position, previous_position);
            if (distance <= d + t) {
                int min_x_pos = max(navigator_position.first - d, previous_position.first - t);
                int max_x_pos = min(navigator_position.first + d, previous_position.first + t);
                for (int x = min_x_pos; x < max_x_pos + 1; ++x) {
                    int leftover_a = d - abs(navigator_position.first - x);
                    int leftover_b = t - abs(previous_position.first - x);
                    int min_y_pos = max(navigator_position.second - leftover_a, previous_position.second - leftover_b);
                    int max_y_pos = min(navigator_position.second + leftover_a, previous_position.second + leftover_b);
                    for (int y = min_y_pos; y < max_y_pos + 1; ++y) {
                        possible_positions.emplace(x, y);
                    }
                }
            }
        }
        previous_positions = possible_positions;
    }

    cout << size(previous_positions);
    for (const auto &elem: previous_positions) {
        cout << '\n' << elem.first << " " << elem.second;
    }

    return EXIT_SUCCESS;
}
