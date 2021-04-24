function res=field(xc,yc,map_s,type)
res=zeros(map_s,map_s,1);
for x=1:map_s
    for y=1:map_s
       if(x>0 && y>0 && x<=map_s && y<=map_s)
            if(type==2)
                d = sqrt((x-xc).^2 + (y-yc).^2);
                t = 10;
                if(d>t)
                    res(x,y) = t*d-0.5*(t).^2;
                else
                    res(x,y) = 0.5*(d).^2;
                end
                res(x,y) = 0.000001*res(x,y);
                %res(x,y) = -( 3*min(sqrt(1/((x-xc).^2 + (y-yc).^2)) , *** ) );
                %amplitude = -(amplitude);
                 %end
            else
                if(type == 3)
                     %if(x>0 && y>0 && x<=map_s && y<=map_s)
%                      exponent = ((x-xc).^2 + (y-yc).^2)./(2*sigma^2);
%                      amplitude = 1 / (sigma * sqrt(2*pi));
%                      res(x,y)= 1.5*amplitude  * exp(-exponent); 
                     a = 5;
                     b = 5;
                     thr= 5;
                     c = ( (x-xc).^2 )/a.^2 +( (y-yc).^2 )/b.^2 ;
                     c = sqrt(c);
                     if(c < 1)
                         res(x,y) = min( (1 - 1/c).^2 ,thr);
                         res(x,y) =res(x,y)*0.001;
                     else
                         res(x,y)=0;
                     end
                     
                else
                    if(type==1)
                      res(x,y)=0;
                    else
                        a = 200;
                        b = 50;
                        thr= 5;
                        c = ( (x-xc).^2 )/a.^2 +( (y-yc).^2 )/b.^2 ;
                        c = sqrt(c);
                        if(c < 1)
                            res(x,y) = min( (1 - 1/c).^2 ,thr);
                            res(x,y) =res(x,y)*0.001;
                        else
                            res(x,y)=0;
                        end
                    end
                end
            end
        end
    end
end
