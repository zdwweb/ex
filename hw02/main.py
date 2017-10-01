def research(list_,target):
    low,high=0,len(list_)-1
    while(low<=high):
        mid=(low+high)//2
        if(list_[mid]==target):
            return mid
            break
        if(target<list_[mid]):
            high=mid-1
        if(target>list_[mid]):
            low=mid+1
data_lst=[1,2,3,4,5,6]
target=int(input())
position=research(data_lst,target)
print("元素{0}处于{1}位置".format(target,position))

