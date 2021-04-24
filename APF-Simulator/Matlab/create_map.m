function map=create_map(map_s,x,y,type)
%x=num(:,1)';
%y=num(:,2)';
%sigma=num(:,3)';
%type=num(:,4);
%map_s=xlsread('Book1.xlsx',2);
[~,n]=size(x);
map=zeros(map_s,map_s,3);
for i=1:n
%     map(:,:,1)=map(:,:,1)+gauss(x(i),y(i),sigma(i),map_s,type(i));
    if(type == 0)
        d=sqrt( ((x(i)-x(end)).^2 + (y(i)-y(end)).^2) );
        map(:,:,1)=map(:,:,1)+field(x(i),y(i),map_s,type(i));
    else
        map(:,:,1)=map(:,:,1)+field(x(i),y(i),map_s,type(i));
    end
end
