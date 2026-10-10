#include<iostream>
#include<fstream>
using namespace std;
int main(){
    int square_size = 8;
    ofstream MyFile1("MyFile1.txt");
    srand(time(0));
    int i, j;
    for(i=0;i<square_size;i++){
        for(j=0;j<square_size;j++){
            MyFile1<<rand() % 10<<", ";
        }
        MyFile1<<endl;
    }
    MyFile1.close();
    ofstream MyFile2;
    MyFile2.open("DeepInFile.txt");
    MyFile2.close();
    return 0;
}