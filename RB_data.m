clc;clear
fid=fopen('text.txt');
s=textscan(fid,'%s');
fclose(fid);
s=s{1};
b={'seconds'};
loc=find(strcmp(s,b)==1);
loc=loc-1;
times=zeros(length(loc),1);
for i=1:length(loc)
times(i)=str2double(s{loc(i),1});
end
times