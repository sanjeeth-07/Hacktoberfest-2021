#include<stdio.h>
int main()
{
	int number=0;
	int count = 0;
	printf("Enter a integer : ");
	scanf("%d",&number);
	while(number>=1)
	{
		number/=10;
		count++;
	}
	printf("Number of digits : %d", count);
	return 0;
}
