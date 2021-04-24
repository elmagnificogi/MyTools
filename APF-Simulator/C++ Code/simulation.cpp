//
//  simulation.cpp
//  
//
//  Created by muskaan on 15/05/17.
//
//

#include <stdio.h>
#include <iostream>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/core/core.hpp>
#include <vector>
#include "Field.cpp"
#include <stdlib.h>
#include <math.h>
#include "create_map.cpp"
#include "Filter_waypoint.cpp"

using namespace cv;
using namespace std;


void simulation(){

    vector < vector<int> > points;
    vector <int> coordinates(2);
    int alpha = 90000;
    int X[] = {200, 55, 400};
    int Y[] = {200, 62, 350 };
    int SIGMA_X[] = {30, 100, 100 };
    int SIGMA_Y[] = {30, 100, 100 };
    int TYPE[] = {0, 1, 2};
    int map_sx = 500;
    int map_sy = 500;
    
    int m = 3;
    namedWindow("path", WINDOW_NORMAL);
    int x, y, x1, y1, temp0, temp1, Dx ,Dy;
    
    double **Map = create_map(map_sx, map_sy ,X, Y,SIGMA_X,SIGMA_Y,TYPE);
    Mat img(map_sx, map_sy, CV_8UC3, Scalar(0,0,0));
    imshow("path", img);
    
    for(int i=0; i<=m; i++){
    
        if(TYPE[i] == 2){
           
             Dx = X[i];
             Dy = Y[i];
        
        }
        if(TYPE[i] == 1){
        
            x = x1 = X[i];
            y = y1 = Y[i];
            
        }
        
    }
    img = draw(img, Dx, Dy, 1, 0);
    imshow("path", img);
    coordinates[0] = x;
    coordinates[1] = y;
    points.push_back(coordinates);
       int count = 0;
    
    while( abs(x-Dx) > 5 or abs(y-Dy) > 5 ){
    
        img = draw(img, x, y, 0, 0);
        imshow("path",img);
        waitKey(10);
    
        //checking if bot is stationary for long
        if(abs(x - x1)<1 and abs(y - y1) < 1)
            count += 1;
        else
            count = 0;
        
        //to avoid local minima
        
        if(count > 10){
        
            int m = 100000;
            for(int i=-10; i<=11; i++){
                for(int j=-10; j<=11; j++){
                
                    if(i != 0 || j != 0 ){
                    
                        if(Map[x+i][y+j] - Map[x][y] < m){
                        
                            m = Map[x+i][y+j] - Map[x][y];
                            temp0 = x - 1.5*alpha*m;
                            temp1 = y - 1.5*alpha*m;
                        }
                    }
                }
            }
        
            x = temp0;
            y = temp1;
            count = 0;
            coordinates[0] = x;
            coordinates[1] = y;
            points.push_back(coordinates);
                        continue;
        
        }
        
        x1 = x;
        y1 = y;
        temp0 = x - alpha*(Map[x+3][y] - Map[x][y]);
        temp1 = y - alpha*(Map[x][y+3] - Map[x][y]);
        x = temp0;
        y = temp1;
        coordinates[0] = x;
        coordinates[1] = y;
        points.push_back(coordinates);
    }
    waitKey(1000);
    Map = filter_map(map_sx, map_sy, X, Y, SIGMA_X, SIGMA_Y, TYPE);
    Filter_waypoint(points, Map, map_sx, map_sy);
    return;
    
}



int main(){
    simulation();
    }
