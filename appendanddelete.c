#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *AppendAndDelete(char *s, char *t, int k) {
    if (k >= strlen(s) + strlen(t)) {
        return "Yes";
    }

    int d = 0;
    while (d < strlen(s) && d < strlen(t) && s[d] == t[d]) {
        d++;
    }

    int min_ops = (strlen(s) - d) + (strlen(t) - d);

    if (min_ops == k) {
        return "Yes";
    } 
    else if (min_ops < k) {
        if ((k - min_ops) % 2 == 0) {
            return "Yes";
        } 
        else {
            return "No";
        }
    } 
    else {
        return "No";
    }
}

int main() {
    char s[100], t[100];
    int k;

    scanf("%s", s);
    scanf("%s", t);
    scanf("%d", &k);

    char *result = AppendAndDelete(s, t, k);
    printf("%s\n", result);

    return 0;
}
