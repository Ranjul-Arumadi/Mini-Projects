import java.util.*;
class main{
	public static void main(String[] args){
		guess();
	}
	public static void guess(){
		Scanner sc = new Scanner(System.in);
		int computerNumber = (int) (Math.random()*100 + 1);
		System.out.println(computerNumber);
		int userAnswer = 0;
		int chances = 5;
		
		System.out.println("Enter a number from 1 - 100: ");
		do{
			userAnswer = sc.nextInt();
			if(userAnswer>100 || userAnswer<1){
				System.out.println("Please input values in the range 1-100 only");
			}
			else{
				chances--;
				if(userAnswer==computerNumber){
					System.out.println("Right guess!. You won with "+chances+" chances remaining");
					System.exit(0);
				}
				else if(userAnswer>computerNumber){
					System.out.println("Guess lower value "+chances+" chances remaining");
				}
				else if(userAnswer<computerNumber){
					System.out.println("Guess higher value "+chances+" chances remaining");
				}
				
				if(Math.abs(computerNumber-userAnswer)<=3){
					System.out.println("You are very close!");
				}
			}
			
		}while(chances>0);
		
		System.out.println("Ops!. All chances over!. Better luck next time :)");
		System.exit(0);
	}
}
