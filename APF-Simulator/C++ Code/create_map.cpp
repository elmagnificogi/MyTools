//
//  create_map.cpp
//  
//
//  Created by muskaan on 15/05/17.
//
//

//#include <stdio.h>
//#include <iostream>
//#include <opencv2/highgui/highgui.hpp>
//#include <opencv2/imgproc/imgproc.hpp>
//#include <opencv2/core/core.hpp>
//#include "Field.cpp"
//#include <stdlib.h>

using namespace cv;
using namespace std;


double** create_map(int mx,int my,int X[],int Y[],int SIGMA_X[],int SIGMA_Y[],int TYPE[]){

    
   
    double **res;
    double **map = (double**)calloc(mx, sizeof(double*));
    for(int i=0; i<mx; i++)
        map[i] = (double*)calloc(my, sizeof(double));

    int n = 3;
    
    for(int j=0; j<n; j++){
    
        if(TYPE[j] == 0){
            res = rep_field(X[j],Y[j],SIGMA_X[j],SIGMA_Y[j],mx,my);
            
            for(int x=0; x<mx; x++)
                for(int y=0; y<my; y++)
                    map[x][y] += res[x][y];
                    
        }else if(TYPE[j] == 2){
            res = att_field(X[j],Y[j],mx,my);
            for(int x=0; x<mx; x++)
                for(int y=0; y<my; y++)
                    map[x][y] += res[x][y];

        }
    }
    
    return map;
}



double** filter_map(int mx,int my,int X[],int Y[],int SIGMA_X[],int SIGMA_Y[],int TYPE[]){
  
    double **res;
    double **map = (double**)calloc(mx, sizeof(double*));
    for(int i=0; i<mx; i++)
        map[i] = (double*)calloc(my, sizeof(double));

    int n = 3;
    for(int j=0; j<n; j++){
    
        if(TYPE[j] == 0){
            res = rep_field(X[j],Y[j],SIGMA_X[j],SIGMA_Y[j],mx,my);
            for(int x=0; x<mx; x++)
                for(int y=0; y<my; y++)
                    map[x][y] += 2*res[x][y];

    
    
        }
    }

        return map;

}
