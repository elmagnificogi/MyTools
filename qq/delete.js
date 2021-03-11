// 寻找qq群高级管理页面中的加群时间和最后发言时间相同的人
// 自动勾选，之后可以直接删除这种人，每次选人不超过20个

var tableId = document.getElementById("groupMember");
var join_time = ""
var last_speak_time = ""
var delete_count = 0
console.log(tableId.rows.length)
for(var i=1;i<tableId.rows.length;i++)
{
    var user_name = tableId.rows[i].cells[2]
    join_time = tableId.rows[i].cells[7].innerHTML.replace(/\s+/g,"");
    last_speak_time = tableId.rows[i].cells[9].innerHTML.replace(/\s+/g,"");
    if(join_time==last_speak_time)
    {
        console.log(last_speak_time)
        console.log(user_name)

        // select the user
        var input_check = tableId.rows[i].cells[0].childNodes[1];
        input_check.checked=true;

        delete_count++;
        //alert(user_name)
    }

    if(delete_count==20)
    {
        //alert("找到20个")
        break;
    }


}