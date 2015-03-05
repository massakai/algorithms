#include<iostream>
#include<cstring>

using namespace std;

const unsigned MAX_N = 2000;

void solve(int n, const char *original_ptr)
{
    char new_line[81] = {0};
    char reverse_line[MAX_N + 1] = {0};
    for (int i = 0; i < n; ++i) {
        reverse_line[i] = original_ptr[n - 1 - i];
    }

    int i = 0;
    char *reverse_ptr = reverse_line;
    for (; 0 < n; ++i, --n) {
        if (i == 80) {
            cout << new_line << endl;
            i = 0;
        }
        int cmp = strcmp(original_ptr, reverse_ptr);
        if (cmp < 0) {
            new_line[i] = *original_ptr;
            ++original_ptr;
        } else {
            new_line[i] = *reverse_ptr;
            ++reverse_ptr;
        }
    }
    new_line[i] = '\0';
    cout << new_line << endl;
}

int main()
{
    int n;
    char cow_line[MAX_N + 1] = {0};

    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> cow_line[i];
    }

    solve(n, cow_line);

    return 0;
}
