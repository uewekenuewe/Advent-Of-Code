// author: Uwe Schmidt
// created: 2023-09-30 10:51:49.188933
#include <iostream>
using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define ll long long

const char *alphabet = "abcdefghijklmnopqrstuvwxyz";


int main() {
	string s;
	cin >> s;
	ll ans1 = 0;
	ll ans2 = 0;
	for(int i = 0; i < s.size(); i++){
		if(s[i] == '(')
			ans1++;
		else 
			ans1--;
		if(ans1 == -1 && ans2 == 0)
			ans2 = i;
	}

	cout << "ans1: " << ans1 << endl ;
	cout << "ans2: " << ans2 << endl ;

}
