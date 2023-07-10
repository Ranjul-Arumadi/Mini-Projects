//tictactoe project
#include<stdio.h>
#include<conio.h>
#include<cstdlib>
#include<ctime>
#include<windows.h>
#include<iostream>
#include<dos.h>
using std::cout;
using std::cin;
int slot,current_player;
char current_marker;
char board[3][3]={{'1','2','3'},{'4','5','6'},{'7','8','9'}};
void drawboard()
{

    cout<<" -----------------\n";
    cout<<"|  "<<board[0][0]<<"  |  "<<  board[0][1]<<"  |  "<<board[0][2]<<"  |  \n";
    cout<<" ----------------- \n";
    cout<<"|  "<<board[1][0]<<"  |  "<<  board[1][1]<<"  |  "<<board[1][2]<<"  |  \n";
    cout<<" ----------------- \n";
    cout<<"|  "<<board[2][0]<<"  |  "<<  board[2][1]<<"  |  "<<board[2][2]<<"  |  \n";
    cout<<" -----------------  \n";


}


bool marker_placing(int slot)
{
    int row=0,col=0;
    row=(slot/3);
    if(slot%3==0)
    {
        col=2;
        row=row-1;
    }
    else
        {
            col=(slot%3)-1;
        }

   //placing marker
   if(board[row][col]!='x' && board[row][col]!='o' )
   {
       board[row][col]=current_marker;
       return true;
   }
   else
    return false;

}
int winner()
{
    for(int i=0;i<3;i++)
    {
        //row
        if(board[i][0]==board[i][1] && board[i][1]== board[i][2])
            return current_player;
        //column
        if(board[0][i]==board[1][i] && board[1][i]== board[2][i])
            return current_player;
    }
    //diagonals
    if(board[0][0]==board[1][1] && board[1][1]== board[2][2])
            return current_player;
    if(board[0][2]==board[1][1] && board[1][1]== board[2][0])
            return current_player;

     return 0;



}
void swap_swap()
{
    //marker swapping
    if(current_marker=='x')
        current_marker='o';
    else
        current_marker='x';
    //player swapping
    if(current_player==1)
            current_player=2;
    else
        current_player=1;
}
void game()
{

    int slot;

    drawboard();
    char marker_p1;
    current_player=1;
    a:
    cout<<"Player 1 enter your marker (x OR o)\n";
    cin>>marker_p1;
    if(marker_p1!='x' && marker_p1!='o')
    {
        cout<<"ERROR\n";
        goto a;
    }
    int winner_boy;
    current_marker=marker_p1;


    for(int i=0;i<=9;i++)
    {
        cout<<"Player "<<current_player<<"'s turn,enter slot value\n";
        cin>>slot;
        if(slot<1 || slot>9)
        {

            cout<<"WRONG INPUT\n";
            i--;
            continue;

        }

        if(!marker_placing(slot))
        {
            cout<<"slot occupied\n";
            i--;
            continue;

        }
        int winner_boy=winner();
        drawboard();
        if(winner_boy==1)
        {
            cout<<"*************Congo player 1****************\n";
            //Sleep(2);
            //delay(3000);
            exit(0);
            //break;
        }
        if(winner_boy==2)
        {
            cout<<"*************Congo player 2****************\n";
            exit(0);
            //break;

        }
        swap_swap();


    }
    if(winner_boy==0)
        {
            cout<<"TIE";
            exit(0);
        }

}
//-------------------AGAINST-------COMPUTER---------------------
void swap_computer()
{
    //marker swapping
    if(current_marker=='x')
        current_marker='o';
    else
        current_marker='x';
    //player swapping
    if(current_player==1)
            current_player=2;
    else
        current_player=1;
}
void computer()
{


    int slot;

    drawboard();
    char marker_p1;
    current_player=1;
    b:
    cout<<"Player 1 enter your marker (x OR o)\n";
    cin>>marker_p1;
    if(marker_p1!='x' && marker_p1!='o')
    {
        cout<<"ERROR\n";
        goto b;
        //exit(0);
    }
    int winner_boy;
    current_marker=marker_p1;


    for(int j=0;j<=9;j++)
    {

        if(j%2==0)
        {
          cout<<"Player "<<"user"<<"'s turn,enter slot value\n";
        cin>>slot;
        }
        else
        {
            //cout<<"Player "<<"computer"<<"'s turn,enter slot value\n";

            //source: bitdegree.org
            srand((unsigned) time(0));
            int a;

              a = (rand() % 10) + 1;
             //cout << a;

                slot=a;
               // cin>>slot;
        }

        if(slot<1 || slot>9)
        {

            if(current_player==1)

            {cout<<"WRONG INPUT\n";
            j--;
            continue;
            }
            if(current_player==2)
              { //cout<<"WRONG INPUT\n";
                j--;
                continue;
              }

        }

        if(!marker_placing(slot))
        {
            if(current_player==1)
            {
                cout<<"slot occupied\n";
            j--;
            continue;

            }
            if(current_player==2)
            {
                //cout<<"slot occupied\n";
                j--;
                continue;
            }

        }
        int winner_boy=winner();
        drawboard();
        if(winner_boy==1)
        {
            cout<<"*************Congo user****************\n";
            exit(0);
            //break;
        }
        if(winner_boy==2)
        {
            cout<<"*************Congo computer****************\n";
            exit(0);
            //break;
        }
        swap_computer();


    }
    if(winner_boy==0)
        {
            cout<<"TIE";
            exit(0);
        }


}
//$$$$$$$$$$$$$$$%%%%%%%%%%%%%^^^^^^^^^^^^^^  AI  ^^^^^^^^^^^^^^%%%%%%%%%%%%%$$$$$$$$$$$$$$$
void AI()
{
    cout<<"UNDER WORK!";
    exit(0);
}

int main()
{
   cout<<"------TIC TAC TOE------\n\n\n";
   cout<<"!__MENU__!\n\n";
   cout<<"1.Multiplayer\n"<<"2.Against Computer [Easy]\n"<<"3.Against AI\n\n\n";
   int input;
   cout<<"Enter choice   :\t\t";
   cin>>input;

   switch(input)
   {
       case 1: game();
                break;
       case 2: computer();
                break;
       case 3:  AI();
                break;
       default: cout<<"wait up";
   }

   game();
   return 0;

}
