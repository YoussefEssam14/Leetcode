#include <vector>
using namespace std;
class Solution {
public:
    int n , m;
    int similarColor;
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        similarColor = image[sr][sc];
        if(similarColor == color)return image;
        n = image.size();
        m = image[0].size();
        dfs(sr,sc,image,color);
        return image;
    }
private:
    inline bool inBoundaries(int row,int col){
        return row >=0 && row < n && col >=0  && col < m;
    }
    void dfs(int row,int col,vector<vector<int>>& image,int color){
        if(!inBoundaries(row,col) || image[row][col] != similarColor) return;
        // Flood fill
        image[row][col] = color;
        dfs(row,col-1,image,color);
        dfs(row,col+1,image,color);
        dfs(row-1,col,image,color);
        dfs(row+1,col,image,color);
    }
};