#include <bits/stdc++.h>
using namespace std;

int num[10];
int main(void) {
	int a, b, c;
	cin >> a >> b >> c;
	int z = a * b * c;

	while (z > 0) {
		num[z % 10]++;
		z = z / 10;
	}
	for (int i = 0; i < 10; i++) {
		cout << num[i] << "\n";
	}

}
