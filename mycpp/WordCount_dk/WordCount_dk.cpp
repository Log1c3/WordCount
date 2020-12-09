#include<stdio.h>
#include<string.h>
int main(int argc, char *argv[])
{
	int cnt=0;
	int ch;
	char filename[80];
	FILE *fp;
	strcpy(filename,argv[2]);
	fp = fopen(filename,"r");
	cnt = 0;
	if (strcmp(argv[1],"-c") == 0 || strcmp(argv[1],"-C") == 0)
	{
		while(!feof(fp))
		{
			ch = fgetc(fp);//当前fp所指的字符赋给ch
			cnt++;//字符计数++
		}
		printf("字符数：%d\n",--cnt);
	}
	else if (strcmp(argv[1],"-w") == 0  || strcmp(argv[1],"-W") == 0)
	{
		while(!feof(fp))
		{
			ch = fgetc(fp);//当前fp所指的字符赋给ch
			if ( ch == ',' || ch == ' ' )//判断条件：如果fp所指的字符为逗号和空格
				cnt++;//单词计数++
		}
		if(ch == ',' || ch == ' ')
		//上面所有字符读完，ch为文本最后一个字符，如果ch不是逗号或者空格，
		//就说明上一个逗号或空格之后有一个单词，所以单词数++
			cnt++;
		printf("单词数：%d\n",cnt);

	}
	return 0;
}