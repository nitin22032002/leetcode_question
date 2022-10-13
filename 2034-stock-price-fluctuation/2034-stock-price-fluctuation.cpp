class StockPrice {
public:
    map<int,int> stock;
    multiset<int> prices;
    StockPrice() {
        
    }
    
    void update(int timestamp, int price) {
        if(stock.find(timestamp)!=stock.end()){
            prices.erase(prices.find(stock[timestamp]));   
        }
        stock[timestamp]=price;
        prices.insert(price);
    }
    
    int current() {
        auto it=--stock.end();
        return (*it).second;
    }
    
    int maximum() {
        auto it=--prices.end();
        return (*it);
    }
    
    int minimum() {
        return (*prices.begin());
    }
};

/**
 * Your StockPrice object will be instantiated and called as such:
 * StockPrice* obj = new StockPrice();
 * obj->update(timestamp,price);
 * int param_2 = obj->current();
 * int param_3 = obj->maximum();
 * int param_4 = obj->minimum();
 */