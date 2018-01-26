
function myFunction()
{
    document.getElementById("demo").innerHTML="我的第一个 JavaScript 函数";
}

function checkboxed(objName){
    var objNameList=document.getElementsByName(objName);    

    if(null!=objNameList){
        for(var i=0;i<objNameList.length;i++){
            objNameList[i].checked="checked";
        }
    }
}

function uncheckboxed(objName){
    var objNameList=document.getElementsByName(objName);    

    if(null!=objNameList){
        for(var i=0;i<objNameList.length;i++){
            objNameList[i].checked="";
        }
    }
}
var checkAll = false;
function allcheck(){
    checkAll = !checkAll;
    var inputs = document.getElementsByName('checkbox')
    if (checkAll){
    for(var i =0;i<inputs.length;i++){inputs[i].checked = 'checked'}
	}
	else{
    for(var i =0;i<inputs.length;i++){inputs[i].checked = ''}
	}
}
function opennew(){
	window.open();
}
function setCookie(cname,cvalue,exdays){
	var d = new Date();
	d.setTime(d.getTime()+exdays*24*60*60*1000)
	var expires = "expires="+d.toGMTString();
	document.cookie =cname+ "="+ cvalue +";" +expires;
}
function getCookies(cname)
{
	var name = cname + "=";
	var ca = document.cookie.split(';');
	for (var i =0,i<ca.length;i++)
	{
		var c = ca[i].trim();
		if(c.indexOf(name)==0) return c.substring(name.length,c.length);
	}
	return "";
}
function checkCookie()
{
  var username=getCookie("username");
  if (username!="")
  {
    alert("Welcome again " + username);
  }
  else 
  {
    username = prompt("Please enter your name:","");
    if (username!="" && username!=null)
    {
      setCookie("username",username,365);
    }
  }
}