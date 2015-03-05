#include<iostream>
#include<cstring>

using namespace std;

const unsigned MAX_N = 2000;

void solve(int n, const char *original_ptr, char *new_ptr)
{
    char reverse_line[MAX_N + 1] = {0};
    for (int i = 0; i < n; ++i) {
        reverse_line[i] = original_ptr[n - 1 - i];
    }

    char *reverse_ptr = reverse_line;
    while (0 < n) {
        int cmp = strcmp(original_ptr, reverse_ptr);
        if (cmp < 0) {
            *new_ptr = *original_ptr;
            ++original_ptr;
        } else {
            *new_ptr = *reverse_ptr;
            ++reverse_ptr;
        }
        --n;
        ++new_ptr;
    }
}

int main()
{
    int n;
    char cow_line[MAX_N + 1] = {0};

    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> cow_line[i];
    }

    char new_line[MAX_N + 1] = {0};
    solve(n, cow_line, new_line);
    cout << new_line << endl;

    return 0;
}
