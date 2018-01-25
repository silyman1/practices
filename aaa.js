
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