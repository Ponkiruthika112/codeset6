def binary(arr,l,r,k):
	mid=(l+r)//2
	while l<=r:
		if arr[mid]==k:
			return 1
		elif arr[mid]>k:
			return binary(arr,l,mid-1,k)
		else:
			return binary(arr,mid+1,r,k)
	
	return -1
n,k=map(int,input().split())
arr=list(map(int,input().split()))
j=binary(arr,0,len(arr)-1,k)
if j!=-1:
	print("Yes")
else:
	print("No")
#key present or not
