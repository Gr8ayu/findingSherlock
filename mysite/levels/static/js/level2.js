$(document).ready(function(){

  // $("#btn1").click(function(){
    $("#text").text("915BF19648AC5F6068CFB34163B6B4E9");
    $("#text").css("color", "black");


  $("#submitData").click(function(){
    username = $("#username").val();
    password = $("#password").val()

    if (password == "049DCA6B1BA0235FAC48A2B596E1804C" && username != ""  ){

      
      $.ajax({
         url: '/levels/1/',
         data: {'username': username, 'password':password},
         type: 'POST'
       }).done(function(response){
         console.log(response);
         alert("correct");
      
       });
     
    }

    else {

       alert("wrong");
    }

  });
});