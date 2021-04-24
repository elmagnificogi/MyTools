//
//  Field.cpp
//  
//
//  Created by muskaan on 14/05/17.
//
//


//#include <stdio.h>
//#include <math.h>
//#include <iostream>
//#include <opencv2/highgui/highgui.hpp>
//#include <opencv2/imgproc/imgproc.hpp>
//#include <opencv2/core/core.hpp>

using namespace cv;
using namespace std;

double** att_field(int px,int py,int mx,int my){

    double t,d;
        double **res = (double**)calloc(mx, sizeof(double*));
    for(int i=0; i<mx; i++)
        res[i] = (double*)calloc(my, sizeof(double));
    
    for(int x=0; x<mx; x++){
        for(int y=0; y<my; y++){
            
            t = 20;
            d = sqrt(pow((x-px),2) + pow((y-py),2));
            
            if(d > t)
                res[x][y] = t*d - 0.5*pow(t, 2);
            else
                res[x][y] = 0.5*pow(d, 2);
            
            res[x][y] = 0.000001*res[x][y];
            
        }
    }

    return res;
    
}




double** rep_field(int px,int py,int sx,int sy,int mx,int my){

    double thr,d;
    
    double **res = (double**)calloc(mx, sizeof(double*));
    for(int i=0; i<mx; i++)
        res[i] = (double*)calloc(my, sizeof(double));

    for(int x=0; x<mx; x++){
        for(int y=0; y<my; y++){

            thr = 5;
            d = sqrt(pow((x-px), 2)/pow(sx, 2) + pow((y-py), 2)/pow(sy, 2));
            
            if(d < 1 && d != 0){
            
                if(pow((1 - 1/d), 2) < thr){
                    res[x][y] = pow((1 - 1/d), 2);
                }
                else
                    res[x][y] = thr;
                
                res[x][y] = 0.001*res[x][y];
                

            }
            else
                res[x][y] = 0;
            
        }
    }
    


    return res;
    
}




double** guassian(int px,int py,int sx,int sy,int mx,int my){

    double d, pi = 3.14159,amp, e = 2.71828;
    double **res = (double**)calloc(mx, sizeof(double*));
    for(int i=0; i<mx; i++)
        res[i] = (double*)calloc(my, sizeof(double));
   
    for(int x=0; x<mx; x++){
        for(int y=0; y<my; y++){

           d = sqrt(pow((x-px), 2)/pow(sx, 2) + pow((y-py), 2)/pow(sy, 2));
            d *= -0.5;
            amp = 1/(2*pi*sx*sy);
            res[x][y] = 200*amp*pow(e, d);
            
        }
    }
    
    return res;
}




