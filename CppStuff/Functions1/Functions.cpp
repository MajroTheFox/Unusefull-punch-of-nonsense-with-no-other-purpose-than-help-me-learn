#include <iostream>
using namespace std;
//Here are the commands
string show_commands_command = "?";
string end_program_command = "end";
string wonderer_1_2_3_a_command = "wonderer_a";
string wonderer_1_2_3_b_command = "wonderer_b";
string introduction = "introduction";
void commands(){
    //Don't forget to add any new command here!
    cout<<show_commands_command<<" - Shows usable commands"<<endl;
    cout<<end_program_command<<" - Ends program"<<endl;
    cout<<wonderer_1_2_3_a_command<<" - Runs wonderer program a"<<endl;
    cout<<wonderer_1_2_3_b_command<<" - Runs wonderer program b"<<endl;
    cout<<introduction<<" - Introduces the program"<<endl;
}
void wonderer_1_2_3_a(){
    cout<<"The wonderer a simulates a sprite randomly wondering in a set number of dimensions and tests how many times he returns to where he started (home). It moves in every available dimension by either -1 or 1."<<endl;
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
    int x = 0;
    int y = 0;
    int z = 0;
    int max_x = 0;
    int max_y = 0;
    int max_z = 0;
    int home_visits = 0;
    srand(time(0));
    if(dimensions == 1){
        if(write_every_step == 1){
            for(step = 1; step <= steps; step++){
                x += ((rand() % 2) - 0.5)*2;
                cout<<"Step: "<<step<<", x position: "<<x<<endl;
                if(x == 0){
                    cout<<"Sprite visited home at step "<<step<<endl;
                    home_visits++;
                }
                if(abs(x) > max_x){
                    max_x = abs(x);
                }
            }
        }
        else if(write_every_step == 0){
            for(step = 1; step <= steps; step++){
                x += ((rand() % 2) - 0.5)*2;
                if(x == 0){
                    cout<<"Sprite visited home at step "<<step<<endl;
                    home_visits++;
                }
                if(abs(x) > max_x){
                    max_x = abs(x);
                }
            }
        }
        else{
            cout<<"You were supossed to input 1 or 0, you silly!"<<endl;
        }
        
    }
    else if(dimensions == 2){
        if(write_every_step == 1){
            for(step = 1; step <= steps; step++){
                x += ((rand() % 2) - 0.5)*2;
                y += ((rand() % 2) - 0.5)*2;
                cout<<"Step: "<<step<<", x position: "<<x<<", y position: "<<y<<endl;
                if(x == 0 && y == 0){
                    cout<<"Sprite visited home at step "<<step<<endl;
                    home_visits++;
                }
                if(abs(x) > max_x){
                    max_x = abs(x);
                }
                if(abs(y) > max_y){
                    max_y = abs(y);
                }
            }
        }
        else if(write_every_step == 0){
            for(step = 1; step <= steps; step++){
                x += ((rand() % 2) - 0.5)*2;
                y += ((rand() % 2) - 0.5)*2;
                if(x == 0 && y == 0){
                    cout<<"Sprite visited home at step "<<step<<endl;
                    home_visits++;
                }
                if(abs(x) > max_x){
                    max_x = abs(x);
                }
                if(abs(y) > max_y){
                    max_y = abs(y);
                }
            }
        }
        else{
            cout<<"You were supossed to input 1 or 0, you silly!"<<endl;
        }
        
    }
    else if(dimensions == 3){
        if(write_every_step == 1){
            for(step = 1; step <= steps; step++){
                x += ((rand() % 2) - 0.5)*2;
                y += ((rand() % 2) - 0.5)*2;
                z += ((rand() % 2) - 0.5)*2;
                cout<<"Step: "<<step<<", x position: "<<x<<", y position: "<<y<<", z position: "<<z<<endl;
                if(x == 0 && y == 0 && z == 0){
                    cout<<"Sprite visited home at step "<<step<<endl;
                    home_visits++;
                }
                if(abs(x) > max_x){
                    max_x = abs(x);
                }
                if(abs(y) > max_y){
                    max_y = abs(y);
                }
                if(z > max_z){
                    max_z = abs(z);
                }
            }
        }
        else if(write_every_step == 0){
            for(step = 1; step <= steps; step++){
                x += ((rand() % 2) - 0.5)*2;
                y += ((rand() % 2) - 0.5)*2;
                z += ((rand() % 2) - 0.5)*2;
                if(x == 0 && y == 0 && z == 0){
                    cout<<"Sprite visited home at step "<<step<<endl;
                    home_visits++;
                }
                if(abs(x) > max_x){
                    max_x = abs(x);
                }
                if(abs(y) > max_y){
                    max_y = abs(y);
                }
                if(z > max_z){
                    max_z = abs(z);
                }
            }
        }
        else{
            cout<<"You were supossed to input 1 or 0, you silly!"<<endl;
        }
        
    }
    cout<<"Sprite visited home "<<home_visits<<" times."<<endl;
    cout<<"Highest |x| was "<<max_x<<endl<<"Highest |y| was "<<max_y<<endl<<"Highest |z| was "<<max_z<<endl;
}
void wonderer_1_2_3_b(){
    cout<<"The wonderer b simulates a sprite randomly wondering in a set number of dimensions and tests how many times he returns to where he started (home). It moves in one of the available dimension by either -1 or 1."<<endl;
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
    int coin;
    int x = 0;
    int y = 0;
    int z = 0;
    int max_x = 0;
    int max_y = 0;
    int max_z = 0;
    int home_visits = 0;
    srand(time(0));
    if(dimensions == 1){
        if(write_every_step == 1){
            for(step = 1; step <= steps; step++){
                x += ((rand() % 2) - 0.5)*2;
                cout<<"Step: "<<step<<", x position: "<<x<<endl;
                if(x == 0){
                    cout<<"Sprite visited home at step "<<step<<endl;
                    home_visits++;
                }
                if(abs(x) > max_x){
                    max_x = abs(x);
                }
            }
        }
        else if(write_every_step == 0){
            for(step = 1; step <= steps; step++){
                x += ((rand() % 2) - 0.5)*2;
                if(x == 0){
                    cout<<"Sprite visited home at step "<<step<<endl;
                    home_visits++;
                }
                if(abs(x) > max_x){
                    max_x = abs(x);
                }
            }
        }
        else{
            cout<<"You were supossed to input 1 or 0, you silly!"<<endl;
        }
        
    }
    else if(dimensions == 2){
        if(write_every_step == 1){
            for(step = 1; step <= steps; step++){
                coin = rand() % 4;
                if(coin == 0){
                    x++;
                }
                if(coin == 1){
                    x--;
                }
                if(coin == 2){
                    y++;
                }
                if(coin == 3){
                    y--;
                }
                cout<<"Step: "<<step<<", x position: "<<x<<", y position: "<<y<<endl;
                if(x == 0 && y == 0){
                    cout<<"Sprite visited home at step "<<step<<endl;
                    home_visits++;
                }
                if(abs(x) > max_x){
                    max_x = abs(x);
                }
                if(abs(y) > max_y){
                    max_y = abs(y);
                }
            }
        }
        else if(write_every_step == 0){
            for(step = 1; step <= steps; step++){
                coin = rand() % 4;
                if(coin == 0){
                    x++;
                }
                if(coin == 1){
                    x--;
                }
                if(coin == 2){
                    y++;
                }
                if(coin == 3){
                    y--;
                }
                if(x == 0 && y == 0){
                    cout<<"Sprite visited home at step "<<step<<endl;
                    home_visits++;
                }
                if(abs(x) > max_x){
                    max_x = abs(x);
                }
                if(abs(y) > max_y){
                    max_y = abs(y);
                }
            }
        }
        else{
            cout<<"You were supossed to input 1 or 0, you silly!"<<endl;
        }
        
    }
    else if(dimensions == 3){
        if(write_every_step == 1){
            for(step = 1; step <= steps; step++){
                coin = rand() % 6;
                if(coin == 0){
                    x++;
                }
                if(coin == 1){
                    x--;
                }
                if(coin == 2){
                    y++;
                }
                if(coin == 3){
                    y--;
                }
                if(coin == 4){
                    z++;
                }
                if(coin == 5){
                    z--;
                }
                cout<<"Step: "<<step<<", x position: "<<x<<", y position: "<<y<<", z position: "<<z<<endl;
                if(x == 0 && y == 0 && z == 0){
                    cout<<"Sprite visited home at step "<<step<<endl;
                    home_visits++;
                }
                if(abs(x) > max_x){
                    max_x = abs(x);
                }
                if(abs(y) > max_y){
                    max_y = abs(y);
                }
                if(z > max_z){
                    max_z = abs(z);
                }
            }
        }
        else if(write_every_step == 0){
            for(step = 1; step <= steps; step++){
                coin = rand() % 6;
                if(coin == 0){
                    x++;
                }
                if(coin == 1){
                    x--;
                }
                if(coin == 2){
                    y++;
                }
                if(coin == 3){
                    y--;
                }
                if(coin == 4){
                    z++;
                }
                if(coin == 5){
                    z--;
                }
                if(x == 0 && y == 0 && z == 0){
                    cout<<"Sprite visited home at step "<<step<<endl;
                    home_visits++;
                }
                if(abs(x) > max_x){
                    max_x = abs(x);
                }
                if(abs(y) > max_y){
                    max_y = abs(y);
                }
                if(z > max_z){
                    max_z = abs(z);
                }
            }
        }
        else{
            cout<<"You were supossed to input 1 or 0, you silly!"<<endl;
        }
        
    }
    cout<<"Sprite visited home "<<home_visits<<" times."<<endl;
    cout<<"Highest |x| was "<<max_x<<endl<<"Highest |y| was "<<max_y<<endl<<"Highest |z| was "<<max_z<<endl;
}
int main(){
    string response = introduction;
    while(response != end_program_command){
        if(response == show_commands_command){
            commands();
        }
        else if(response == wonderer_1_2_3_a_command){
            wonderer_1_2_3_a();
        }
        else if(response == wonderer_1_2_3_b_command){
            wonderer_1_2_3_b();
        }
        else if (response == introduction){
            cout<<"Greetings, user! This is a program, that repeats itself. It is basically a terminal. Enter "<<show_commands_command<<" to view all commands."<<endl;
        }
        else{
            cout<<"That command does not exist. To view the full list of commands, enter "<<show_commands_command<<endl;
        }
        cin>>response;
    }
    return 0;
}
