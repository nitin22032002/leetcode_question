class Solution {
public:
    int poorPigs(int buckets, int poisonTime, int totalTime) {
        int base = totalTime / poisonTime +1;
        for(int i=0; i<10; ++i){
            if(powl(base, i) >= buckets) return i;
        }
        return 10;
    }
};