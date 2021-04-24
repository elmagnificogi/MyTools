function simulation
s1=cputime;
alpha=400000;
num=xlsread('Book1.xlsx',1);
cx=num(:,1)';
cy=num(:,2)';
sigma=num(:,3)';
type=num(:,4);
map_s=xlsread('Book1.xlsx',2);
map=create_map(map_s,cx,cy,type);
image=map.*20;
%image=zeros(map_s,map_s);
x=cx(end-1);
y=cy(end-1);
image=draw(image,cx(end),cy(end),2);
%image2=draw(image,cx(end),cy(end),2);
cnt=0;
x1=x;
y1=y;
[m n]=size(cx);
A=[x y];
j=1;
while( abs(x-cx(end)) > 5 || abs(y-cy(end)) > 5 )
    
%     for j=1:(n-2)
%         d=sqrt((x-cx(j))^2 + (y-cy(j))^2);
%          if(d >= 75)
%              sigma(j) = 75;
%          else
%             if(d<=30)
%                 sigma(j) = 30;
%             else
%                 sigma(j)= d;
%             end
%          end
%     end
%     map=create_map(map_s,sigma,cx,cy,type);
  %  image=map;
    image=draw(image,x,y,3);
    imshow(image);
    if(abs(x - x1)<=1 && abs(y - y1)<=1)
        cnt=cnt+1;
    else
        cnt = 0;
    end
%    if(cnt>20)
%        map(:,:,1)=map(:,:,1)+field(x1,y1,50,map_s,3);
%          if(j>6)
%             x=A(j-5,1);
%             y=A(j-5,2);
%             display(j);
%             A=A(1:1:16 , 1:1:1);
%             j=j-5;
%          else
%             x=A(1,1);
%             y=A(1,2);
%             A=[x y];
%             j=1;
%        %  end    
%          cnt=0;
%      end
     if(cnt>20)
        m =1000000;
        for i = -5:5
            for j = -5:5
                if(i~=0 || j~=0)
                    if(map(x+i,y+j,1)-map(x,y,1) <= m )
                        m = map(x+i,y+j,1)-map(x,y,1);
                        temp0=x+i;
                        temp1=y+j;
                    end
                end
            end
        end
        x = round(temp0);
        y = round(temp1);
        cnt = 0;
        continue;
    end
    x1=x;
    y1=y;
    temp0=x-alpha*(map(x+3,y,1)-map(x,y,1));
    temp1=y-alpha*(map(x,y+3,1)-map(x,y,1));
    x = round(temp0);
    y = round(temp1);
    A=[A; x y];
    j=j+1;
end
map=create_map(map_s,cx(1:1:end-2),cy(1:1:end-2),type);
image=map.*20;
imshow(image);
filter_waypoint(A,map);
end
function image=draw(img,x,y,n)
image=img;
for i=x:(x+5)
    for j=y:(y+5)
        image(i,j,n)=255;
    end
end
end
function filter_waypoint(A,map)
[m, n]=size(A);
flag=1;
while(flag)
    flag=0;
for i=1:m-2
    mid=[round((A(i,1)+A(i+2,1))/2), round((A(i,2)+A(i+2,2))/2)];
    if(map(A(i+1,1),A(i+1,2),1) >= map(mid(1),mid(2),1))
        A(i+1,1)=mid(1);
        A(i+1,2)=mid(2);
        flag=1;
    end
end
image=map.*20;
for i=1:m
    image=draw(image,A(i,1),A(i,2),2);
end
imshow(image);
% delay(1000);
end
s2=cputime;
display(s2-s1);
end
