#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main(){
    string answer1 = "";
    string answer2;
    while(answer1 != "a"){
        cout<<"Possible actions:"<<endl;
        cout<<"a)   STOP"<<endl;
        cout<<"b)   Count all words in answer list"<<endl;
        cout<<"What do you want to do? ";
        cin>>answer1;
        if(answer1 == "b"){
            ofstream AnswerList("wordle-answers-alphabetical");
            if(AnswerList.is_open()){
                int LineCount = 0;
                string line;
                while(getline(AnswerList, line)){
                    LineCount += 1;
                }
                AnswerList.close();
                cout<<"There are "<<LineCount<<" words in answer list."
            }
        }
    }
    return 0;
}