<!--Ranjus calculator -->
<html>
<head>
<title> calculator </title>
</head>
<body>


<form action="" method="post">

	<h1> <u><b>Calculator<b></u></h1>
	<div>
	<p>Enter first number :</p>
    <input type="text" name="num1" placeholder="" required>
	</div>
	</br>
	
	<div>
	<p>Enter second number :</p>
    <input type="text" name="num2" placeholder="" required>
	</div>
	<br>
	
	<div>
	<p>Choose operator</p>
    <select name="operator">
        <option>+</option>
        <option>-</option>
        <option>/</option>
        <option>*</option>
    </select>
	</div>
    <br>
    <button type="submit" name="submitbtn"value="submit">Calculate</button>    
</form>
<p>The answer is : </p>
<?php
    if(isset($_POST['submitbtn'])){
        $result1=$_POST['num1'];
        $result2=$_POST['num2'];
        $operator=$_POST['operator'];
		$result3=0;
		
		if($result2==0 && $operator=='/'){
			exit("Division by 0 is not possible");
			
		}
        
    switch($operator)
        {
            case "None":
                $result3="error";
                break;

            case '+': 
                $result3=$result1+$result2;
                break;

            case '-':
                $result3=$result1-$result2; 
                break;

            
            case '*': 
                $result3=$result1*$result2;  
                break;

            
            case '/':  
                $result3=$result1/$result2;   
                break;

            default: echo "something's wrong"; 
            
        }
        echo $result3;
     }
     
?>


</body>
</html>
