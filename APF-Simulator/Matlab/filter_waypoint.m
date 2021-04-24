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
image=map;
for i=1:m
    image=draw(image,A(i,1),A(i,2),2);
end
end
end