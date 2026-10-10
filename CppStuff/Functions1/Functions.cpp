#include <iostream>
using namespace std;
string show_commands_command = "?";
string end_program_command = "end";
string wonderer_1_2_3_command = "wonderer";
void commands(){
    cout<<show_commands_command<<" - Shows usable commands"<<endl;
    cout<<end_program_command<<" - Ends program"<<endl;
    cout<<wonderer_1_2_3_command<<" - Runs wonderer program"<<endl;
}
void wonderer_1_2_3(){
    cout<<"The wonderer simulates a sprite randomly wondering in a set number of dimensions and tests how many times he returns to where he started (home)";
    cout<<"How many dimensions should he wonder? ";
    int dimensions;
    cin>>dimensions;
    cout<<"For how many steps should the simulation run? ";
    int steps;
    cin>>steps;
    cout<<"Write every step (1 = yes, 0 = no)? ";
    int write_every_step;
    cin>>write_every_step;
    int step;
    srand(time(0));
    if(dimensions == 1){
        int x = 0;
        if(write_every_step == 1){
            for(step = 1; step <= steps; step++){
                x += (rand() % 2) - 1;
                cout<<"Step: "<<step<<", x position: "<<x<<endl;
            }
        }
        
    }
}
int main(){
    string response = "a";
    while(response != end_program_command){
        cin>>response;
        cout<<response<<endl;
        if(response == show_commands_command){
            commands();
        }
        else if (response == wonderer_1_2_3_command)
        {
            wonderer_1_2_3();
        }
        
    }
    return 0;
}
