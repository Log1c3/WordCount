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
			ch = fgetc(fp);//��ǰfp��ָ���ַ�����ch
			cnt++;//�ַ�����++
		}
		printf("�ַ�����%d\n",--cnt);
	}
	else if (strcmp(argv[1],"-w") == 0  || strcmp(argv[1],"-W") == 0)
	{
		while(!feof(fp))
		{
			ch = fgetc(fp);//��ǰfp��ָ���ַ�����ch
			if ( ch == ',' || ch == ' ' )//�ж����������fp��ָ���ַ�Ϊ���źͿո�
				cnt++;//���ʼ���++
		}
		if(ch == ',' || ch == ' ')
		//���������ַ����꣬chΪ�ı����һ���ַ������ch���Ƕ��Ż��߿ո�
		//��˵����һ�����Ż�ո�֮����һ�����ʣ����Ե�����++
			cnt++;
		printf("��������%d\n",cnt);

	}
	return 0;
}