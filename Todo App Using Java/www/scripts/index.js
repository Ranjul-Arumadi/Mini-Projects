// For an introduction to the Blank template, see the following documentation:
// http://go.microsoft.com/fwlink/?LinkID=397704
// To debug code on page load in cordova-simulate or on Android devices/emulators: launch your app, set breakpoints, 
// and then run "window.location.reload()" in the JavaScript Console.
(function () {
    "use strict";

    document.addEventListener( 'deviceready', onDeviceReady.bind( this ), false );

    function onDeviceReady() {

        var db = window.openDatabase("Database", "1.0", "Cordova Demo", 200000);
        db.transaction(populateDB, errorCB, successCB);
        // Handle the Cordova pause and resume events
      //  document.addEventListener( 'pause', onPause.bind( this ), false );
       // document.addEventListener( 'resume', onResume.bind( this ), false );
        
        // TODO: Cordova has been loaded. Perform any initialization that requires Cordova here.
       // var parentElement = document.getElementById('deviceready');
       // var listeningElement = parentElement.querySelector('.listening');
       // var receivedElement = parentElement.querySelector('.received');
      //  listeningElement.setAttribute('style', 'display:none;');
      //  receivedElement.setAttribute('style', 'display:block;');

      
        
    };

    document.getElementById("addbtn2").addEventListener("click", add);
    document.getElementById("addbtn2").addEventListener("click", displayContacts);

    var nameArray = [];
    var numberArray = [];

    function add() {
        console.log("in add");

        var name = document.getElementById('box1').value;
        nameArray.push(name);
        console.log(nameArray);

        var number = document.getElementById('box2').value;
        numberArray.push(number);
        console.log(numberArray);
    }

    var i = -1;
    //displayContacts();
    function displayContacts() {
        i = i + 1;
        console.log("in display");
        var nameArrLen, numberArrLen;
        var increment = 0;
        nameArrLen = nameArray.length;
        
        numberArrLen = numberArray.length;


            
                console.log("in for of display");
                
                var table = document.getElementById("displayTable");
                var row = table.insertRow(increment);
                increment++;
                var cell1 = row.insertCell(0);
                cell1.innerHTML = nameArray[i];
                var cell2 = row.insertCell(1);
                cell2.innerHTML = numberArray[i];
            
            
            
   
        
    }


    var searchValue = document.getElementById("searchBox").value;
    document.getElementById("addbtn").addEventListener("click", searchContact);

    function searchContact() {

        console.log("in searcch");

        var searchedValue = document.getElementById("searchBox").value;

        var nameArrLen, numberArrLen, i;
       
        nameArrLen = nameArray.length;
        console.log(nameArrLen);
        numberArrLen = numberArray.length;
        console.log(numberArrLen);

       
        for (i = 0; i < nameArrLen; i++) {
            console.log(nameArray[i]);
            if (nameArray[i] == searchedValue) {

                console.log("true");
                var firstArrayindex = i;
                var foundContact = numberArray[i];
                document.getElementById("resultBox").value = foundContact;
                break;
            }
            else
            {
                console.log("false");
                var message = "Name not found";
                document.getElementById("resultBox").value = message;
            }
        }
        
    }

    function onPause() {
        // TODO: This application has been suspended. Save application state here.
    };

    function onResume() {
        // TODO: This application has been reactivated. Restore application state here.
    };
} )();