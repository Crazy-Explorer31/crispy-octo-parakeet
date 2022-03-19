#include <iostream>
#include <cmath>
using namespace std;
bool is_simple(int alpha) {
	bool flag = true;
	for(int i = 2; i < sqrt(alpha) + 1; i++) {
		if (alpha % i == 0) {
			flag = false;
			break;
		}
	}
	return flag;
}
int main() {
	int alpha;
	cin>>alpha;
	if (is_simple(alpha)) {
		cout<<"Simple";
	}
	else {
		cout<<"Not simple";
	}
	return 0;
}